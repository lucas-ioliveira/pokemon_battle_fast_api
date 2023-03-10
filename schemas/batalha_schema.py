from pydantic import BaseModel as SCBaseModel


class BatalhaSchema(SCBaseModel):
    nome_treinador1: str
    nome_treinador2: str

    class Config:
        orm_mode = True


class GetBatalhaSchema(SCBaseModel):
    id: int
    nome_treinador_vencedor: int
    nome_pokemon_vencedor: int
    nome_treinador_perdedor: int
    nome_pokemon_perdedor: int
    tipo_da_batalha: str
    experiencia_pokemon_vencedor: int
    experiencia_pokemon_perdedor: int
    data_batalha: float

    class Config:
        orm_mode = True
