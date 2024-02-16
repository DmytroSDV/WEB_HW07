import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from sqlalchemy import select, and_, desc, func, update
from conf_db.tab_models import Students, Groups, Professors, Subjects, Raiting

from conf_db.connect_db import session
from custom_funcs.custom_vizualization import vizualization
from custom_funcs.custom_logger import my_logger
from custom_funcs.custom_faker import CustomFaker

fake = CustomFaker("uk_UA")


@vizualization
def select_01():

    info = """
 1-- Знайти 5 студентів із найбільшим середнім балом з усіх предметів."""
    my_logger.log(info)

    query = session.execute(
        select(Raiting.student_id, Students.fullname,
               func.round(func.avg(Raiting.rate), 2).label('avg_rate'))
        .join(Students)
        .group_by(Raiting.student_id, Students.fullname)
        .order_by(desc("avg_rate"))
        .limit(5)
    ).mappings().all()
    return query


@vizualization
def select_02():

    info = """
2-- Знайти студента із найвищим середнім балом з певного предмета."""
    my_logger.log(info)

    query = session.execute(
        select(Raiting.subject_id, Students.fullname, Subjects.subject,
               func.round(func.avg(Raiting.rate), 2).label("avg_rate"))
        .join(Students)
        .join(Subjects)
        .where(Raiting.subject_id == 2)
        .group_by(Raiting.student_id, Raiting.subject_id, Students.fullname, Subjects.subject)
        .order_by(desc("avg_rate"))
        .limit(1)
    ).mappings().all()
    return query


@vizualization
def select_03():

    info = """
3-- Знайти середній бал у групах з певного предмета."""
    my_logger.log(info)

    query = session.execute(
        select(Groups.id, Groups.group_name, Subjects.subject,
               func.round(func.avg(Raiting.rate), 2).label("avg_rate"))
        .select_from(Raiting)
        .join(Students)
        .join(Groups)
        .join(Subjects)
        .where(Subjects.id == 2)
        .group_by(Groups.id, Subjects.subject)
    ).mappings().all()
    return query


@vizualization
def select_04():

    info = """
4-- Знайти середній бал на потоці (по всій таблиці оцінок)."""
    my_logger.log(info)

    query = session.execute(select(func.round(func.avg(Raiting.rate), 2).label("avg_rate"),
                                   func.count(Raiting.rate).label("rate_quatiny"))
                            .select_from(Raiting)).mappings().all()
    return query


@vizualization
def select_05():

    info = """
5-- Знайти які курси читає певний викладач."""
    my_logger.log(info)

    query = session.execute(select(Subjects.subject, Professors.fullname)
                            .select_from(Subjects)
                            .join(Professors)
                            .where(Professors.id == 2)
                            ).mappings().all()
    return query


@vizualization
def select_06():

    info = """
6-- Знайти список студентів у певній групі."""
    my_logger.log(info)

    query = session.execute(select(Students.fullname, Groups.group_name)
                            .select_from(Students)
                            .join(Groups)
                            .where(Groups.id == 2)
                            ).mappings().all()

    return query


@vizualization
def select_07():

    info = """
7-- Знайти оцінки студентів у окремій групі з певного предмета."""
    my_logger.log(info)

    query = session.execute(select(Raiting.student_id, Students.fullname, Subjects.subject, Raiting.rate)
                            .select_from(Raiting)
                            .join(Students)
                            .join(Subjects)
                            .join(Groups)
                            .where(and_(Groups.id == 2, Subjects.id == 2))
                            ).mappings().all()
    return query


@vizualization
def select_08():

    info = """
8-- Знайти середній бал, який ставить певний викладач зі своїх предметів."""
    my_logger.log(info)

    query = session.execute(select(Professors.fullname, Subjects.subject,
                            func.round(func.avg(Raiting.rate), 2).label('avg_rate'))
                            .select_from(Raiting)
                            .join(Subjects)
                            .join(Professors)
                            .group_by(Professors.fullname, Subjects.subject)
                            .where(Professors.id == 2)
                            ).mappings().all()

    return query


@vizualization
def select_09():

    info = """
9-- Знайти список курсів, які відвідує студент."""
    my_logger.log(info)

    query = session.execute(select(Students.fullname, Groups.group_name, Subjects.subject)
                            .select_from(Students)
                            .join(Groups)
                            .join(Raiting)
                            .join(Subjects)
                            .where(Students.id == 2)
                            ).mappings().all()

    return query


@vizualization
def select_10():

    info = """
10-- Список курсів, які певному студенту читає певний викладач."""
    my_logger.log(info)

    query = session.execute(
        select(Students.fullname, Subjects.subject, Professors.fullname)
        .select_from(Students)
        .join(Raiting)
        .join(Subjects)
        .join(Professors)
        .where(and_(Students.id == 3, Professors.id == 2))
    ).mappings().all()

    return query


@vizualization
def select_11():

    info = """
11-- Середній бал, який певний викладач ставить певному студентові."""
    my_logger.log(info)

    query = session.execute(select(Students.fullname, Professors.fullname, Subjects.subject,
                            func.round(func.avg(Raiting.rate), 2).label("avg_rate"))
                            .select_from(Raiting)
                            .join(Students)
                            .join(Subjects)
                            .join(Professors)
                            .group_by(Students.fullname, Professors.fullname,Subjects.subject)
                            .where(and_(Professors.id == 2, Students.id == 2))
                            ).mappings().all()

    return query


@vizualization
def select_12():

    info = """
12-- Оцінки студентів у певній групі з певного предмета на останньому занятті."""
    my_logger.log(info)

    query = session.execute(select(Students.fullname, Raiting.rate, Raiting.date_of)
                            .select_from(Students)
                            .join(Raiting)
                            .join(Subjects)
                            .join(Groups)
                            .where(and_(Groups.id == 2, Subjects.id == 2))
                            .order_by(desc(Raiting.date_of))
                            .limit(1)
                            ).mappings().all()

    return query

if __name__ == '__main__':
    select_01()
    select_02()
    select_03()
    select_04()
    select_05()
    select_06()
    select_07()
    select_08()
    select_09()
    select_10()
    select_11()
    select_12()
