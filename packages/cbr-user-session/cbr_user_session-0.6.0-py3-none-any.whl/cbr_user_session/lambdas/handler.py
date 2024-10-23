import uvicorn
from mangum                                           import Mangum
from cbr_user_session.fast_api.User_Session__Fast_API import User_Session__Fast_API

user_session_fast_api = User_Session__Fast_API().setup()
app                   = user_session_fast_api.app()
run                   = Mangum(app)

def main():
    uvicorn.run(app, host="0.0.0.0", port=8080)

if __name__ == "__main__":      # pragma: no cover
    main()