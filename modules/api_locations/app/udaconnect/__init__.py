from app.udaconnect.controllers import api as udaconnect_locations_api

def register_routes(api):
    '''
        Register all the routes defined in the controllers of the api.
    '''
    root="api"
    api.add_namespace(udaconnect_locations_api, path=f"/{root}")