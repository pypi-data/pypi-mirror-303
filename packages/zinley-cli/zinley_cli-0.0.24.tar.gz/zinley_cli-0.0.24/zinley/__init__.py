__app_name__ = "zinley-cli"
from .version import __version__

(
    SUCCESS,
    DIR_ERROR,
    FILE_ERROR,
    DB_READ_ERROR,
    DB_WRITE_ERROR,
    JSON_ERROR,
    ID_ERROR,
) = range(7)

ERRORS = {
    DIR_ERROR: "config directory error",
    FILE_ERROR: "config file error",
    DB_READ_ERROR: "database read error",
    DB_WRITE_ERROR: "database write error",
    ID_ERROR: "to-do id error",
}

api_key = "96ae909e40534d49a70c5e4bdfe54f62"
endpoint = "https://zinley.openai.azure.com"
deployment_id = "gpt-4o"
max_tokens = 4096
