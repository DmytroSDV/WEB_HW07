import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from cli_comands import CliCommands

import argparse

parser = argparse.ArgumentParser(description="CRUD_db_helper")
parser.add_argument("--action", "-a", choices=["create", "list", "update", "remove"],
                    help="type/choose the operation (create/list/update/remove)", required=True)
parser.add_argument("--model", "-m", choices=["Students", "Groups", "Professors", "Subjects", "Raiting"],
                    help="type/choose model (Students/Groups/Professors/Subjects/Raiting)", required=True)
parser.add_argument("-i", "--id", type=int, help="ID of the record", default=None)
parser.add_argument("-n", "--name", help="Name of the record", default=None)

args = vars(parser.parse_args())
action = args.get("action")
model = args.get("model")
id_s = args.get("id")
name = args.get("name")



if __name__ == "__main__":
    cli_handler = CliCommands()

    cli_handler.command_execute(action, model, id_s, name)
