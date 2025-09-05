"""
Testes unitários para o módulo math_functions.

Este módulo contém testes abrangentes para todas as funções
matemáticas implementadas no pacote mathutils.
"""

import pytest
import sys
import os

# Adiciona o diretório pai ao path para importar o módulo
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from mathutils.math_functions import (
    fibonacci,
    fibonacci_sequence,
    factorial,
    is_fibonacci_number,
    fibonacci_up_to
)


class TestFibonacci:
    """Testes para a função fibonacci."""
    
    def test_fibonacci_base_cases(self):
        """Testa casos base da sequência de Fibonacci."""
        assert fibonacci(0) == 0
        assert fibonacci(1) == 1
        
    def test_fibonacci_iterative(self):
        """Testa implementação iterativa de Fibonacci."""
        expected_values = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
        for i, expected in enumerate(expected_values):
            assert fibonacci(i, method="iterative") == expected
            
    def test_fibonacci_recursive(self):
        """Testa implementação recursiva de Fibonacci."""
        expected_values = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
        for i, expected in enumerate(expected_values):
            assert fibonacci(i, method="recursive") == expected
            
    def test_fibonacci_large_numbers(self):
        """Testa Fibonacci com números maiores."""
        assert fibonacci(20) == 6765
        assert fibonacci(30) == 832040
        
    def test_fibonacci_negative_input(self):
        """Testa comportamento com entrada negativa."""
        with pytest.raises(ValueError, match="n deve ser um número não-negativo"):
            fibonacci(-1)
            
    def test_fibonacci_invalid_method(self):
        """Testa comportamento com método inválido."""
        with pytest.raises(ValueError, match="method deve ser 'iterative' ou 'recursive'"):
            fibonacci(5, method="invalid")
            
    def test_fibonacci_methods_consistency(self):
        """Testa se ambos os métodos retornam o mesmo resultado."""
        for i in range(15):
            iterative_result = fibonacci(i, method="iterative")
            recursive_result = fibonacci(i, method="recursive")
            assert iterative_result == recursive_result


class TestFibonacciSequence:
    """Testes para a função fibonacci_sequence."""
    
    def test_fibonacci_sequence_empty(self):
        """Testa sequência vazia."""
        assert fibonacci_sequence(0) == []
        
    def test_fibonacci_sequence_basic(self):
        """Testa sequências básicas."""
        assert fibonacci_sequence(1) == [0]
        assert fibonacci_sequence(2) == [0, 1]
        assert fibonacci_sequence(5) == [0, 1, 1, 2, 3]
        assert fibonacci_sequence(10) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
        
    def test_fibonacci_sequence_negative_length(self):
        """Testa comportamento com comprimento negativo."""
        with pytest.raises(ValueError, match="length deve ser um número não-negativo"):
            fibonacci_sequence(-1)
            
    def test_fibonacci_sequence_methods(self):
        """Testa ambos os métodos de cálculo."""
        iterative_seq = fibonacci_sequence(8, method="iterative")
        recursive_seq = fibonacci_sequence(8, method="recursive")
        assert iterative_seq == recursive_seq


class TestFactorial:
    """Testes para a função factorial."""
    
    def test_factorial_base_cases(self):
        """Testa casos base do fatorial."""
        assert factorial(0) == 1
        assert factorial(1) == 1
        
    def test_factorial_iterative(self):
        """Testa implementação iterativa do fatorial."""
        expected_values = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
        for i, expected in enumerate(expected_values):
            assert factorial(i, method="iterative") == expected
            
    def test_factorial_recursive(self):
        """Testa implementação recursiva do fatorial."""
        expected_values = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
        for i, expected in enumerate(expected_values):
            assert factorial(i, method="recursive") == expected
            
    def test_factorial_large_numbers(self):
        """Testa fatorial com números maiores."""
        assert factorial(10) == 3628800
        assert factorial(12) == 479001600
        
    def test_factorial_negative_input(self):
        """Testa comportamento com entrada negativa."""
        with pytest.raises(ValueError, match="n deve ser um número não-negativo"):
            factorial(-1)
            
    def test_factorial_invalid_method(self):
        """Testa comportamento com método inválido."""
        with pytest.raises(ValueError, match="method deve ser 'iterative' ou 'recursive'"):
            factorial(5, method="invalid")
            
    def test_factorial_methods_consistency(self):
        """Testa se ambos os métodos retornam o mesmo resultado."""
        for i in range(10):
            iterative_result = factorial(i, method="iterative")
            recursive_result = factorial(i, method="recursive")
            assert iterative_result == recursive_result


class TestIsFibonacciNumber:
    """Testes para a função is_fibonacci_number."""
    
    def test_is_fibonacci_number_true_cases(self):
        """Testa números que são de Fibonacci."""
        fibonacci_numbers = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
        for num in fibonacci_numbers:
            assert is_fibonacci_number(num) is True
            
    def test_is_fibonacci_number_false_cases(self):
        """Testa números que não são de Fibonacci."""
        non_fibonacci_numbers = [4, 6, 7, 9, 10, 11, 12, 14, 15, 16]
        for num in non_fibonacci_numbers:
            assert is_fibonacci_number(num) is False
            
    def test_is_fibonacci_number_negative(self):
        """Testa comportamento com números negativos."""
        assert is_fibonacci_number(-1) is False
        assert is_fibonacci_number(-5) is False


class TestFibonacciUpTo:
    """Testes para a função fibonacci_up_to."""
    
    def test_fibonacci_up_to_basic(self):
        """Testa casos básicos."""
        assert fibonacci_up_to(0) == [0]
        assert fibonacci_up_to(1) == [0, 1, 1]
        assert fibonacci_up_to(10) == [0, 1, 1, 2, 3, 5, 8]
        assert fibonacci_up_to(20) == [0, 1, 1, 2, 3, 5, 8, 13]
        
    def test_fibonacci_up_to_exact_match(self):
        """Testa quando o limite é exatamente um número de Fibonacci."""
        assert fibonacci_up_to(21) == [0, 1, 1, 2, 3, 5, 8, 13, 21]
        assert fibonacci_up_to(55) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
        
    def test_fibonacci_up_to_negative(self):
        """Testa comportamento com limite negativo."""
        assert fibonacci_up_to(-1) == []
        assert fibonacci_up_to(-10) == []


class TestIntegration:
    """Testes de integração entre diferentes funções."""
    
    def test_fibonacci_and_factorial_integration(self):
        """Testa integração entre funções de Fibonacci e fatorial."""
        # Testa se o fatorial dos primeiros números de Fibonacci funciona
        fib_seq = fibonacci_sequence(6)  # [0, 1, 1, 2, 3, 5]
        
        for fib_num in fib_seq:
            fact_result = factorial(fib_num)
            assert isinstance(fact_result, int)
            assert fact_result >= 1
            
    def test_performance_comparison(self):
        """Testa comparação de performance entre métodos."""
        import time
        
        # Testa Fibonacci
        start_time = time.time()
        fibonacci(25, method="iterative")
        iterative_time = time.time() - start_time
        
        start_time = time.time()
        fibonacci(25, method="recursive")
        recursive_time = time.time() - start_time
        
        # Para números pequenos, ambos devem ser rápidos
        assert iterative_time < 1.0
        assert recursive_time < 1.0


if __name__ == "__main__":
    # Executa os testes se o arquivo for executado diretamente
    pytest.main([__file__, "-v"])

