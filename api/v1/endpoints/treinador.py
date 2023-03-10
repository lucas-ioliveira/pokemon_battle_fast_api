import datetime
from typing import List

from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from core.deps import get_session
from models.treinador_models import TreinadorModel
from schemas.treinador_schema import SoftDeleteSchema, TreinadorSchema

router = APIRouter()


# Post treinador


@router.post("/", response_model=TreinadorSchema, status_code=status.HTTP_201_CREATED)
async def post_trainer(
    trainer: TreinadorSchema, db: AsyncSession = Depends(get_session)
):
    novo_trainer = TreinadorModel(
        nome=trainer.nome,
        idade=trainer.idade,
        genero=trainer.genero,
        status=trainer.status,
        criado_em=datetime.datetime.now().timestamp(),
    )
    db.add(novo_trainer)
    await db.commit()

    return novo_trainer


# Get treinadores


@router.get("/", response_model=List[TreinadorSchema])
async def get_treinadores(db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(TreinadorModel)
        resultado = await session.execute(query)
        treinadores: List[TreinadorModel] = resultado.scalars().all()

        return treinadores


# Get treinador
@router.get(
    "/{treinador_id}",
    response_model=TreinadorSchema,
    status_code=status.HTTP_200_OK,
)
async def get_treinador(treinador_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(TreinadorModel).filter(TreinadorModel.id == treinador_id)
        resultado = await session.execute(query)
        treinador = resultado.scalars().one_or_none()

        if treinador:
            return treinador
        else:
            raise HTTPException(
                detail="Treinador não encontrado.",
                status_code=status.HTTP_404_NOT_FOUND,
            )


# Put treinador
@router.put(
    "/{treinador_id}",
    response_model=TreinadorSchema,
    status_code=status.HTTP_202_ACCEPTED,
)
async def put_treinador(
    treinador_id: int,
    treinador: TreinadorSchema,
    db: AsyncSession = Depends(get_session),
):
    async with db as session:
        query = select(TreinadorModel).filter(TreinadorModel.id == treinador_id)
        resultado = await session.execute(query)
        treinador_up = resultado.scalars().one_or_none()

        if treinador_up:
            treinador_up.nome = treinador.nome
            treinador_up.idade = treinador.idade
            treinador_up.genero = treinador.genero
            treinador_up.status = treinador.status

            await session.commit()

            return treinador

        else:
            raise HTTPException(
                detail="Treinador não encontrado.",
                status_code=status.HTTP_404_NOT_FOUND,
            )


# Soft delete treinador
@router.put(
    "/{id_treinador}",
    response_model=SoftDeleteSchema,
    status_code=status.HTTP_202_ACCEPTED,
)
async def put_soft_delete_treinador(
    id_treinador: int,
    treinador: SoftDeleteSchema,
    db: AsyncSession = Depends(get_session),
):
    async with db as session:
        query = select(TreinadorModel).filter(TreinadorModel.id == id_treinador)
        resultado = await session.execute(query)
        treinador_up = resultado.scalars().one_or_none()

        if treinador_up:
            treinador_up.status = treinador.status

            await session.commit()

            return treinador_up

        else:
            raise HTTPException(
                detail="Treinador não encontrado.",
                status_code=status.HTTP_404_NOT_FOUND,
            )


# Delete treinador
@router.delete("/{treinador_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_treinador(treinador_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(TreinadorModel).filter(TreinadorModel.id == treinador_id)
        resultado = await session.execute(query)
        treinador_del = resultado.scalars().one_or_none()

        if treinador_del:
            await session.delete(treinador_del)
            await session.commit()

            return Response(status_code=status.HTTP_204_NO_CONTENT)

        else:
            raise HTTPException(
                detail="Treinador não encontrado.",
                status_code=status.HTTP_404_NOT_FOUND,
            )
