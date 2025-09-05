_


# MathUtils - Pacote Python para Funções Matemáticas

`mathutils` é um pacote Python leve e eficiente que fornece implementações otimizadas de funções matemáticas comuns, como a sequência de Fibonacci e o cálculo de fatorial. O pacote foi projetado para ser simples, bem documentado e fácil de usar, ideal para fins educacionais e projetos que necessitam de funções matemáticas básicas.

<<<<<<< HEAD
**Autor:** Aluno Diogo Da Silva Rego, 20240045381

=======
>>>>>>> 20dd68dce2b236aa81af074211ca7475f3866560
---




## Instalação

Para instalar o pacote, utilize o `pip`:

```bash
pip install mathutils-pacote
```




## Como Usar

### Sequência de Fibonacci

Calcular o n-ésimo número da sequência:

```python
from mathutils import fibonacci

# Calcula o 10º número de Fibonacci (método iterativo)
resultado = fibonacci(10)
print(f"O 10º número de Fibonacci é: {resultado}")  # Saída: 55

# Usando o método recursivo (otimizado com cache)
resultado_recursivo = fibonacci(10, method="recursive")
print(f"Resultado com método recursivo: {resultado_recursivo}")  # Saída: 55
```

Gerar uma sequência de Fibonacci:

```python
from mathutils import fibonacci_sequence

# Gera os 10 primeiros números da sequência
sequencia = fibonacci_sequence(10)
print(f"Sequência de Fibonacci: {sequencia}")
# Saída: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```

### Cálculo de Fatorial

Calcular o fatorial de um número:

```python
from mathutils import factorial

# Calcula o fatorial de 5 (método iterativo)
resultado = factorial(5)
print(f"O fatorial de 5 é: {resultado}")  # Saída: 120

# Usando o método recursivo
resultado_recursivo = factorial(5, method="recursive")
print(f"Resultado com método recursivo: {resultado_recursivo}")  # Saída: 120
```




## Funcionalidades

- **Fibonacci**: Cálculo do n-ésimo número e geração de sequências.
  - Suporta métodos iterativo e recursivo (com cache para otimização).
- **Fatorial**: Cálculo do fatorial de um número.
  - Suporta métodos iterativo e recursivo.
- **Utilitários**: Funções para verificar se um número pertence à sequência de Fibonacci e para gerar sequências até um limite.
- **Documentação Completa**: Docstrings detalhadas e type hints em todas as funções.
- **Testes Abrangentes**: Cobertura de testes de 100% com `pytest`.




## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma *issue* ou enviar um *pull request*.

## Licença

Este projeto é licenciado sob a Licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.


