#!/usr/bin/env python3
"""
Exemplo de uso do pacote mathutils.

Este arquivo demonstra como usar as principais funções do pacote.

Autor: Aluno Diogo Da Silva Rego, 20240045381
"""

from mathutils import fibonacci, factorial, fibonacci_sequence


def main():
    """Função principal com exemplos de uso."""
    print("=== Demonstração do Pacote MathUtils ===\n")
    
    # Exemplos de Fibonacci
    print("1. Sequência de Fibonacci:")
    print("-" * 30)
    
    # Calculando números individuais
    for i in range(11):
        fib_num = fibonacci(i)
        print(f"fibonacci({i}) = {fib_num}")
    
    print(f"\nNúmeros maiores:")
    print(f"fibonacci(20) = {fibonacci(20)}")
    print(f"fibonacci(30) = {fibonacci(30)}")
    
    # Gerando sequência
    print(f"\nSequência dos primeiros 15 números:")
    seq = fibonacci_sequence(15)
    print(seq)
    
    # Exemplos de Fatorial
    print("\n\n2. Cálculo de Fatorial:")
    print("-" * 30)
    
    for i in range(11):
        fact_num = factorial(i)
        print(f"factorial({i}) = {fact_num}")
    
    print(f"\nNúmeros maiores:")
    print(f"factorial(15) = {factorial(15)}")
    print(f"factorial(20) = {factorial(20)}")
    
    # Comparação de métodos
    print("\n\n3. Comparação de Métodos:")
    print("-" * 30)
    
    n = 25
    fib_iter = fibonacci(n, method="iterative")
    fib_rec = fibonacci(n, method="recursive")
    
    print(f"fibonacci({n}) iterativo: {fib_iter}")
    print(f"fibonacci({n}) recursivo: {fib_rec}")
    print(f"Resultados iguais: {fib_iter == fib_rec}")
    
    fact_iter = factorial(10, method="iterative")
    fact_rec = factorial(10, method="recursive")
    
    print(f"factorial(10) iterativo: {fact_iter}")
    print(f"factorial(10) recursivo: {fact_rec}")
    print(f"Resultados iguais: {fact_iter == fact_rec}")


if __name__ == "__main__":
    main()

