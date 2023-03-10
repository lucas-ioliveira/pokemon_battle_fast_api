from sqlalchemy import Boolean, Column, Float, Integer, String
from sqlalchemy.orm.attributes import InstrumentedAttribute

from core.configs import settings


class BatalhaModel(settings.DBBaseModel):
    __tablename__ = "batalhas"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome_treinador_vencedor: InstrumentedAttribute = Column(String(100))
    nome_pokemon_vencedor: InstrumentedAttribute = Column(String(100))
    nome_treinador_perdedor: InstrumentedAttribute = Column(String(100))
    nome_pokemon_perdedor: InstrumentedAttribute = Column(String(100))
    tipo_da_batalha: InstrumentedAttribute = Column(String(100))
    experiencia_pokemon_vencedor: InstrumentedAttribute = Column(Integer)
    experiencia_pokemon_perdedor: InstrumentedAttribute = Column(Integer)
    data_batalha: InstrumentedAttribute = Column(Float)
