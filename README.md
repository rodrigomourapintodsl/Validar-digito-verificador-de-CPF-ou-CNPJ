# Validador de CPF e CNPJ (Alfanumérico) em Python
[![NumPy](https://img.shields.io/badge/NumPy-4DABCF?logo=numpy&logoColor=fff)](https://numpy.org/)
[![PyPI Python Version](https://img.shields.io/pypi/pyversions/numpy)](https://www.python.org/downloads/)


Este repositório contém um script eficiente em Python para validação de Cadastro de Pessoas Físicas (CPF) e Cadastro Nacional da Pessoa Jurídica (CNPJ). 

O diferencial deste código é a utilização da biblioteca `numpy` para cálculos vetorizados e otimizados dos dígitos verificadores, além de **suporte nativo ao novo formato de CNPJ alfanumérico** implementado pela Receita Federal.

## 🚀 Funcionalidades

- **Validação de CPF:** Verifica o formato e calcula os dígitos verificadores com base no algoritmo oficial.
- **Validação de CNPJ Alfanumérico:** Suporte atualizado para validar tanto o formato numérico tradicional quanto o novo modelo que inclui letras (ex: `12.ABC.345/01DE-35`).
- **Otimização de Performance:** Uso de arrays e operações do `numpy` para o cálculo rápido dos pesos e somatórios (ideal para integração em pipelines de dados ou rotinas de ETL).
- **Tratamento de Exceções Comuns:** Identifica e rejeita CPFs/CNPJs com todos os números iguais (ex: `111.111.111-11`), que possuem cálculos matematicamente válidos mas são blocos inválidos na Receita Federal.
- **Filtro Regex Integrado:** Remove automaticamente pontuações (`.`, `-`, `/`) e formatações indesejadas antes da validação.

## 📋 Pré-requisitos

Para rodar este script, você precisará do Python instalado em sua máquina e da biblioteca NumPy.

```bash
pip install numpy
```

## 💻 Como Usar
Você pode importar as funções diretamente para o seu projeto. Veja o exemplo abaixo:
```python
from validador import validar_cpf, validar_cnpj
cpf_teste = "123.456.789-09"
if validar_cpf(cpf_teste):
    print("CPF Válido!")

cnpjs_para_testar = [
    "12.ABC.345/01DE-35", # Novo formato com pontuação
    "12ABC34501DE35",     # Novo formato sem pontuação
    "12345678000195"      # Formato tradicional numérico
]
for cnpj in cnpjs_para_testar:
    status = "Válido" if validar_cnpj(cnpj) else "Inválido"
    print(f"O CNPJ {cnpj} é {status}.")
```

## 📝 Criando Rotinas de testes
[![Pytest](https://img.shields.io/badge/Pytest-fff?logo=pytest&logoColor=000)](https://docs.pytest.org/en/stable/getting-started.html)

Você pode criar rotinas que testam casos garantindo a integridade
```Python
import pytest
from validador import validar_cpf, validar_cnpj

# --- Testes de CPF ---
@pytest.mark.parametrize("cpf, resultado_esperado", [
    ("111.111.111-11", False), # Caso raro de números repetidos
    ("123", False),            # Tamanho incorreto
    ("ABC.456.789-09", False), # Caracteres inválidos
    # Adicione aqui um CPF que você sabe que é matematicamente válido para testar o True
])
def test_validar_cpf(cpf, resultado_esperado):
    assert validar_cpf(cpf) == resultado_esperado


# --- Testes de CNPJ ---
@pytest.mark.parametrize("cnpj, resultado_esperado", [
    ("12.ABC.345/01DE-35", True),  # Formato Alfanumérico (válido conforme seu script)
    ("12ABC34501DE35", True),      # Alfanumérico sem pontuação
    ("12345678000195", False),     # Exemplo de numérico (substitua por um válido real se quiser testar True)
    ("11.111.111/1111-11", False), # Números repetidos
    ("CNPJ_ERRADO", False)         # Formato totalmente incorreto
])
def test_validar_cnpj(cnpj, resultado_esperado):
    assert validar_cnpj(cnpj) == resultado_esperado
```
