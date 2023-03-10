import datetime
from typing import List

from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from core.deps import get_session
from models.batalha_models import BatalhaModel
from models.captura_models import CapturaModel
from schemas.batalha_schema import GetBatalhaSchema, BatalhaSchema
from schemas.captura_schema import CapturaSchema

router = APIRouter()


# Post batalha


@router.post(
    "/",
    response_model=GetBatalhaSchema,
    status_code=status.HTTP_201_CREATED,
)
async def post_batalha(
    batalha: BatalhaSchema,
    db: AsyncSession = Depends(get_session),
):
    pass

    # async with db as session:
    #     query1 = select(CapturaModel).filter(CapturaModel.id == nome)
    #     query2 = select(CapturaModel).filter(CapturaModel.id == nome_treinador2)
    #     result = await session.execute(query1)
    #     result2 = await session.execute(query2)
    #     batalha1 = result.scalars().one_or_none()
    #     batalha2 = result2.scalars().one_or_none()
    #
    #     if batalha1["experiencia"] > batalha2["expriencia"]:
    #         trainer_winner = nome_treinador1
    #
    #     nova_batalha = BatalhaModel(
    #         nome_treinador_vencedor=nome_treinador1,
    #         nome_pokemon_vencedor
    #     )


# Get batalha


@router.get(
    "/{batalha_id}",
    response_model=GetBatalhaSchema,
    status_code=status.HTTP_200_OK,
)
async def get_batalha(batalha_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(BatalhaModel).filter(BatalhaModel.id == batalha_id)
        resultado = await session.execute(query)
        batalha = resultado.scalars().one_or_none()

        if batalha:
            return batalha
        else:
            raise HTTPException(
                detail="Batalha não encontrado.",
                status_code=status.HTTP_404_NOT_FOUND,
            )


# Get Batalhas


@router.get("/", response_model=List[GetBatalhaSchema])
async def get_batalhas(db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(BatalhaModel)
        resultado = await session.execute(query)
        batalhas: List[BatalhaModel] = resultado.scalars().all()

        return batalhas
