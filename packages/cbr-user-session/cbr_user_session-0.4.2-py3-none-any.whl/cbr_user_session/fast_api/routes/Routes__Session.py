from cbr_user_session.user_session.User_Session__Utils  import User_Session__Utils
from osbot_aws.aws.boto3.View_Boto3_Rest_Calls import print_boto3_calls
from osbot_fast_api.api.Fast_API_Routes                 import Fast_API_Routes
from osbot_utils.helpers.trace.Trace_Call import Trace_Call
from osbot_utils.helpers.trace.Trace_Call__Config import Trace_Call__Config


class Routes__Session(Fast_API_Routes):
    tag                : str                 = 'session'
    user_session_utils : User_Session__Utils

    def session_exists(self, session_id):
        return self.user_session_utils.session_exists(session_id)

    def session_exists__with_trace(self, session_id:str, bigger_than:float=0.020):
        config = dict(trace_capture_start_with  = ['osbot_', 'cbr', 'boto'],
                      show_method_class         = True                     ,
                      show_parent_info          = True                     ,
                      capture_duration          = True                     ,
                      print_duration            = True                     ,
                      print_padding_duration    = 190                      ,
                      with_duration_bigger_than = float(bigger_than)         )
        trace_call_config = Trace_Call__Config(**config)
        with Trace_Call(config=trace_call_config) as trace_call:
            self.session_exists(session_id)
        traces    = trace_call.print_to_str()
        from starlette.responses import PlainTextResponse
        return PlainTextResponse(traces)

    def setup_routes(self):
        self.add_route_get(self.session_exists            )
        self.add_route_get(self.session_exists__with_trace)