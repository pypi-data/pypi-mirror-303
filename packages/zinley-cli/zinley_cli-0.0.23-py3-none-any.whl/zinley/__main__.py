"""RP To-Do entry point script."""
# zinley/__main__.py

from zinley import cli, __app_name__

import getpass


# def authenticate():
#     username = input("Username: ")
#     password = getpass.getpass("Password: ")
#     # Validate credentials against stored values (e.g., in a database)
#     if username == "admin" and password == "admin":
#         return True
#     else:
#         return False


def main():
    cli.app(prog_name=__app_name__)


if __name__ == "__main__":
    main()
