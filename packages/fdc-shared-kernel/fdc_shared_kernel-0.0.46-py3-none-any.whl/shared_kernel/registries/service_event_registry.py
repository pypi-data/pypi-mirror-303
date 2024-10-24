from shared_kernel.config import Config

config = Config()


class ServiceEventRegistry:
    # Sync events to master service to create/update status tracker
    CREATE_TASK = (
        config.get("MASTER_SERVICE_BASE_ENDPOINT")
        + "/event/subscribe-sync-event/CREATE_TASK/"
    )

    UPDATE_TASK = (
        config.get("MASTER_SERVICE_BASE_ENDPOINT")
        + "/event/subscribe-sync-event/UPDATE_TASK/"
    )

    MARK_TASK_AS_FAILURE = (
        config.get("MASTER_SERVICE_BASE_ENDPOINT")
        + "/event/subscribe-sync-event/MARK_TASK_AS_FAILURE/"
    )
