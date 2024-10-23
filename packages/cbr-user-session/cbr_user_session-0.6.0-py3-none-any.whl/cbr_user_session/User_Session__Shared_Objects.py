from osbot_utils.decorators.methods.cache_on_self   import cache_on_self
from cbr_user_session.backend.guests.S3_DB__Guests  import S3_DB__Guests
from osbot_utils.base_classes.Type_Safe             import Type_Safe

class User_Session__Shared_Objects(Type_Safe):

    @cache_on_self
    def db_guests(self) -> S3_DB__Guests:
        with S3_DB__Guests() as _:
            _.setup()
            return _

user_session__shared_objects = User_Session__Shared_Objects()