from osbot_fast_api.api.Fast_API                        import Fast_API
from cbr_user_session.fast_api.routes.Routes__Info      import Routes__Info


class User_Session__Fast_API(Fast_API):
    base_path      : str  = '/user-session'
    enable_cors    : bool = True
    default_routes : bool = False

    def setup_routes(self):
        self.add_routes(Routes__Info   )