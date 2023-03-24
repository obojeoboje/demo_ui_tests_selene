from voluptuous import Schema

login_single_user_successful = Schema(
    {
        "token": str
    }
)

login_single_user_unsuccessful = Schema(
    {
        "error": str
    }
)