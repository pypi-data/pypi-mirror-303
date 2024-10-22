from osbot_fast_api.api.Fast_API_Routes import Fast_API_Routes


class Routes__Session(Fast_API_Routes):

    def session_exists(self, session_id):
        return False

    def setup_routes(self):
        self.add_route_get(self.session_exists)