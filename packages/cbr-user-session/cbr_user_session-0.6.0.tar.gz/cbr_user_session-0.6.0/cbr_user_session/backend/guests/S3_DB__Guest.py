from cbr_shared.schemas.data_models.Model__User__Profile_Data import Model__User__Profile_Data
from cbr_shared.schemas.data_models.Model__User__Config_Data  import Model__User__Config_Data
from osbot_utils.decorators.methods.cache_on_self             import cache_on_self
from cbr_shared.cbr_sites.CBR_Site__Shared_Objects            import cbr_site_shared_objects
from cbr_shared.cbr_backend.cbr.S3_DB__CBR                    import S3_DB__CBR
from osbot_utils.helpers.Random_Guid                          import Random_Guid
from osbot_utils.utils.Http                                   import url_join_safe
from cbr_user_session.schemas.Model__Guest__Config            import Model__Guest__Config

FILE_NAME__GUEST_CONFIG = "guest-config.json"

class S3_DB__Guest(S3_DB__CBR):
    guest_id : Random_Guid

    @cache_on_self
    def db_user(self):
        return self.db_users().db_user(user_id=self.db_user_id())

    def db_user__create(self):
        with self.db_user() as _:
            guest_config          = self.guest_config()
            guest_name            = guest_config.guest_name
            user_id               = guest_config.user_id
            first_name, last_name = self.util__split__guest_name_into_first_and_last_names(guest_name)
            user_config           = Model__User__Config_Data (user_id=user_id      , user_name=guest_name)
            user_profile          = Model__User__Profile_Data(first_name=first_name, last_name=last_name )
            _.create(user_config=user_config, user_profile=user_profile)
            return _

    def db_user__data(self):
        return self.db_user().user_data()

    def db_user_id(self):
        guest_config = self.guest_config()
        if guest_config:
            return guest_config.user_id

    @cache_on_self
    def db_users(self):
        return cbr_site_shared_objects.db_users()

    @cache_on_self
    def db_session(self):
        return self.db_sessions().db_session(self.db_session__id())

    def db_session__create(self):
        session_data = dict(user_type = 'guest'      ,
                            sub       = self.db_user_id()        )
        with self.db_session() as _:
            _.create(data=session_data)
            return _

    def db_session__data(self):
        return self.db_session().session_data()

    def db_session__id(self):
        guest_config = self.guest_config()
        if guest_config:
            return guest_config.session_id

    def db_sessions(self):
        return cbr_site_shared_objects.db_sessions()

    def create(self, guest_name:str=None):
        self.guest_config__create(guest_name)
        self.db_user__create     ()
        self.db_session__create  ()
        return self.exists()


    def delete(self):
        if self.exists():
            self.db_user   ().delete()                                              # delete user
            self.db_session().delete()                                              # delete session data
            self.delete__guest_s3_files()                                           # delete created s3 files for this guest

            return self.s3_folder__guest_data__files() == []                        # confirm that there were no files left in the folder
        return False

    def delete__guest_s3_files(self):
        s3_key_user_files = [self.s3_key__guest__config()]                          # mapping of db_guest files to delete
        self.s3_files_delete(s3_key_user_files)                                     # delete those files

    def exists(self):
        return self.s3_file_exists(self.s3_key__guest__config())

    @cache_on_self                                                                  # we can cache this data since the data doesn't change
    def guest_config(self) -> Model__Guest__Config:
        s3_key_guest_config = self.s3_key__guest__config()
        if self.s3_file_exists(s3_key_guest_config):
            guest_config_json = self.s3_file_contents_json(s3_key_guest_config)
            guest_config = Model__Guest__Config(**guest_config_json)
            return guest_config
        return None

    def guest_config__create(self, guest_name=None):
        guest_config = Model__Guest__Config(guest_name=guest_name, guest_id=self.guest_id)
        self.s3_save_data(data=guest_config.json(), s3_key=self.s3_key__guest__config())
        return guest_config

    # s3 key generation

    def s3_folder__guest_data(self):
        return url_join_safe(self.s3_folder_guests(), self.guest_id)

    def s3_folder__guest_data__files(self):
        return self.s3_folder_files(self.s3_folder__guest_data())

    def s3_key__guest__config(self):
        return self.s3_key__in__guest_folder(FILE_NAME__GUEST_CONFIG)

    def s3_key__in__guest_folder(self, file_name):
        return url_join_safe(self.s3_folder__guest_data(), file_name)

    def util__split__guest_name_into_first_and_last_names(self, guest_name: str):  # Split a guest name into first and last names, returning them as a tuple
        first_name = ''                                                            # Initialize first_name as an empty string
        last_name  = ''                                                            # Initialize last_name as an empty string
        if guest_name:                                                             # Proceed only if guest_name is not None or empty
            guest_name = guest_name.strip('_ ').replace('_', ' ')                  # Strip leading/trailing underscores and spaces, then replace remaining underscores with spaces
            parts = guest_name.split()                                             # Split the cleaned name into words based on spaces
            if parts:                                                              # Check if the parts list is not empty
                first_name = parts[0]                                              # Assign the first part as first_name
                last_name = ' '.join(parts[1:])                                    # Combine the remaining parts into last_name, separated by spaces
        return first_name, last_name                                               # Return the first_name and last_name as a tuple

