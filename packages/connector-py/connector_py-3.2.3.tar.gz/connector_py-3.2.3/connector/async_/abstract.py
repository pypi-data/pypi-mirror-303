from connector.helpers import collect_methods, validate_commands
from connector.serializers.abstract import Info
from connector.utils.info import generate_capability_schema


class AbstractCommands:
    app_id: str

    def __init__(self, app_id: str = ""):
        self.app_id = self.app_id or app_id
        self.validate()

    def validate(self) -> None:
        validate_commands(self)

    async def info(self) -> Info:
        if not hasattr(self, "app_id"):
            raise NotImplementedError("app_id attribute is required")
        methods = collect_methods(self)
        capabilities, objects = generate_capability_schema(methods)

        return Info(
            app_id=self.app_id,
            capabilities=sorted(capabilities),
            capability_schema=objects,
        )
