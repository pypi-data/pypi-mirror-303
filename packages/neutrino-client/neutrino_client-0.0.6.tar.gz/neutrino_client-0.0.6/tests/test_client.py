import neutrino_client


def test_init():
    neutrino_client.init(dsn="localhost:9999")
    grpc_channel = neutrino_client.get_grpc_channel()
    assert grpc_channel


def test_capture_task():
    neutrino_client.init(dsn="localhost:9999")
    task = neutrino_client.NeutrinoTask(
        task_name="task name",
        task_id="abcd",
        status="IN_PROGRESS"
    )
    neutrino_client.publish_task_info(task)
