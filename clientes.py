class Cliente:
    def __init__(self, id, nome, email):
        self.id = id
        self.nome = nome
        self.email = email

class ClienteManager:
    def __init__(self):
        self.clientes = []
        self.proximo_id = 1

    def adicionar_cliente(self, nome, email):
        cliente = Cliente(self.proximo_id, nome, email)
        self.clientes.append(cliente)
        self.proximo_id += 1

    def listar_clientes(self):
        return self.clientes

    def editar_cliente(self, id, nome, email):
        for cliente in self.clientes:
            if cliente.id == id:
                cliente.nome = nome
                cliente.email = email
                break

    def excluir_cliente(self, id):
        self.clientes = [cliente for cliente in self.clientes if cliente.id != id]