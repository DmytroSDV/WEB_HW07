from sqlalchemy import Integer, String, ForeignKey, create_engine, select, and_, or_, not_, desc, func
from sqlalchemy.orm import sessionmaker, relationship, declarative_base, Mapped, mapped_column

from tab_models import Students, Groups, Professors, Subjects, Raiting
from connect_db import session


if __name__ == '__main__':
    pass
