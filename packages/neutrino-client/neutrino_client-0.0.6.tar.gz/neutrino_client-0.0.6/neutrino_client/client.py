import logging
from typing import Optional

import grpc
from neutrino_client.task_pb2_grpc import TaskStub
from neutrino_client.task_pb2 import TaskInput
import logging as log


class _NeutrinoClient:
    _grpc_channel: Optional[grpc.Channel] = None
    _secure = True
    _host = "application"
    _application = "application"
    _runner = ""
    _stub: Optional[TaskStub] = None
    _timeout_in_seconds: float = 1.0
    _reconnect_on_connection_lost: bool = False
    _dsn: str = None
    _keepalive_time_ms: int
    _keepalive_timeout_ms: int

    def __new__(cls, dsn: str,
                secure: bool,
                host:str,
                application:str,
                runner:str,
                timeout_in_seconds: float,
                reconnect_on_connection_lost: bool,
                keep_alive_time_ms: int,
                keepalive_timeout_ms: int):
        """
        creates new gRPC channel and initializes the stub
        """
        cls._dsn = dsn
        cls._secure = secure
        cls._host = host
        cls._application = application
        cls._runner = runner
        cls._timeout_in_seconds = timeout_in_seconds
        cls._reconnect_on_connection_lost = reconnect_on_connection_lost
        cls._keepalive_time_ms = keep_alive_time_ms
        cls._keepalive_timeout_ms = keepalive_timeout_ms

        if cls._grpc_channel is None:
            try:
                cls._grpc_channel = cls._connect_to_neutrino_server(dsn)
            except Exception as e:
                log.info(f"neutrino:error creating grpc channel - {str(e)}")
                return

        if cls._stub is None:
            cls._stub = TaskStub(cls._grpc_channel)

        return cls._grpc_channel

    @classmethod
    def _connect_to_neutrino_server(cls, dsn: str) -> Optional[grpc.Channel]:
        try:
            options = [
                ('grpc.keepalive_time_ms', cls._keepalive_time_ms),
                ('grpc.keepalive_timeout_ms', cls._keepalive_timeout_ms),
            ]
            if cls._secure:
                logging.info("neutrino: connecting through secure channel")
                return grpc.secure_channel(dsn, grpc.ssl_channel_credentials(), options=options)
            logging.info("neutrino: connecting through insecure channel")
            return grpc.insecure_channel(dsn, options)
        except Exception as e:
            logging.info(f"error connect to grpc server {str(e)}")
            return

    @classmethod
    def _retry_init(cls):
        if cls._grpc_channel is None:
            cls._grpc_channel = cls._connect_to_neutrino_server(cls._dsn)

        if cls._stub is None:
            cls._stub = TaskStub(cls._grpc_channel)

    @classmethod
    def send_message(cls, task_input: TaskInput):
        """
        Invokes UpsertTaskInfo to send task information to gRPC server
        """
        if not cls._grpc_channel or not cls._stub:
            logging.info("neutrino: sdk not initialized, please initialize sdk")
            return

        try:
            task_input.host = cls._host
            task_input.application = cls._application
            task_input.runner = cls._runner
            cls._stub.UpsertTaskInfo(task_input, cls._timeout_in_seconds)
        except grpc.RpcError as e:
            logging.info(f"neutrino: error while publishing task info {str(e)}")
            if cls._reconnect_on_connection_lost:
                logging.info("neutrino: retrying to connect")
                cls._retry_init()
                cls._stub.UpsertTaskInfo(task_input, cls._timeout_in_seconds)
        except Exception as e:
            logging.error(f"neutrino: error while publishing task info {str(e)}")

    @classmethod
    def get_channel(cls):
        return cls._grpc_channel
