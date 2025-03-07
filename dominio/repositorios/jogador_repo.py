# backend/app/dominio/repositorios/jogador_repo.py
from abc import ABC, abstractmethod
from app.dominio.entidades.jogador import Jogador

class JogadorRepositorio(ABC):
    @abstractmethod
    def obter_jogador(self, id: int) -> Jogador:
        pass

    @abstractmethod
    def atualizar_jogador(self, jogador: Jogador) -> Jogador:
        pass

    @abstractmethod
    def criar_jogador(self, jogador: Jogador) -> Jogador:
        pass
