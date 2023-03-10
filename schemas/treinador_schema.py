from pydantic import BaseModel as SCBaseModel


class TreinadorSchema(SCBaseModel):
    nome: str
    idade: int
    genero: str
    status: bool
    criado_em: float

    class Config:
        orm_mode = True


class SoftDeleteSchema(SCBaseModel):
    status: bool

    class Config:
        orm_mode = True
