from sqlalchemy import select, and_, or_, not_, desc, func
from tab_models import Students, Groups, Professors, Subjects, Raiting

from connect_db import session

# -- Знайти 5 студентів із найбільшим середнім балом з усіх предметів.
if __name__ == '__main__':
    query = session.execute(
        select(Raiting.student_id, Students.fullname,
               func.avg(Raiting.rate).label('avg_rate'))
        .join(Students)
        .group_by(Raiting.student_id)
        .order_by(desc("avg_rate"))
        .limit(5)
    ).mappings().all()

    print(query)
