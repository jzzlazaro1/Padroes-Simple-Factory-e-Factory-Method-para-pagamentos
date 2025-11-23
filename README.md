#Padrões-Simple-Factory-e-Factory-Method-para-pagamentos

#💳 Sistema de Pagamento Abstrato

Uma demonstração concisa da aplicação do módulo ABC e do decorador @abstractmethod do Python para criar uma arquitetura de pagamento flexível e extensível.

#🌟 Sobre o Projeto

Este projeto é um exemplo didático que utiliza Classes Abstratas para definir um contrato padrão para diferentes formas de pagamento. O objetivo é garantir que qualquer nova forma de pagamento (Cartão, Boleto, Pix, etc.) implemente o método obrigatório processarPagamento, seguindo o princípio Open/Closed (aberto para extensão, fechado para modificação).

#💡 Conceitos Demonstrados

O código ilustra o uso de:
ABC (Abstract Base Class): A classe base Pagamento que não pode ser instanciada diretamente.
@abstractmethod: Garante que a classe Pagamento force suas subclasses a implementar o método processarPagamento().
Polimorfismo: As subclasses (PagamentoCartao, PagamentoBoleto, PagamentoPix) fornecem suas próprias implementações do método processarPagamento, mas todas compartilham a mesma assinatura da classe pai.

#⚙️ Tecnologias Utilizadas

Linguagem: Python
Módulos: abc (para Abstraction)

#💻 Estrutura do Código

abstract_method.py
O arquivo principal que contém a lógica do sistema de pagamento:
