from cbr_user_session.utils.Version         import version__cbr_user_session
from osbot_fast_api.api.Fast_API_Routes     import Fast_API_Routes


class Routes__Info(Fast_API_Routes):
    tag : str = 'info'

    def ping(self):
        return {"pong" : '42' }

    def version(self):
        return {"version" : version__cbr_user_session }

    def setup_routes(self):
        self.add_route_get(self.ping   )
        self.add_route_get(self.version)
        return self