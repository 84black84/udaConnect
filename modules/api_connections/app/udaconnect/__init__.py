from app.udaconnect.controllers import api as udaconnect_connections_api

def register_routes(api):
    root="api"
    api.add_namespace(udaconnect_connections_api, path=f"/{root}")