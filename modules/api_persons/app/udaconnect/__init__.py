def register_routes(api, app, root="api"):
    from app.udaconnect.controllers import api as udaconnect_persons_api

    api.add_namespace(udaconnect_persons_api, path=f"/{root}")
