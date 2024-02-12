from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///myWebDb.db", echo=True)
DBSession = sessionmaker(bind=engine)
session = DBSession()
