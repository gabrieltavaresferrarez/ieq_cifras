
from dynaconf import Dynaconf, Validator

settings = Dynaconf(
    envvar_prefix="IEQCIFRAS",
    settings_files=['settings.toml', '.secrets.toml'],
    environments=["development", "production", "teste"],
    env_switcher='IEQCIFRAS_ENV',
    validators = [
        Validator("FLASK_RUN_PORT", must_exist=True),
        Validator("DEBUG", must_exist=True),
        Validator("SECRET_KEY", must_exist=True),
        Validator("SQLALCHEMY_DATABASE_URI", must_exist=True),
    ],
)

# this is the list of attributes in dynaconf object that are not set in config file and enviroment variables
list_keysToIgnore = ['RENAMED_VARS', 'SETTINGS_MODULE', 'PROJECT_ROOT', 'GET_CONFIG']
settings.get_config = \
    lambda : [key for key in list(settings.keys()) \
              if not 'DYNACONF' in key and key not in list_keysToIgnore]

# `envvar_prefix` = export envvars with `export DYNACONF_FOO=bar`.
# `settings_files` = Load these files in the order.
