from pydantic import BaseModel as SCBaseModel


class PokemonSchema(SCBaseModel):
    apelido: str
    status: bool

    class Config:
        orm_mode = True


class GetPokemonSchema(PokemonSchema):
    id: int
    nome: str
    numero_pokemon: int
    peso: int
    experiencia: int
    criado_em: int
