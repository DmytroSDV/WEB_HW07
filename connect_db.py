from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///myWebDb.db", echo=False)
DBSession = sessionmaker(bind=engine)
session = DBSession()
