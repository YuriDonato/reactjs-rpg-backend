# backend/app/aplicacao/casos_de_uso/atualizar_jogador.py
from app.dominio.repositorios.jogador_repo import JogadorRepositorio
from app.dominio.entidades.jogador import Jogador

class AtualizarJogadorCasoUso:
    def __init__(self, repositorio: JogadorRepositorio):
        self.repositorio = repositorio

    def executar(self, jogador: Jogador) -> Jogador:
        return self.repositorio.atualizar_jogador(jogador)
