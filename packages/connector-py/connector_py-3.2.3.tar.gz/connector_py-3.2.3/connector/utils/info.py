import json
from types import FunctionType

from connector.serializers.abstract import CommandTypes, EmptyModel


def generate_capability_schema(
    methods: list[FunctionType],
) -> tuple[list[str], dict[str, CommandTypes]]:
    objects = {}
    capabilities = []
    for method in methods:
        capabilities.append(name := method.__name__.lower().replace("_", "-"))

        annotations = method.__annotations__
        output = annotations.pop("return", EmptyModel)
        if len(keys := tuple(annotations.keys())) > 0:
            argument_model = annotations[keys[0]]
        else:
            argument_model = EmptyModel

        objects[name] = CommandTypes(
            argument=json.dumps(argument_model.model_json_schema(), sort_keys=True),
            output=json.dumps(output.model_json_schema(), sort_keys=True),
        )

    return capabilities, objects
