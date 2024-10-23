from dataclasses                        import dataclass
from osbot_utils.utils.Str              import safe_str
from osbot_utils.helpers.Random_Guid    import Random_Guid
from osbot_utils.utils.Misc             import random_text, timestamp_to_str_date, timestamp_to_str_time
from osbot_utils.base_classes.Type_Safe import Type_Safe
from osbot_utils.helpers.Timestamp_Now  import Timestamp_Now

@dataclass
class Model__Guest__Config(Type_Safe):
    created__date   : str               = None
    created__time   : str               = None
    timestamp       : Timestamp_Now     = None
    guest_name      : str               = None
    guest_id        : Random_Guid       = None
    session_id      : Random_Guid       = None
    user_id         : Random_Guid       = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if self.guest_id      is None: self.guest_id      = Random_Guid           ()
        if self.session_id    is None: self.session_id    = Random_Guid           ()
        if self.user_id       is None: self.user_id       = Random_Guid           ()
        if self.timestamp     is None: self.timestamp     = Timestamp_Now         ()
        if self.guest_name    is None: self.guest_name    = random_text           ('guest', lowercase=True, length=5)
        if self.created__date is None: self.created__date = timestamp_to_str_date (self.timestamp                         )
        if self.created__time is None: self.created__time = timestamp_to_str_time (self.timestamp                         )


        self.guest_name = safe_str(self.guest_name)  # todo: create Safe_Str class (similar to Random_Guid)




