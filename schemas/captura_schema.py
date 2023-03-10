from pydantic import BaseModel as SCBaseModel


class CapturaSchema(SCBaseModel):
    nome_treinador: str
    apelido_pokemon: str
    status: bool

    class Config:
        orm_mode = True


class GetCapturaSchema(CapturaSchema):
    id: int
    nome_pokemon: str
    numero_pokemon: int
    peso: int
    experiencia: int
    criado_em: int
