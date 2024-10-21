from typing import List, Optional, NamedTuple

def processa_dados(valores: List[int], fator: Optional[int] = None) -> float:
    """
    Processa uma lista de inteiros e retorna um valor float.
    
    Parâmetros:
    valores (List[int]): Uma lista de números inteiros.
    fator (Optional[int]): Um fator opcional para multiplicar a soma dos valores.
    
    Retorno:
    float: O resultado do processamento.
    """
    soma = sum(valores)
    if fator:
        soma *= fator
    return float(soma)

class Pessoa(NamedTuple):
    nome: str
    sobrenome: str
    idade: int

def retorna_pessoa() -> Pessoa:
    """
    Retorna um objeto NamedTuple contendo as informações de uma pessoa: nome, sobrenome e idade.

    Retorno:
    Pessoa: Um objeto com os atributos 'nome', 'sobrenome' e 'idade'.
    """
    return Pessoa(nome="João", sobrenome="Silva", idade=30)

