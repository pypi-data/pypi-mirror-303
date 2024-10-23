import json

from fastapi import Request

from connector.capability import CapabilityName
from connector.generated import CapabilityName as OpenApiCapabilityName
from connector.helpers import collect_methods
from connector.oai.integration import Integration


def collect_routes(obj: object):
    """
    Collect all methods from an object and create a route for each.
    """
    from fastapi import APIRouter

    router = APIRouter()
    commands = collect_methods(obj)
    for method in commands:
        router.add_api_route(f"/{method.__name__.replace('_', '-')}", method, methods=["POST"])
    return router


def create_req_handler(
    capability: CapabilityName | OpenApiCapabilityName,
    integration: Integration,
):
    async def req_handler(request: Request):
        body = await request.body()
        req_str = body.decode()
        integration.handle_errors = True
        response = await integration.dispatch(OpenApiCapabilityName(capability), req_str)
        return json.loads(response)

    return req_handler


def collect_integration_routes(
    integration: Integration,
    prefix_app_id: bool = False,
):
    """Create API endpoint for each method in integration."""
    from fastapi import APIRouter

    router = APIRouter()
    for capability_name, _ in integration.capabilities.items():
        prefix = f"/{integration.app_id}" if prefix_app_id else ""
        # replace `-` in prefix (e.g. app_id) and capability name
        route = f"{prefix}/{capability_name.value}".replace("-", "_")
        handler = create_req_handler(capability_name, integration)
        router.add_api_route(route, handler, methods=["POST"])

    return router


def runserver(router, port: int):
    import uvicorn
    from fastapi import FastAPI

    app = FastAPI()
    app.include_router(router)

    uvicorn.run(app, port=port)
