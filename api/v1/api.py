from fastapi import APIRouter
from api.v1.endpoints import batalha, captura, pokemon, treinador

api_router = APIRouter()
api_router.include_router(treinador.router, prefix="/treinadores", tags=["Treinadores"])
api_router.include_router(pokemon.router, prefix="/pokemons", tags=["Pokemons"])
api_router.include_router(
    captura.router, prefix="/capturas", tags=["Capturas_pokemons"]
)
api_router.include_router(batalha.router, prefix="/batalhas", tags=["Batalhas"])
