from sqlalchemy import Boolean, Column, Float, Integer, String
from sqlalchemy.orm.attributes import InstrumentedAttribute

from core.configs import settings


class PokemonModel(settings.DBBaseModel):
    __tablename__ = "pokemons"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome: InstrumentedAttribute = Column(String(100))
    numero_pokemon: InstrumentedAttribute = Column(Integer)
    apelido: InstrumentedAttribute = Column(String(100))
    peso: InstrumentedAttribute = Column(Integer)
    experiencia: InstrumentedAttribute = Column(Integer)
    status: InstrumentedAttribute = Column(Boolean)
    criado_em: InstrumentedAttribute = Column(Float)
