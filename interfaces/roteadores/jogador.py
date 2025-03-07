from fastapi import APIRouter, HTTPException
from aplicacao.dto.jogador_dto import JogadorDTO
from dominio.entidades.jogador import Jogador
from infra.repositorios_impl.jogador_repo_impl import JogadorRepositorioFirebase

router = APIRouter()
repositorio_jogador = JogadorRepositorioFirebase()

@router.get("/", response_model=JogadorDTO)
def obter_jogador(id: str = "1"):
    try:
        jogador = repositorio_jogador.obter_jogador(id)
        return jogador
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.post("/", response_model=JogadorDTO)
def criar_jogador(jogador: JogadorDTO):
    try:
        novo_jogador = Jogador(**jogador.dict())
        criado = repositorio_jogador.criar_jogador(novo_jogador)
        return criado
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.put("/", response_model=JogadorDTO)
def atualizar_jogador(jogador: JogadorDTO):
    try:
        jogador_atualizado = Jogador(**jogador.dict())
        atualizado = repositorio_jogador.atualizar_jogador(jogador_atualizado)
        return atualizado
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
