from datetime import datetime
import faker
from random import randint, choice
import sqlite3
from faker_data import CustomFaker

NUMBER_OF_STUDENTS = 50
NUMBER_OF_GROUPS = 3
NUMBER_OF_SUBJECTS = 8
NUMBER_PROFESSORS = 5
NUMBER_RAITING = 20


def generate_fake_data(number_students, number_groups, number_subjects, number_professors) -> tuple():
    fake_students = []
    fake_groups = []
    fake_subjects = []
    fake_professors = []

    c_facker = CustomFaker('uk_UA')

    for _ in range(number_students):
        fake_students.append(c_facker.name())

    for _ in range(number_groups):
        fake_groups.append(c_facker.groups())

    for _ in range(number_subjects):
        fake_subjects.append(c_facker.subjects())

    for _ in range(number_professors):
        fake_professors.append(c_facker.professors())

    return fake_students, fake_groups, fake_subjects, fake_professors


def prepare_data(students, groups, subjects, professors) -> tuple():

    for_students = []
    for student in students:
        for_students.append((student, randint(1, NUMBER_OF_GROUPS)))

    for_groups = []
    for group in groups:
        for_groups.append((group, ))

    for_subjects = []
    for subject in subjects:
        for_subjects.append((subject, randint(1, NUMBER_PROFESSORS)))

    for_professors = []
    for professor in professors:
        for_professors.append((professor, choice(subjects)))

    for_raiting = []
    for _ in range(NUMBER_RAITING):
        for _ in range(1, NUMBER_OF_STUDENTS + 1):
            rate = randint(51, 100)
            rate_date = datetime(2023, randint(1, 12), randint(10, 20)).date()
            for_raiting.append(
                (randint(1, NUMBER_OF_STUDENTS), randint(1, NUMBER_OF_SUBJECTS), rate, rate_date))

    return for_students, for_groups, for_subjects, for_professors, for_raiting


def insert_data_to_db(students, groups, subjects, professors, raiting) -> None:

    with sqlite3.connect('register.db') as con:

        cur = con.cursor()

        sql_to_students = """INSERT INTO students(student_name, group_id)
                               VALUES (?,?)"""
        cur.executemany(sql_to_students, students)

        sql_to_groups = """INSERT INTO groups(group_name)
                               VALUES (?)"""
        cur.executemany(sql_to_groups, groups)

        sql_to_professors = """INSERT INTO professors(professor_name, subject_name)
                               VALUES (?,?)"""
        cur.executemany(sql_to_professors, professors)

        sql_to_subjects = """INSERT INTO subjects(subject_name, professors_id)
                               VALUES (?,?)"""
        cur.executemany(sql_to_subjects, subjects)

        sql_to_raiting = """INSERT INTO raiting(student_id, subject_id, rate, date_of)
                              VALUES (?, ?, ?, ?)"""
        cur.executemany(sql_to_raiting, raiting)

        con.commit()


if __name__ == "__main__":
    students, groups, subjects, professors, raiting = prepare_data(
        *generate_fake_data(NUMBER_OF_STUDENTS, NUMBER_OF_GROUPS, NUMBER_OF_SUBJECTS, NUMBER_PROFESSORS))
    insert_data_to_db(students, groups, subjects, professors, raiting)
