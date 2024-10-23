from flask                                                      import g
from cbr_shared.cbr_backend.users.DB_Users                      import DB_Users
from cbr_shared.config.Server_Config__CBR_Website               import server_config__cbr_website
from cbr_shared.schemas.data_models.Model__User__Profile_Data   import Model__User__Profile_Data

EXPECTED_ROUTES__LLMS = []
INTRO_TO_USER_DATA     = "We have asked the user to provide some information and included below is the data provided, please customise the answers as much as possible to these user preferences:\n"

# todo: refactor this into a separate file and class
def user_data_for_prompt():
    user_profile = current_user_data()                         # todo: needs fixing to reflect new Model__User__Profile_Data
    if not user_profile:
        return ""

    lines_of_data = [INTRO_TO_USER_DATA]


    for key,value in user_profile.json().items():               # Format the data into a readable list, aligned in columns
        if value:
            line = f"{key:<{30 + 2}}: {value}"
            lines_of_data.append(line)

    user_data = "\n".join(lines_of_data)                        # Join the lines into a single string with newline separation
    return user_data


# todo: this code needs refactoring, specially the bucket creation code below
def current_user_data() -> Model__User__Profile_Data:
    if server_config__cbr_website.login_disabled():
        return None
    db_users = DB_Users()
    db_users.setup()                        # create bucket if needed
    user_data = g.user_data
    user_id = user_data.get('sub')          # use the 'sub' field from Cognito (which is a GUID) to set the user_id
    if user_id:
        db_user = db_users.db_user(user_id)
        if db_user.exists() is False:
            print(f"Creating user: {user_id}")
            db_user.create()
        return db_user.user_profile()
    return None





