from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

# Definir la sesión de la base de datos
engine = create_engine("postgresql://macbookpro:1234@localhost:5432/polaris_db")
DBSession = scoped_session(sessionmaker(bind=engine))

class Cliente(Base):
    __tablename__ = 'clientes'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String, nullable=False)
    codigo = Column(String, unique=True, nullable=False)
    telefono1 = Column(String)
    direccion = Column(String)
    nif = Column(String)

# Asociar la metadata a la sesión
Base.metadata.bind = engine
