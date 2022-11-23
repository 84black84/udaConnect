def register_routes(api, app, root="api"):
    from app.udaconnect.controllers import api as udaconnect_locations_api

    api.add_namespace(udaconnect_locations_api, path=f"/{root}")