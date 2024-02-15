import os
import sys
from abc import ABC, abstractmethod
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from sqlalchemy import select, and_, or_, not_, desc, func

from custom_vizualization import vizualization
from custom_logger import my_logger
from custom_faker import CustomFaker
from tab_models import Students, Groups, Professors, Subjects, Raiting
from connect_db import session


MODELS = {"Students": Students, "Groups": Groups, "Professors": Professors, "Subjects": Subjects, "Raiting": Raiting}


class CliSceleton(ABC):
    @abstractmethod
    def __init__(self, model: str, id_s: int = None, name: str = None):
        pass

    @abstractmethod
    def command_run(self):
        pass

class CreateNewEntry(CliSceleton):
    def __init__(self, model: str, id_s: int = None, name: str = None):
        self.model = model
        self.id_s = id_s
        self.name = name 
        self.command_run()

    def command_run(self):

        my_logger.log("create_func", 10)
        my_logger.log(self.model)
        my_logger.log(self.id_s)
        my_logger.log(self.name)

class ShowAllEntries(CliSceleton):
    def __init__(self, model: str, id_s: int = None, name: str = None):
        self.model = model
        self.id_s = id_s
        self.name = name 
        self.command_run()
    
    def command_run(self):
        
        query = session.execute(select(Students)).scalars()
        print(query)
        return query
                
        print(r)
        my_logger.log("show_func", 10)
        my_logger.log(self.id_s)
        my_logger.log(self.name)

class UpdateExistEntry(CliSceleton):
    def __init__(self, model: str, id_s: int = None, name: str = None):
        self.model = model
        self.id_s = id_s
        self.name = name 
        self.command_run()

    def command_run(self):
        my_logger.log("update_func", 10)
        my_logger.log(self.model)
        my_logger.log(self.id_s)
        my_logger.log(self.name)

class DeleteExistEntry(CliSceleton):
    def __init__(self, model: str, id_s: int = None, name: str = None):
        self.model = model
        self.id_s = id_s
        self.name = name 
        self.command_run()

    def command_run(self):
        my_logger.log("remove_func", 10)
        my_logger.log(self.model)
        my_logger.log(self.id_s)
        my_logger.log(self.name)

class CliCommands:
    def __init__(self):
        self._full_list_command = {}
        self.command_list()


    def command_registration(self, action: str, command_type: CliSceleton):
        self._full_list_command[action] = command_type

    def command_execute(self, action: str, model: str, id_s: int = None, name:str = None):
        if action in self._full_list_command:
            return self._full_list_command[action](model, id_s, name)

        raise ValueError(
            f"Unkown command please add this command '{action}' to my commnad list!")

    def command_list(self):
        self.command_registration("create", CreateNewEntry)
        self.command_registration("list", ShowAllEntries)
        self.command_registration("update", UpdateExistEntry)
        self.command_registration("remove", DeleteExistEntry)


