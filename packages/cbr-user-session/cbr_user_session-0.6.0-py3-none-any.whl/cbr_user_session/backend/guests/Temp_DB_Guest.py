from cbr_user_session.backend.guests.S3_DB__Guest   import S3_DB__Guest
from osbot_utils.decorators.methods.cache_on_self   import cache_on_self
from cbr_user_session.User_Session__Shared_Objects  import user_session__shared_objects
from osbot_utils.base_classes.Type_Safe             import Type_Safe

class Temp_DB_Guest(Type_Safe):
    guest_name: str = None

    @cache_on_self
    def db_guest(self):
        return self.db_guests().db_guest()

    @cache_on_self
    def db_guests(self):
        return user_session__shared_objects.db_guests()

    def __enter__(self) -> S3_DB__Guest:
        self.create()
        return self.db_guest()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.delete()

    def create(self):
        self.db_guest().create(guest_name=self.guest_name)
        return self.db_guest()

    def delete(self):
        self.db_guest().delete()
        return self