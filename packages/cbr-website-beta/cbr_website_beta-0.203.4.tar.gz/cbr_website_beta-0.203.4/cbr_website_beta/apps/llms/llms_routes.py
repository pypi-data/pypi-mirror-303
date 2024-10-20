import os

from flask                                                      import render_template, g
from cbr_shared.cbr_backend.users.DB_Users                      import DB_Users
from cbr_shared.config.Server_Config__CBR_Website               import server_config__cbr_website
from cbr_website_beta.apps.llms                                 import blueprint
from cbr_website_beta.apps.llms.Prompt_Examples                 import Prompt_Examples
from cbr_website_beta.cbr__flask.decorators.allow_annonymous    import admin_only
from osbot_utils.helpers.Random_Guid import Random_Guid
from osbot_utils.utils.Dev import pprint

EXPECTED_ROUTES__LLMS = []
INTRO_TO_USER_DATA     = "We have asked the user to provide some information and included below is the data provided, please customise the answers as much as possible to these user preferences:\n"

def user_data_for_prompt():
    raw_user_data = current_user_data()
    if raw_user_data == {} or raw_user_data.get('user_id') is None:
        return ""
    vars_to_add = [
        'First name', 'Last name', 'Role', 'Organisation',
        'Sector', 'Size of organisation', 'Country', 'Linkedin',
        'Additional suggested prompts for Athena, your AI advisor' ]

    # Determine the longest variable name for proper alignment
    longest_var = max(len(var) for var in vars_to_add)

    lines_of_data = [INTRO_TO_USER_DATA]

    # Format the data into a readable list, aligned in columns
    for var in vars_to_add:
        value = raw_user_data.get(var)
        if value:
            # Capitalize each word in var_name for better presentation
            var_name_capitalized = ' '.join(word.capitalize() for word in var.split())
            # Align the data with the longest variable name
            line = f"{var_name_capitalized:<{longest_var + 2}}: {value}"
            lines_of_data.append(line)

    # Join the lines into a single string with newline separation
    user_data = "\n".join(lines_of_data)
    return user_data


# todo: this code needs refactoring, specially the bucket creation code below
def current_user_data():
    if server_config__cbr_website.login_disabled():
        return {}
    db_users = DB_Users()
    db_users.setup()                        # create bucket if needed
    user_data = g.user_data
    user_id = user_data.get('sub')          # use the 'sub' field from Cognito (which is a GUID) to set the user_id
    if user_id:
        db_user = db_users.db_user(user_id)
        if db_user.exists() is False:
            print(f"Creating user: {user_id}")
            db_user.create()
        return db_user.metadata()
    return {}





