""" Module to load the application settings from env variables """
import os
from dotenv import load_dotenv

load_dotenv()


def get_required_env_variable(variable_name):
    """ Tries to load a variable from the environment
        throws and exception if it is not found
    """
    env_value = os.environ.get(variable_name, default=None)
    if env_value is None:
        raise Exception(f"required env variable {variable_name} not found!")
    return env_value


SECRET_KEY = get_required_env_variable("SECRET_KEY")
