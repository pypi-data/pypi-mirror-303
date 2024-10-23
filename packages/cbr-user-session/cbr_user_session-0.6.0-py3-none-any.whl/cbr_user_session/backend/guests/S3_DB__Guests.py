from osbot_utils.utils.Status                       import status_ok, status_error
from cbr_shared.cbr_backend.cbr.S3_DB__CBR          import S3_DB__CBR
from cbr_user_session.backend.guests.S3_DB__Guest   import S3_DB__Guest

class S3_DB__Guests(S3_DB__CBR):

    def db_guest(self, guest_id=None):
        return S3_DB__Guest(guest_id=guest_id)

    def db_guest__create(self, guest_name:str=None):
        db_guest = S3_DB__Guest()
        db_guest.create(guest_name=guest_name)
        return db_guest.guest_config()

    def db_guests(self):
        for session_id in self.db_guests__ids():
            yield self.db_guest(session_id)

    def db_guests__data(self):
        all_data = {}
        for db_guest in self.db_guests():
            all_data[db_guest.guest_id] = db_guest.guest_config().json()
        return all_data

    def db_guests__delete_all(self):
        deleted_guests = []
        for db_guest in self.db_guests():
            db_guest.delete()
            deleted_guests.append(db_guest.guest_id)
        return deleted_guests

    def db_guests__ids(self):
        return self.s3_folder_list(folder=self.s3_folder_guests())


