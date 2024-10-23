import logging
from typing import Optional

from neutrino_client.client import _NeutrinoClient
from neutrino_client.neutrino_task import NeutrinoTask
from neutrino_client.task_pb2 import TaskInput

neutrino: Optional[_NeutrinoClient] = None


def init(dsn: str,
         secure: bool = True,
         host: str = "application",
         runner: str = '',
         application: str = 'application',
         timeout_in_seconds: Optional[float] = 1.0,
         reconnect_on_connection_lost: Optional[bool] = False,
         keep_alive_time_ms: int = 30000,
         keepalive_timeout_ms: int = 5000):
    _NeutrinoClient(dsn=dsn, host=host,application=application,runner=runner, secure=secure, timeout_in_seconds=timeout_in_seconds,
                    reconnect_on_connection_lost=reconnect_on_connection_lost, keep_alive_time_ms=keep_alive_time_ms,
                    keepalive_timeout_ms=keepalive_timeout_ms)


def publish_task_info(task: NeutrinoTask):
    """
    Constructs TaskInput() object from param
    Invokes client.send_message(task_input)
    All kinds of exceptions are suppressed so that client is not affected
    """
    try:
        task_input = TaskInput()
        task_input.task_id = task.task_id
        task_input.task_name = task.task_name
        task_input.threshold = task.threshold
        task_input.threshold_unit = task.threshold_unit
        task_input.status = task.status
        task_input.type = task.type
        for k, v in task.additional_data.items():
            task_input.additional_data[k] = v
        _NeutrinoClient.send_message(task_input)
    except Exception as e:
        logging.info(f"neutrino: error while sending task info {str(e)}")


def get_grpc_channel():
    return _NeutrinoClient.get_channel()
