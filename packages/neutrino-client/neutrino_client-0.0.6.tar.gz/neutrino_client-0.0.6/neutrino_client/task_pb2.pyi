from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class TaskInput(_message.Message):
    __slots__ = ("task_id", "task_name", "timestamp", "type", "status", "threshold", "threshold_unit", "additional_data", "host", "application", "runner")
    class AdditionalDataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    TASK_NAME_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    THRESHOLD_UNIT_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_DATA_FIELD_NUMBER: _ClassVar[int]
    HOST_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_FIELD_NUMBER: _ClassVar[int]
    RUNNER_FIELD_NUMBER: _ClassVar[int]
    task_id: str
    task_name: str
    timestamp: str
    type: str
    status: str
    threshold: int
    threshold_unit: str
    additional_data: _containers.ScalarMap[str, str]
    host: str
    application: str
    runner: str
    def __init__(self, task_id: _Optional[str] = ..., task_name: _Optional[str] = ..., timestamp: _Optional[str] = ..., type: _Optional[str] = ..., status: _Optional[str] = ..., threshold: _Optional[int] = ..., threshold_unit: _Optional[str] = ..., additional_data: _Optional[_Mapping[str, str]] = ..., host: _Optional[str] = ..., application: _Optional[str] = ..., runner: _Optional[str] = ...) -> None: ...

class TaskOutput(_message.Message):
    __slots__ = ("response",)
    class ResponseEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    response: _containers.ScalarMap[str, str]
    def __init__(self, response: _Optional[_Mapping[str, str]] = ...) -> None: ...
