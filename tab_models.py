from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import relationship, declarative_base, Mapped, mapped_column
from sqlalchemy.sql.sqltypes import DateTime
from datetime import datetime

Base = declarative_base()


class Students(Base):
    __tablename__ = "students"
    id: Mapped[int] = mapped_column(primary_key=True)
    fullname: Mapped[str] = mapped_column(
        String(100), nullable=False, unique=True)
    group_id: Mapped[int] = mapped_column(ForeignKey(
        "groups.id", onupdate="CASCADE", ondelete="CASCADE"), nullable=False)
    group: Mapped['Groups'] = relationship('Groups')


class Groups(Base):
    __tablename__ = "groups"
    id: Mapped[int] = mapped_column(primary_key=True)
    group_name: Mapped[str] = mapped_column(
        String(50), nullable=False, unique=True)


class Professors(Base):
    __tablename__ = "professors"
    id: Mapped[int] = mapped_column(primary_key=True)
    fullname: Mapped[str] = mapped_column(
        String(100), nullable=False, unique=True)
    subject: Mapped[str] = mapped_column(String(50), nullable=False)
    subjects: Mapped['Subjects'] = relationship(
        "Subjects", cascade="all, delete-orphan")


class Subjects(Base):
    __tablename__ = "subjects"
    id: Mapped[int] = mapped_column(primary_key=True)
    subject: Mapped[str] = mapped_column(
        String(50), unique=True, nullable=False)
    professors_id: Mapped[int] = mapped_column(ForeignKey(
        "professors.id", ondelete="CASCADE", onupdate="CASCADE"), nullable=False)
    professor: Mapped['Professors'] = relationship(
        "Professors", back_populates='subjects')
    raitings: Mapped['Raiting'] = relationship(
        "Raiting", cascade="all, delete-orphan")


class Raiting(Base):
    __tablename__ = "raiting"
    id: Mapped[int] = mapped_column(primary_key=True)
    student_id: Mapped[int] = mapped_column(ForeignKey(
        'students.id', ondelete="CASCADE", onupdate="CASCADE"), nullable=False)
    student: Mapped['Students'] = relationship("Students")
    subject_id: Mapped[int] = mapped_column(ForeignKey(
        'subjects.id', ondelete="CASCADE", onupdate="CASCADE"), nullable=False)
    subject: Mapped['Subjects'] = relationship(
        "Subjects", cascade="all, delete", overlaps="raitings") 
    rate: Mapped[int] = mapped_column(nullable=False)
    date_of: Mapped[DateTime] = mapped_column(
        DateTime, default=datetime.now(), nullable=False)
