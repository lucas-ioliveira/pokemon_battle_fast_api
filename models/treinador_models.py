import datetime

from sqlalchemy import Boolean, Column, Float, Integer, String
from sqlalchemy.orm.attributes import InstrumentedAttribute

from core.configs import settings


class TreinadorModel(settings.DBBaseModel):
    __tablename__ = "treinadores"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome: InstrumentedAttribute = Column(String(100))
    idade: InstrumentedAttribute = Column(Integer)
    genero: InstrumentedAttribute = Column(String(100))
    status: InstrumentedAttribute = Column(Boolean)
    criado_em: InstrumentedAttribute = Column(Float)
