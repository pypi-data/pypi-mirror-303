from cbr_shared.cbr_sites.CBR_Site__Shared_Objects  import cbr_site_shared_objects
from osbot_utils.base_classes.Type_Safe             import Type_Safe
from osbot_utils.decorators.methods.cache_on_self   import cache_on_self


class User_Session__Utils(Type_Safe):


    @cache_on_self
    def db_sessions(self):
        return cbr_site_shared_objects.db_sessions()

    def session(self, session_id):
        db_session    = self.db_sessions().db_session(session_id)
        db_session.s3 = self.db_sessions().s3                         # FIX to performance issue with session resolution
        return db_session                                           # todo: figure out a better way to make this fix scale

    def session_exists(self, session_id):
        return self.session(session_id).exists()