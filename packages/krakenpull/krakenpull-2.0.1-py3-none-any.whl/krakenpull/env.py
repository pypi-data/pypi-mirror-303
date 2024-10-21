import os

from krakenpull.utils import get_root_dir


def get_env_variable(var_name: str, default: str | None = None):
    """
    Get the environment variable or return exception
    :param var_name: Environment Variable to lookup
    :param default: Default to return if the variable is not found
    """
    try:
        return os.environ[var_name]
    except KeyError:
        from io import StringIO
        from configparser import ConfigParser

        env_file = get_root_dir() / ".secrets.env"
        try:
            with open(env_file) as f:
                config = StringIO()
                config.write("[DATA]\n")
                config.write(f.read())
                config.seek(0, os.SEEK_SET)
                cp = ConfigParser()
                cp.read_file(config)

            value = dict(cp.items("DATA"))[var_name.lower()]
            if value.startswith('"') and value.endswith('"'):
                value = value[1:-1]
            elif value.startswith("'") and value.endswith("'"):
                value = value[1:-1]

            os.environ.setdefault(var_name, value)
            return value
        except (KeyError, IOError):
            if default:
                return default
            raise ValueError("Can't find env variable")


KRAKEN_API_KEY = get_env_variable("KRAKEN_API_KEY")
KRAKEN_PRIVATE_KEY = get_env_variable("KRAKEN_PRIVATE_KEY")
