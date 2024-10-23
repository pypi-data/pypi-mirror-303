from osbot_fast_api.api.Fast_API_Routes             import Fast_API_Routes
from osbot_utils.decorators.methods.cache_on_self   import cache_on_self
from cbr_user_session.User_Session__Shared_Objects  import user_session__shared_objects

class Routes__Guests(Fast_API_Routes):
    tag : str = 'guests'

    @cache_on_self
    def db_guests(self):
        return user_session__shared_objects.db_guests()

    def data(self):
        return self.db_guests().db_guests__data()

    def ids(self):
        return self.db_guests().db_guests__ids()

    def setup_routes(self):
        self.add_route_get(self.data)
        self.add_route_get(self.ids)
        return self