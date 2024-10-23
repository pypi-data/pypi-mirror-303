from __future__ import annotations
import importlib.metadata
from typing import cast

from .clients.util import get_execution_environment, in_cloud_environment
from .clients import config as cfg
from .clients.config import Config
from . import dsl
from . import debugging
from . import metamodel
from . import rel
from .loaders import csv
from . import analysis
from . import tools
from snowflake.snowpark import Session
from snowflake.snowpark.context import get_active_session
from .errors import RAIException, SnowflakeIntegrationMissingException

# Set up global exception handler for debugging
debugging.setup_exception_handler()
debugging.install_warninghook()

__version__ = importlib.metadata.version(__package__ or __name__)

def Model(
    name: str,
    *,
    profile: str | None = None,
    config: Config | None = None,
    dry_run: bool | None = False,
    debug: bool | None = None,
    debug_host: str | None = None,
    debug_port: int | None = None,
    connection: Session | None = None,
    keep_model: bool | None = None,
    isolated: bool | None = None,
    nowait_durable: bool | None = None,
    use_package_manager: bool | None = None,
    format: str = "default",
):
    config = config or Config(profile=profile)
    if use_package_manager is not None:
        config.set("use_package_manager", use_package_manager)

    execution_environment = get_execution_environment()

    environments_that_provide_a_session = {"snowflake_notebook", "hex"}

    if execution_environment in environments_that_provide_a_session:
        if execution_environment == "snowflake_notebook":
            session = get_active_session()
            connection = session
        if connection is not None:
            config.set("platform", "snowflake")
            user = connection.sql("select current_user()").collect()[0][0]
            assert isinstance(user, str), "Could not retrieve current user"
            config.set("user", user)
            config.file_path = "__inline__"
        elif execution_environment == "hex" and config.get("user", None) is None:
            raise ValueError("A Session object should be provided when running in Hex. Import `hextoolkit` and supply `connection=hextoolkit.get_data_connection('<your connection name>').get_snowpark_session()` as an argument to `Model`.")

    if debug is None:
        if in_cloud_environment():
            debug = False
        else:
            config_debug = config.get("debug", True)
            if isinstance(config_debug, dict):
                debug = True
            elif isinstance(config_debug, bool):
                debug = config_debug
            else:
                raise Exception("Invalid value specified for `debug`, expected `true` or `false`.")

    if debug_host is None:
        # Our get function isn't robust to allowing `debug = true/false` or `[debug]\n  port=...`
        # Went with the lowest impact solve for now which is handling it locally.
        try:
            debug_host = config.get("debug.host", None)
        except AttributeError:
            pass

    if debug_port is None:
        try:
            config_debug_port = config.get("debug.port", 8080)
            if not isinstance(config_debug_port, int):
                raise Exception("Invalid value specified for `debug.port`, expected `int`.")
            debug_port = config_debug_port
        except AttributeError:
            pass

    if debug:
        from relationalai.tools.debugger_client import start_debugger_session
        start_debugger_session(config, host=debug_host, port=debug_port)
    if not config.file_path:
        if cfg.legacy_config_exists():
            message = (
                "Use `rai init` to migrate your configuration file "
                "to the new format (raiconfig.toml)"
            )
        else:
            message = "No configuration file found. Please run `rai init` to create one."
        raise Exception(message)
    if config.get("platform", None) is None:
        config.set("platform", "snowflake")
    platform = config.get("platform")
    if platform != "snowflake" and connection is not None:
        raise ValueError("The `connection` parameter is only supported with the Snowflake platform")
    if dry_run is None:
        dry_run = config.get_bool("compiler.dry_run", False)
    if keep_model is None:
        keep_model = config.get_bool("model.keep", False)
    if isolated is None:
        isolated = config.get_bool("model.isolated", True)
    if nowait_durable is None:
        nowait_durable = config.get_bool("model.nowait_durable", True)

    try:
        if platform == "azure":
            import relationalai.clients.azure as azure
            model = azure.Graph(
                name,
                profile=profile,
                config=config,
                dry_run=dry_run,
                isolated=isolated,
                keep_model=keep_model,
                format=format,
            )
        elif platform == "snowflake":
            from relationalai.clients import snowflake
            model = snowflake.Graph(
                name,
                profile=profile,
                config=config,
                dry_run=dry_run,
                isolated=isolated,
                connection=connection,
                keep_model=keep_model,
                nowait_durable=nowait_durable,
                format=format,
            )
        else:
            raise Exception(f"Unknown platform: {platform}")
    except RAIException as e:
        raise e.clone() from None
    except Exception as e:
        if (
            "NameResolutionError" in str(e)
            and get_execution_environment() == "snowflake_notebook"
        ):
            raise SnowflakeIntegrationMissingException() from None
        raise e
    return model


def Resources(
    profile: str | None = None,
    config: Config | None = None,
    connection: Session | None = None,
):
    config = config or Config(profile)
    platform = config.get("platform", "snowflake")
    if platform == "azure":
        from relationalai.clients.azure import Resources
        return Resources(config=config)
    elif platform == "snowflake":
        from relationalai.clients.snowflake import Resources
        return Resources(config=config, connection=connection)
    else:
        raise Exception(f"Unknown platform: {platform}")

def Provider(
    profile: str | None = None,
    config: Config | None = None,
    connection: Session | None = None,
):
    resources = Resources(profile, config, connection)
    platform = resources.config.get("platform", "snowflake")
    if platform == "azure":
        import relationalai.clients.azure
        resources = cast(relationalai.clients.azure.Resources, resources)
        return relationalai.clients.azure.Provider(
            resources=resources
        )
    elif platform == "snowflake":
        import relationalai.clients.snowflake
        resources = cast(relationalai.clients.snowflake.Resources, resources)
        return relationalai.clients.snowflake.Provider(
            resources=resources,
        )
    else:
        raise Exception(f"Unknown platform: {platform}")


def Graph(name:str, dry_run:bool=False):
    return Model(name, profile=None, dry_run=dry_run)

__all__ = ['Model', 'Config', 'Resources', 'Provider', 'dsl', 'rel', 'debugging', 'metamodel', 'csv', 'analysis', 'tools']
