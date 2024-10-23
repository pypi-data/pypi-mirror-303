from osbot_local_stack.local_stack.Local_Stack          import Local_Stack
from cbr_user_session.User_Session__Config              import user_session__config
from cbr_user_session.fast_api.routes.Routes__Guest     import Routes__Guest
from cbr_user_session.fast_api.routes.Routes__Guests    import Routes__Guests
from cbr_user_session.fast_api.routes.Routes__Session   import Routes__Session
from osbot_fast_api.api.Fast_API                        import Fast_API
from cbr_user_session.fast_api.routes.Routes__Info      import Routes__Info


class User_Session__Fast_API(Fast_API):
    base_path      : str  = '/user-session'
    enable_cors    : bool = True
    default_routes : bool = False

    def setup(self):
        user_session__config.setup()
        self.setup__local_stack()
        super().setup()
        return self

    def setup__local_stack(self):
        if user_session__config.use_local_stack:
            Local_Stack().activate()

    def setup_routes(self):
        self.add_routes(Routes__Info   )
        self.add_routes(Routes__Session)
        self.add_routes(Routes__Guest  )
        self.add_routes(Routes__Guests )