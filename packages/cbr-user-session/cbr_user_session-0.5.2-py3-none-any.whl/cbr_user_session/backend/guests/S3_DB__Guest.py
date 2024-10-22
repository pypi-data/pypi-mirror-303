from cbr_shared.cbr_backend.cbr.S3_DB__CBR  import S3_DB__CBR
from osbot_utils.helpers.Random_Guid        import Random_Guid


FILE_NAME_CURRENT_SESSION = 'guest-data.json'

class S3_DB__Guest(S3_DB__CBR):
    guest_id : Random_Guid
