import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


from conf_db.connect_db import session
from conf_db.tab_models import Students, Groups, Professors, Subjects, Raiting
from custom_funcs.custom_faker import CustomFaker
from custom_funcs.custom_logger import my_logger

from random import randint, choice
from datetime import datetime

NUMBER_OF_STUDENTS = 50
NUMBER_OF_GROUPS = 3
NUMBER_OF_SUBJECTS = 8
NUMBER_PROFESSORS = 5
NUMBER_RAITING = 20
c_facker = CustomFaker('uk_UA')


def generate_fake_data(number_students, number_groups, number_subjects, number_professors, number_of_raiting) -> list[object]:

    fake_students = []
    fake_groups = []
    fake_subjects = []
    fake_professors = []
    fake_raiting = []

    # Students
    for _ in range(number_students):
        fake_students.append(
            Students(fullname=c_facker.name(), group_id=randint(1, NUMBER_OF_GROUPS)))

    # Groups
    for _ in range(number_groups):
        fake_groups.append(Groups(group_name=c_facker.groups()))

    # Subjects
    for _ in range(number_subjects):
        fake_subjects.append(Subjects(
            subject=c_facker.subjects(), professors_id=randint(1, NUMBER_PROFESSORS)))

    # Professors
    for _ in range(number_professors):
        fake_professors.append(Professors(
            fullname=c_facker.professors(), subject=choice(fake_subjects).subject))

    # Raiting
    for _ in range(number_of_raiting):
        for _ in range(1, NUMBER_OF_STUDENTS + 1):
            rate = randint(21, 100)
            rate_date = datetime(2023, randint(1, 12), randint(10, 20)).date()
            fake_raiting.append(Raiting(student_id=randint(1, NUMBER_OF_STUDENTS), subject_id=randint(
                1, NUMBER_OF_SUBJECTS), rate=rate, date_of=rate_date))

    return (fake_students, fake_groups, fake_subjects, fake_professors, fake_raiting)


if __name__ == '__main__':
    fake_data = generate_fake_data(
        NUMBER_OF_STUDENTS, NUMBER_OF_GROUPS, NUMBER_OF_SUBJECTS, NUMBER_PROFESSORS, NUMBER_RAITING)
    try:
        for elements in fake_data:
            session.add_all(elements)
        session.commit()
    except Exception as ex:
        my_logger.log(f'Unable to insert data to the database!\n{ex}', 40)
        session.rollback()
    finally:
        session.close()
