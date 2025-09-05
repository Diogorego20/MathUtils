"""
Módulo com funções matemáticas básicas.

Este módulo contém implementações eficientes de funções matemáticas
comumente utilizadas, incluindo sequência de Fibonacci e cálculo de fatorial.
"""

from typing import List, Union
import functools


def fibonacci(n: int, method: str = "iterative") -> int:
    """
    Calcula o n-ésimo número da sequência de Fibonacci.
    
    A sequência de Fibonacci é definida como:
    F(0) = 0, F(1) = 1, F(n) = F(n-1) + F(n-2) para n > 1
    
    Args:
        n (int): Posição na sequência (deve ser >= 0)
        method (str): Método de cálculo ("iterative" ou "recursive")
        
    Returns:
        int: O n-ésimo número de Fibonacci
        
    Raises:
        ValueError: Se n for negativo
        ValueError: Se method não for "iterative" ou "recursive"
        
    Examples:
        >>> fibonacci(0)
        0
        >>> fibonacci(1)
        1
        >>> fibonacci(10)
        55
        >>> fibonacci(10, method="recursive")
        55
    """
    if n < 0:
        raise ValueError("n deve ser um número não-negativo")
    
    if method not in ["iterative", "recursive"]:
        raise ValueError("method deve ser 'iterative' ou 'recursive'")
    
    if method == "recursive":
        return _fibonacci_recursive(n)
    else:
        return _fibonacci_iterative(n)


def _fibonacci_iterative(n: int) -> int:
    """Implementação iterativa do cálculo de Fibonacci."""
    if n <= 1:
        return n
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    
    return b


@functools.lru_cache(maxsize=None)
def _fibonacci_recursive(n: int) -> int:
    """Implementação recursiva otimizada com memoização."""
    if n <= 1:
        return n
    return _fibonacci_recursive(n - 1) + _fibonacci_recursive(n - 2)


def fibonacci_sequence(length: int, method: str = "iterative") -> List[int]:
    """
    Gera uma sequência de números de Fibonacci.
    
    Args:
        length (int): Comprimento da sequência (deve ser >= 0)
        method (str): Método de cálculo ("iterative" ou "recursive")
        
    Returns:
        List[int]: Lista com os primeiros 'length' números de Fibonacci
        
    Raises:
        ValueError: Se length for negativo
        
    Examples:
        >>> fibonacci_sequence(5)
        [0, 1, 1, 2, 3]
        >>> fibonacci_sequence(10)
        [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    """
    if length < 0:
        raise ValueError("length deve ser um número não-negativo")
    
    if length == 0:
        return []
    
    return [fibonacci(i, method) for i in range(length)]


def factorial(n: int, method: str = "iterative") -> int:
    """
    Calcula o fatorial de um número.
    
    O fatorial de n (n!) é definido como:
    n! = n × (n-1) × (n-2) × ... × 2 × 1
    Por convenção, 0! = 1
    
    Args:
        n (int): Número para calcular o fatorial (deve ser >= 0)
        method (str): Método de cálculo ("iterative" ou "recursive")
        
    Returns:
        int: O fatorial de n
        
    Raises:
        ValueError: Se n for negativo
        ValueError: Se method não for "iterative" ou "recursive"
        
    Examples:
        >>> factorial(0)
        1
        >>> factorial(5)
        120
        >>> factorial(10)
        3628800
        >>> factorial(5, method="recursive")
        120
    """
    if n < 0:
        raise ValueError("n deve ser um número não-negativo")
    
    if method not in ["iterative", "recursive"]:
        raise ValueError("method deve ser 'iterative' ou 'recursive'")
    
    if method == "recursive":
        return _factorial_recursive(n)
    else:
        return _factorial_iterative(n)


def _factorial_iterative(n: int) -> int:
    """Implementação iterativa do cálculo de fatorial."""
    if n <= 1:
        return 1
    
    result = 1
    for i in range(2, n + 1):
        result *= i
    
    return result


def _factorial_recursive(n: int) -> int:
    """Implementação recursiva do cálculo de fatorial."""
    if n <= 1:
        return 1
    return n * _factorial_recursive(n - 1)


# Funções utilitárias adicionais
def is_fibonacci_number(num: int) -> bool:
    """
    Verifica se um número pertence à sequência de Fibonacci.
    
    Args:
        num (int): Número a ser verificado
        
    Returns:
        bool: True se o número for um número de Fibonacci, False caso contrário
        
    Examples:
        >>> is_fibonacci_number(13)
        True
        >>> is_fibonacci_number(14)
        False
    """
    if num < 0:
        return False
    
    # Gera números de Fibonacci até encontrar o número ou ultrapassá-lo
    a, b = 0, 1
    while a < num:
        a, b = b, a + b
    
    return a == num


def fibonacci_up_to(limit: int) -> List[int]:
    """
    Gera números de Fibonacci até um limite específico.
    
    Args:
        limit (int): Valor limite (inclusive)
        
    Returns:
        List[int]: Lista de números de Fibonacci até o limite
        
    Examples:
        >>> fibonacci_up_to(20)
        [0, 1, 1, 2, 3, 5, 8, 13]
        >>> fibonacci_up_to(100)
        [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    """
    if limit < 0:
        return []
    
    sequence = []
    a, b = 0, 1
    
    while a <= limit:
        sequence.append(a)
        a, b = b, a + b
    
    return sequence

