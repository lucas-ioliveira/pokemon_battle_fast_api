import datetime
from typing import List

import requests
from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from core.deps import get_session
from models.pokemon_models import PokemonModel
from schemas.pokemon_schema import GetPokemonSchema, PokemonSchema

router = APIRouter()


# Post pokemon


@router.post(
    "/{pokemon_number}",
    response_model=PokemonSchema,
    status_code=status.HTTP_201_CREATED,
)
async def post_pokemon(
    pokemon_number: int,
    pokemon: PokemonSchema,
    db: AsyncSession = Depends(get_session),
):
    api_pokemon = f"https://pokeapi.co/api/v2/pokemon/{pokemon_number}"
    poke_lista = requests.get(api_pokemon)
    result = poke_lista.json()

    pokemons_lista = {
        "nome_pokemon": result["name"],
        "numero_pokemon": pokemon_number,
        "peso": result["weight"],
        "experiencia": result["base_experience"],
    }

    novo_pokemon = PokemonModel(
        nome=pokemons_lista["nome_pokemon"],
        numero_pokemon=pokemon_number,
        apelido=pokemon.apelido,
        peso=pokemons_lista["peso"],
        experiencia=pokemons_lista["experiencia"],
        status=pokemon.status,
        criado_em=datetime.datetime.now().timestamp(),
    )
    db.add(novo_pokemon)
    await db.commit()

    return novo_pokemon


# Get pokemon


@router.get(
    "/{pokemon_id}",
    response_model=GetPokemonSchema,
    status_code=status.HTTP_200_OK,
)
async def get_pokemon(pokemon_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(PokemonModel).filter(PokemonModel.id == pokemon_id)
        resultado = await session.execute(query)
        pokemon = resultado.scalars().one_or_none()

        if pokemon:
            return pokemon
        else:
            raise HTTPException(
                detail="Pokemon não encontrado.",
                status_code=status.HTTP_404_NOT_FOUND,
            )


# Get Pokemons


@router.get("/", response_model=List[GetPokemonSchema])
async def get_pokemons(db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(PokemonModel)
        resultado = await session.execute(query)
        pokemons: List[PokemonModel] = resultado.scalars().all()

        return pokemons


# Delete pokemon
@router.delete("/{pokemon_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_pokemon(pokemon_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(PokemonModel).filter(PokemonModel.id == pokemon_id)
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
