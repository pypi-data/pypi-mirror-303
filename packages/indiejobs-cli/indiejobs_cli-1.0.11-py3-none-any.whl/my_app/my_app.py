import argparse
import os
from ._version import __version__


def do_generate(project_name: str):
    # Use the current working directory and append the project name
    project_path = os.path.join(os.getcwd(), project_name)

    # Create the main project folder
    if not os.path.exists(project_path):
        os.makedirs(project_path)
        print(f"Project '{project_name}' created at {project_path}.")

        # Create subfolders (tasks and utils) inside the project folder
        os.makedirs(os.path.join(project_path, "tasks"))
        os.makedirs(os.path.join(project_path, "utils"))
        print("Subfolders 'tasks' and 'utils' created.")

        with open(os.path.join(project_path, "utils", "consts.py"), "w") as f:
            f.write(f"# Constants used in {project_name}")
            f.close()
        print("utils/consts.py created.")

        with open(os.path.join(project_path, "utils", "helpers.py"), "w") as f:
            f.write(f"# Helpers used in {project_name}")
            f.close()
        print("utils/helpers.py created.")

        # Create the main.py file with the specified content
        main_py_content = """import logging

from ssm.parameter_store import ParameterStoreClient
from ssm.errors.parameter_store_errors import ParameterStoreError

if __name__ == "__main__":

    # Configure logging to output to console
    logging.basicConfig(
        level=logging.INFO,  # Set the minimum log level
        format="%(asctime)s - %(levelname)s - %(message)s",  # Customize the log message format
        handlers=[logging.StreamHandler()],  # Log messages to the console
    )

    ps = ParameterStoreClient("eu-west-1")

    parameters = [
        "/codebuild/PROD-indie-autojobs/dbname",
        "/codebuild/PROD-indie-autojobs/host_main",
        "/codebuild/PROD-indie-autojobs/host_replica",
        "/codebuild/PROD-indie-autojobs/password_ro",
        "/codebuild/PROD-indie-autojobs/password_rw",
        "/PROD-indie-autojobs/user_ro",
        "/PROD-indie-autojobs/user_rw",
        "/PROD-indie-autojobs/dbport",
    ]

    try:
        values = ps.get_parameters(parameters, with_decryption=True)
    except ParameterStoreError as e:
        logging.error(repr(e))

    dbname = values["/codebuild/PROD-indie-autojobs/dbname"]
    user_ro = values["/PROD-indie-autojobs/user_ro"]
    password_ro = values["/codebuild/PROD-indie-autojobs/password_ro"]
    user_rw = values["/PROD-indie-autojobs/user_rw"]
    password_rw = values["/codebuild/PROD-indie-autojobs/password_rw"]
    host_main = values["/codebuild/PROD-indie-autojobs/host_main"]
    host_replica = values["/codebuild/PROD-indie-autojobs/host_replica"]
    dbport = values["/PROD-indie-autojobs/dbport"]

    # db clients
    if host_replica:
        db_ro_params = {
            "dbname": dbname,
            "user": user_ro,
            "password": password_ro,
            "host": host_replica,
            "port": dbport,
        }
    else:
        db_ro_params = {
            "dbname": dbname,
            "user": user_ro,
            "password": password_ro,
            "host": host_main,
            "port": dbport,
        }

    db_rw_params = {
        "dbname": dbname,
        "user": user_rw,
        "password": password_rw,
        "host": host_main,
        "port": dbport,
    }

    # logic here
"""

        # Write the content to main.py
        with open(os.path.join(project_path, "main.py"), "w") as f:
            f.write(main_py_content)
        print("main.py created.")

        # Create an empty README.md file inside the project folder
        readme_content = f"# {project_name.capitalize()}\n\nThis is the {project_name} project.\n\nGenerated with IndieJobs (https://github.com/FranciscoRSilva/indiejobs-cli)"
        with open(os.path.join(project_path, "README.md"), "w") as f:
            f.write(readme_content)
        print("README.md created.")
    else:
        print(f"Project '{project_name}' already exists. No folders created.")


def handle_args(args):
    if args.command == "generate":
        if args.name:
            return do_generate(args.name)
        name = input("Please provide a project name: ")
        return do_generate(name)


def main(parser=argparse.ArgumentParser(description="IndieJobs - Autojobs CLI Tool")):
    parser.add_argument("command", help="Command to run (Allowed: 'generate')")
    parser.add_argument(
        "-n", "--name", help="Project name for generation", required=False
    )

    args = parser.parse_args()
    return handle_args(args)
