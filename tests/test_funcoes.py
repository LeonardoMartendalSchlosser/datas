import sys
import os

# Adiciona o diretório pai ao PYTHONPATH para importar o pacote datas
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from datas.funcoes import (
    adicionar_dias,
    subtrair_dias,
    diferenca_dias,
    eh_final_de_semana,
    eh_dia_util,
    formatar_data,
    data_hoje,
    data_valida
)

def test_adicionar_dias():
    assert adicionar_dias("2025-03-10", 5) == "2025-03-15"
    assert adicionar_dias("2025-12-30", 5) == "2026-01-04"

def test_subtrair_dias():
    assert subtrair_dias("2025-03-10", 10) == "2025-02-28"
    assert subtrair_dias("2025-01-01", 1) == "2024-12-31"

def test_diferenca_dias():
    assert diferenca_dias("2025-03-10", "2025-03-03") == 7
    assert diferenca_dias("2025-01-01", "2025-01-01") == 0

def test_eh_final_de_semana():
    # 2025-03-15 é sábado
    assert eh_final_de_semana("2025-03-15") is True
    # 2025-03-17 é segunda
    assert eh_final_de_semana("2025-03-17") is False

def test_eh_dia_util():
    # segunda-feira
    assert eh_dia_util("2025-03-17") is True
    # sábado
    assert eh_dia_util("2025-03-15") is False

def test_formatar_data():
    assert formatar_data("2025-03-10", "%d/%m/%Y") == "10/03/2025"
    assert formatar_data("2025-12-25", "%d-%m-%Y") == "25-12-2025"

def test_data_valida():
    assert data_valida("2025-02-28") is True
    assert data_valida("2025-02-30") is False
    assert data_valida("texto") is False

def test_data_hoje():
    # Apenas verifica se a função retorna algo no formato esperado
    hoje = data_hoje()
    assert len(hoje) == 10  # exemplo: 2025-03-10
    assert hoje.count("-") == 2
