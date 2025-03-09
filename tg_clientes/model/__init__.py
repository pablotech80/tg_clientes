from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

DeclarativeBase = declarative_base()
DBSession = scoped_session(sessionmaker())

def init_model(engine):
    """Inicia la base de datos con el engine dado."""
    DBSession.configure(bind=engine)
