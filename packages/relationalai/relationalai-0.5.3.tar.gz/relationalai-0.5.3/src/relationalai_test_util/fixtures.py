from __future__ import annotations
import random
import os
import subprocess
from typing import cast, Optional

import snowflake.connector

import relationalai as rai
from relationalai import debugging
from relationalai.clients.profile_polling import TransactionEventsFeedbackHandler
from relationalai.debugging import logger
from relationalai.clients import config as cfg
from relationalai.util.snowflake_handler import SnowflakeHandler
from relationalai.util.span_format_test import SpanCollectorHandler, assert_valid_span_structure
from relationalai.util.span_tracker import TRACE_ID

def graph_index_config_fixture():
    cloud_provider = os.getenv("RAI_CLOUD_PROVIDER")
    if cloud_provider:
        config = make_config()
    else: 
        config = cfg.Config()

    config.set("use_graph_index", True)
    yield config
    return

def engine_config_fixture(size):
    # Check for an externally provided engine name
    # It is used in GitHub Actions to run tests against a specific engine
    engine_name = os.getenv("ENGINE_NAME")
    if engine_name:
        # If engine name was provided, just yield the config
        config = make_config(engine_name)
        yield config
        return

    # If there's a local config file, use it, including
    # the engine specified there.
    config = cfg.Config()
    if config.file_path is not None:
        yield config
        return

    # Otherwise, create a new engine and delete it afterwards.
    random_number = random.randint(1000000000, 9999999999)
    engine_name = f"pyrel_test_{random_number}"
    create_engine(engine_name, size=size)

    yield make_config(engine_name)

    delete_engine(engine_name)

def create_engine(engine_name: str, size: str):
    print('create_engine: about to call make_config')
    config = make_config(engine_name)

    sf_compute_pool = cast(str, os.getenv("SF_TEST_COMPUTE_POOL", config.get("compute_pool", "")))

    provider = rai.Resources(config=config)
    print(f"Creating engine {engine_name}")
    provider.create_engine(name=engine_name, size=size, pool=sf_compute_pool)
    print(f"Engine {engine_name} created")


def delete_engine(engine_name: str):
    print(f"Deleting engine {engine_name}")
    config = make_config(engine_name)
    provider = rai.Resources(config=config)
    provider.delete_engine(engine_name)
    print(f"Engine {engine_name} deleted")

def make_config(engine_name: str | None = None) -> cfg.Config:
    cloud_provider = os.getenv("RAI_CLOUD_PROVIDER")
    
    print('cloud provider:', cloud_provider)
    
    if cloud_provider is None:
        raise ValueError("RAI_CLOUD_PROVIDER must be set")
    elif cloud_provider == "azure":
        client_id = os.getenv("RAI_CLIENT_ID")
        client_secret = os.getenv("RAI_CLIENT_SECRET")
        if client_id is None or client_secret is None:
            raise ValueError(
                "RAI_CLIENT_ID, RAI_CLIENT_SECRET must be set if RAI_CLOUD_PROVIDER is set to 'azure'"
            )
        
        # Pull from env vars; Default to prod
        host = os.getenv("RAI_AZURE_HOST") or "azure.relationalai.com"
        creds_url = os.getenv("RAI_AZURE_CLIENT_CREDENTIALS_URL") or "https://login.relationalai.com/oauth/token"
        region = os.getenv("RAI_AZURE_REGION") or "us-east"
    
        return cfg.Config(
            
            {
                "platform": "azure",
                "host": host,
                "port": "443",
                "region": region,
                "scheme": "https",
                "client_credentials_url": creds_url,
                "client_id": client_id,
                "client_secret": client_secret,
                "engine": engine_name,
            }
        )

    elif cloud_provider == "snowflake":
        sf_username = os.getenv("SF_TEST_ACCOUNT_USERNAME")
        sf_password = os.getenv("SF_TEST_ACCOUNT_PASSWORD")
        sf_account = os.getenv("SF_TEST_ACCOUNT_NAME")
        sf_role = os.getenv("SF_TEST_ROLE_NAME", "RAI_CONSUMER")
        sf_warehouse = os.getenv("SF_TEST_WAREHOUSE_NAME")
        sf_app_name = os.getenv("SF_TEST_APP_NAME")
        sf_compute_pool = os.getenv("SF_TEST_COMPUTE_POOL")
        if sf_username is None or sf_password is None:
            raise ValueError(
                "SF_TEST_ACCOUNT_USERNAME, SF_TEST_ACCOUNT_PASSWORD, SF_TEST_ACCOUNT_NAME must be set if RAI_CLOUD_PROVIDER is set to 'snowflake'"
            )

        current_config = {
            "platform": "snowflake",
            "user": sf_username,
            "password": sf_password,
            "account": sf_account,
            "role": sf_role,
            "warehouse": sf_warehouse,
            "rai_app_name": sf_app_name,
            "compute_pool": sf_compute_pool,
        }
        if engine_name:
            current_config["engine"] = engine_name
        return cfg.Config(current_config)

    else:
        raise ValueError(f"Unsupported cloud provider: {cloud_provider}")

