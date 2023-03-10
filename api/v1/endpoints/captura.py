import datetime
from typing import List

import requests
from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from core.deps import get_session
from models.captura_models import CapturaModel
from schemas.captura_schema import CapturaSchema, GetCapturaSchema

router = APIRouter()


# Post Captura


# Tem que ter relação com as outras tabelas, não pode ser um requests.
@router.post(
    "/{num_pokemon}",
    response_model=CapturaSchema,
    status_code=status.HTTP_201_CREATED,
)
async def post_captura(
    num_pokemon: int,
    captura: CapturaSchema,
    db: AsyncSession = Depends(get_session),
):
    api_poke = f"https://pokeapi.co/api/v2/pokemon/{num_pokemon}"
    poke_list = requests.get(api_poke)
    result = poke_list.json()

    poke_dict = {
        "nome_pokemon": result["name"],
        "numero_pokemon": num_pokemon,
        "peso": result["weight"],
        "experiencia": result["base_experience"],
    }

    nova_captura = CapturaModel(
        nome_treinador=captura.nome_treinador,
        nome_pokemon=poke_dict["nome_pokemon"],
        numero_pokemon=num_pokemon,
        apelido_pokemon=captura.apelido_pokemon,
        peso=poke_dict["peso"],
        experiencia=poke_dict["experiencia"],
        status=captura.status,
        criado_em=datetime.datetime.now().timestamp(),
    )
    db.add(nova_captura)
    await db.commit()

    return nova_captura


# Get Captura


@router.get(
    "/{captura_id}",
    response_model=GetCapturaSchema,
    status_code=status.HTTP_200_OK,
)
async def get_captura(captura_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(CapturaModel).filter(CapturaModel.id == captura_id)
        resultado = await session.execute(query)
        captura = resultado.scalars().one_or_none()

        if captura:
            return captura
        else:
            raise HTTPException(
                detail="Captura não encontrado.",
                status_code=status.HTTP_404_NOT_FOUND,
            )


# Get Capturas


@router.get("/", response_model=List[GetCapturaSchema])
async def get_capturas(db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(CapturaModel)
        resultado = await session.execute(query)
        capturas: List[CapturaModel] = resultado.scalars().all()

        return capturas


# Delete Capturas
@router.delete("/{captura_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_captura(captura_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(CapturaModel).filter(CapturaModel.id == captura_id)
        resultado = await session.execute(query)
        pokemon_del = resultado.scalars().one_or_none()

        if pokemon_del:
            await session.delete(pokemon_del)
            await session.commit()

            return Response(status_code=status.HTTP_204_NO_CONTENT)

        else:
            raise HTTPException(
                detail="Pokemon não encontrado.",
                status_code=status.HTTP_404_NOT_FOUND,
            )
