
import json
from logging import LogRecord
from typing import List, Tuple, Union
from uuid import UUID, uuid4

from relationalai.debugging import Span, encode_log_message, filter_span_attrs
from relationalai.util.constants import SPAN_ATTR_ALLOW_LIST, SPAN_TYPES_KEYS
from relationalai.util.format import default_serialize

TRACE_ID = uuid4()

class SpanTracker:
    """
    Abstract base class for tracking spans produced as log messages. 
    Provides methods to handle the start and end of spans, format span messages, and manage span attributes.
    """

    def __init__(self, trace_id: UUID, span_types_to_skip=None, log_span_attrs_as_str=True):
        self.trace_id = trace_id
        self._set_span_types_to_skip(span_types_to_skip)
        self._log_span_attrs_as_str = log_span_attrs_as_str
        self.open_spans = {}
        self.skipped_spans = set()

    def handle_span_start(self, msg: dict) -> Union[None,Span]:
        span: Span = msg["span"]
        assert_key_exists_for_span_type(span)
        if span.type in self.span_types_to_skip:
            self.skipped_spans.add(str(span.id))
            return None
        self.open_spans[str(span.id)] = span
        return span

    def handle_span_end(self, msg: dict) -> Tuple[Union[dict,None], Union[str,None], Union[dict,None]]:
        if str(msg["id"]) in self.skipped_spans:
            return None, None, None
        span = self.open_spans.pop(msg["id"])
        joined_key_path = get_span_path_as_str(span)
        end_attrs = get_span_allowed_attributes_values(span, msg["end_attrs"])
        combined_attributes = {
            **span.attrs, # span_start attrs
            **end_attrs, # span_end attrs
            "key_path": joined_key_path,
            "elapsed_s": (span.end_timestamp - span.start_timestamp).total_seconds(),
        }
        filtered_attrs = filter_span_attrs(combined_attributes)
        formatted_span_msg = format_span_msg(self.trace_id, span, filtered_attrs, attrs_as_str=self._log_span_attrs_as_str)
        return formatted_span_msg, joined_key_path, filtered_attrs

    def _set_span_types_to_skip(self, span_types_to_skip):
        if span_types_to_skip is None:
            self.span_types_to_skip = set()
        elif isinstance(span_types_to_skip, str):
            self.span_types_to_skip = {span_types_to_skip}
        elif isinstance(span_types_to_skip, (list, tuple)):
            self.span_types_to_skip = set(span_types_to_skip)
        elif isinstance(span_types_to_skip, set):
            self.span_types_to_skip = span_types_to_skip
        else:
            raise ValueError(f"Invalid span_types_to_skip: {span_types_to_skip}, type: {type(span_types_to_skip)}")


#region Span formatting and filtering functions
def format_span_msg(trace_id: UUID, span: Span, attrs: dict, attrs_as_str:bool=True) -> dict:
    span_key = get_span_value_from_key(span)
    if attrs_as_str:
        a = json.dumps(attrs, default=default_serialize)
    else:
        a = encode_log_message(attrs)

    span_json = span.to_json()
    extra_attrs = {
        "trace_id": str(trace_id),
        "key": str(span_key),
        "attrs": a
    }
    formatted_span_msg = {**span_json, **extra_attrs}
    return formatted_span_msg

def get_span_allowed_attributes_values(span: Span, attrs=None) -> dict:
    # For an input span with attrs (or instead for an `attrs` dict), return a dict with only the allowed attributes for the span type
    attrs = attrs or span.attrs
    out = {}
    allowed_attributes = SPAN_ATTR_ALLOW_LIST.get(span.type, set())
    for attr in allowed_attributes:
        if attr in attrs:
            out[attr] = attrs[attr]
    return out

def assert_key_exists_for_span_type(span: Span):
    if span.type in SPAN_TYPES_KEYS:
        key = SPAN_TYPES_KEYS[span.type]
        if key not in span.attrs:
            raise ValueError(f"Attribute {key} is required for spans of type {span.type}, but wasn't provided. Provided attributes:\n{span.attrs}")

def get_span_key_path(span: Span) -> str:
    # Return the key path of the current span
    value = get_span_value_from_key(span)
    if value is None:
        return span.type
    return f"{span.type}({value})"

def get_span_path_as_list(span: Span) -> List[Span]:
    # Return the path from the root to the current span
    path = []
    cur = span
    while cur is not None:
        path.append(cur)
        cur = cur.parent
    path.reverse()
    return path

def get_span_path_as_str(span: Span) -> str:
    # Return a string representation of the path from the root to the current span
    # formerly format_key_path function
    return '.'.join([get_span_key_path(span) for span in get_span_path_as_list(span)])

def get_span_value_from_key(span: Span):
    if span.type in SPAN_TYPES_KEYS:
        key = SPAN_TYPES_KEYS[span.type]
        if key in span.attrs:
            return span.attrs[key]
        raise ValueError(f"Key {key} not found in span of type {span.type}\n{span.attrs}")
    return None

def record_is_span(record: LogRecord) -> bool:
    return (
        isinstance(record.msg, dict) and
        "event" in record.msg and
        record.msg["event"] in ("span_start", "span_end")
    )
#endregion
