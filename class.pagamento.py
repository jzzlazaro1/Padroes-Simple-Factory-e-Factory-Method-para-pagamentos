from abc import ABC, abstractmethod
from abc import ABC, abstractmethod

class Pagamento(ABC):
    @abstractmethod
    def processarPagamento(self, valor: float) -> str:
        pass
class PagamentoFactory(ABC):
    @abstractmethod
    def criarPagamento(self, tipo_pagamento: str) -> Pagamento:
        pass

print("\033[31mclasse abstrata 'PagamentoFactory' e o seu metodo abstrato 'criarPagamento' está definido.\033")