def snowflake_handler_fixture():
    if not os.getenv("SF_REPORTING_PASSWORD"):
        print('snowflake logger disabled since required config env vars not present')
        yield
        return

    conn = snowflake.connector.connect(
        user=os.getenv("SF_REPORTING_USER"),
        password=os.getenv("SF_REPORTING_PASSWORD"),
        account=os.getenv("SF_REPORTING_ACCOUNT"),
        role=os.getenv("SF_REPORTING_ROLE"),
        warehouse=os.getenv("SF_REPORTING_WAREHOUSE"),
        database=os.getenv("SF_REPORTING_DATABASE"),
        schema=os.getenv("SF_REPORTING_SCHEMA"),
    )
    snowflake_handler = SnowflakeHandler(TRACE_ID, conn)
    logger.addHandler(snowflake_handler)
    yield
    snowflake_handler.shut_down()

def profile_poller_fixture(engine_config):
    resources = rai.Resources(config=engine_config)
    handler = TransactionEventsFeedbackHandler(resources)
    logger.addHandler(handler)
    yield

def span_structure_validator_fixture():
    handler = SpanCollectorHandler()
    logger.addHandler(handler)
    yield handler
    logger.removeHandler(handler)
    assert_valid_span_structure(handler.nodes, handler.events)

def root_span_fixture(get_full_config=False, span_type: str = "test_session", extra_attrs: Optional[dict] = None):
    root_span_attrs = _get_root_span_attrs(get_full_config)
    if extra_attrs:
        root_span_attrs.update(extra_attrs)
    with debugging.span(span_type, **root_span_attrs):
        yield

#region root_span_fixture helper functions
def _get_local_git_info():
    try:
        branch = subprocess.check_output(['git', 'rev-parse', '--abbrev-ref', 'HEAD']).strip().decode('utf-8')
        sha = subprocess.check_output(['git', 'rev-parse', 'HEAD']).strip().decode('utf-8')
        repo = subprocess.check_output(['git', 'config', '--get', 'remote.origin.url']).strip().decode('utf-8').rsplit('/', maxsplit=1)[-1].replace('.git', '')
        return {
            'commit': sha,
            'branch': branch,
            'repo': repo,
        }
    except subprocess.CalledProcessError as e:
        logger.warning(f"Could not get git info: {e}")
        return {
            'commit': 'local',
            'branch': 'local',
            'repo': 'local',
        }

def _get_git_info():
    if os.getenv("GITHUB_REF_NAME") is not None:
        return {
            'commit': os.getenv("GITHUB_SHA"),
            'branch': os.getenv("GITHUB_REF_NAME"),
            'repo': os.getenv("GITHUB_REPOSITORY"),
        }
    return _get_local_git_info()

def _get_masked_config():
    """Return a config with all sensitive keys (secrets and passwords) removed, such that it can be safely logged"""
    #TODO: This might not be accurate if engine_config_fixture results in a new engine being created
    config = cfg.Config()
    masked_props = {
        k: v for k, v in config.props.items()
        if not isinstance(v, str)
        or not any(prop_key_pattern in k for prop_key_pattern in ["secret", "password"])
    }
    return masked_props

def _get_cloud_provider():
    provider = os.getenv("RAI_CLOUD_PROVIDER")
    if not provider:
        config = cfg.Config()
        provider = config.get("platform")
    assert provider, "Could no retrieve cloud provider from environment or config"
    return {"platform": provider} # Calling it `platform` to match the key used in the config

def _get_root_span_attrs(get_full_config=False):
    git_info = _get_git_info()
    cloud_provider = _get_cloud_provider()
    masked_config = _get_masked_config() if get_full_config else {}
    attrs = {
        **git_info,
        **cloud_provider,
        **masked_config
    }
    return attrs

#endregion
