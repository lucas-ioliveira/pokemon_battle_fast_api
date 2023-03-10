from sqlalchemy import Boolean, Column, Float, Integer, String
from sqlalchemy.orm.attributes import InstrumentedAttribute

from core.configs import settings


class CapturaModel(settings.DBBaseModel):
    __tablename__ = "captura"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome_treinador: InstrumentedAttribute = Column(String(100))
    nome_pokemon: InstrumentedAttribute = Column(String(100))
    apelido_pokemon: InstrumentedAttribute = Column(String(100))
    numero_pokemon: InstrumentedAttribute = Column(Integer)
    peso: InstrumentedAttribute = Column(Integer)
    experiencia: InstrumentedAttribute = Column(Integer)
    status: InstrumentedAttribute = Column(Boolean)
    criado_em: InstrumentedAttribute = Column(Float)
