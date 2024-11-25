import pytest
from clientes import ClienteManager

def test_adicionar_cliente():
    manager = ClienteManager()
    manager.adicionar_cliente("João", "joao@example.com")
    assert len(manager.listar_clientes()) == 1
    assert manager.listar_clientes()[0].nome == "João"

def test_editar_cliente():
    manager = ClienteManager()
    manager.adicionar_cliente("Maria", "maria@example.com")
    manager.editar_cliente(1, "Maria Silva", "maria.silva@example.com")
    assert manager.listar_clientes()[0].nome == "Maria Silva"

def test_excluir_cliente():
    manager = ClienteManager()
    manager.adicionar_cliente("Carlos", "carlos@example.com")
    manager.excluir_cliente(1)
    assert len(manager.listar_clientes()) == 0