from cbr_shared.cbr_backend.session.DB_Sessions import DB_Sessions
from osbot_utils.base_classes.Type_Safe         import Type_Safe


class User_Session__Utils(Type_Safe):
    db_sessions: DB_Sessions

    def session(self, session_id):
        return self.db_sessions.db_session(session_id)

    def session_exists(self, session_id):
        return self.session(session_id).exists()