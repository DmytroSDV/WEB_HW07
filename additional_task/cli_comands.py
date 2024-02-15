import os
import sys
from abc import ABC, abstractmethod
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from sqlalchemy import select, and_, or_, not_, desc, func, update

from custom_funcs.custom_vizualization import vizualization
from custom_funcs.custom_logger import my_logger
from custom_funcs.custom_faker import CustomFaker
from conf_db.tab_models import Students, Groups, Professors, Subjects, Raiting
from conf_db.connect_db import session


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
        
    @vizualization
    def command_run(self):
        
        info = f"-- List of all available data in the {self.model} table!"
        my_logger.log(info)
        
        model_queries = {
        "Students": {
            "query": session.execute(select(Students.id, Students.fullname, Students.group_id)
                                     .select_from(Students)).mappings().all()},
        "Groups": {
            "query": session.execute(select(Groups.id, Groups.group_name)
                                     .select_from(Groups)).mappings().all()},
        "Professors": {
            "query": session.execute(select(Professors.id, Professors.fullname, Professors.subject)
                                     .select_from(Professors)).mappings().all()},
        "Subjects": {
            "query": session.execute(select(Subjects.id, Subjects.subject, Subjects.professors_id)
                                     .select_from(Subjects)).mappings().all()},
        "Raiting": {
            "query": session.execute(select(Raiting.id, Raiting.student_id, Raiting.subject_id, Raiting.rate)
                                     .select_from(Raiting)).mappings().all()}}
        
        return model_queries[self.model]["query"]

class UpdateExistEntry(CliSceleton):
    def __init__(self, model: str, id_s: int = None, name: str = None):
        self.model = model
        self.id_s = id_s
        self.name = name
        self.command_run()

    def command_run(self):
        
        info = f"-- Updating user {self.name} with id {self.id_s} in the {self.model} table!"
        my_logger.log(info)
        if not self.id_s or not isinstance(self.id_s, int) or not self.name:
            return my_logger.log(f"""
            Wrong input data for the update function additionally
            you must enter -i (id of the row) and -n
            (name(str) or rate(int) format)!""")
        
        try:
            self.name = int(self.name) if self.model == "Raiting" else self.name
            model_queries = {
            "Students": {
                "query": update(Students).where(Students.id == self.id_s).values(fullname=self.name)},
            "Groups": {
                "query": update(Groups).where(Groups.id == self.id_s).values(group_name=self.name)},
            "Professors": {
                "query": update(Professors).where(Professors.id == self.id_s).values(fullname=self.name)},
            "Subjects": {
                "query": update(Subjects).where(Subjects.id == self.id_s).values(subject=self.name)},
            "Raiting": {
                "query": update(Raiting).where(Raiting.id == self.id_s).values(rate=self.name)}}

            session.execute(model_queries[self.model]["query"])
            session.commit()
            my_logger.log(f"User {self.name} with id {self.id_s} successfully updated in the {self.model} table!!")
            
        except ValueError as ex:
            my_logger.log(f"""
            Unable to cast your entered data -n '{self.name}`
            to digital, data must be in the numeric format!
            Please try again later!""")
            my_logger.log(ex)
            
        except Exception as ex:
            my_logger.log(f'Unable to update data in the database!\n{ex}', 40)
            session.rollback()
        finally:
            session.close()
                       
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


