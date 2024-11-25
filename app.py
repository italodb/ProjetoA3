from flask import Flask, render_template, request, redirect, url_for
from clientes import Cliente, ClienteManager

app = Flask(__name__)
cliente_manager = ClienteManager()

@app.route('/')
def index():
    return render_template('index.html', clientes=cliente_manager.listar_clientes())

@app.route('/adicionar', methods=['POST'])
def adicionar_cliente():
    nome = request.form['nome']
    email = request.form['email']
    cliente_manager.adicionar_cliente(nome, email)
    return redirect(url_for('index'))

@app.route('/editar/<int:id>', methods=['POST'])
def editar_cliente(id):
    nome = request.form['nome']
    email = request.form['email']
    cliente_manager.editar_cliente(id, nome, email)
    return redirect(url_for('index'))

@app.route('/excluir/<int:id>')
def excluir_cliente(id):
    cliente_manager.excluir_cliente(id)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)