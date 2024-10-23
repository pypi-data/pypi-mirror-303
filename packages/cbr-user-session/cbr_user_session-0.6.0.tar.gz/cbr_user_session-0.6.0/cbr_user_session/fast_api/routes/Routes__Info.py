from cbr_user_session.user_session.User_Session__Utils import User_Session__Utils
from cbr_user_session.utils.Version                    import version__cbr_user_session
from osbot_fast_api.api.Fast_API_Routes                import Fast_API_Routes


class Routes__Info(Fast_API_Routes):
    tag : str = 'info'

    def db_session(self):
        user_session_utils = User_Session__Utils()
        with user_session_utils.db_sessions() as _:
            return dict(bucket_exists = _.bucket_exists      (),
                        bucket_name   = _.s3_bucket          (),
                        local_stack   = _.using_local_stack  (),
                        session_count = len(_.db_sessions_ids())
                        )

    def ping(self):
        return {"pong" : '42' }

    def version(self):
        return {"version" : version__cbr_user_session }

    def setup_routes(self):
        self.add_route_get(self.db_session)
        self.add_route_get(self.ping      )
        self.add_route_get(self.version   )
        return self