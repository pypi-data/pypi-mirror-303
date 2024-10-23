from mxl.config import config


class MXLTracker:
    def __init__(self):
        # resource_attributes = os.environ.get("OTEL_RESOURCE_ATTRIBUTES")
        # _service_name = os.environ.get("OTEL_SERVICE_NAME")
        # _project_name = self._get_project_name(resource_attributes)

        self.project_name = config.project_name
        self.service_name = config.service_name
        self.access_token = config.access_token or ""
