# Importa a classe Flask do módulo flask
from flask import Flask

# Cria uma instância Flask com o nome de Modulo_00
app = Flask("Modulo_00")

# Cria uma rota para a página inicial com endereço "/",
# define uma função que retorna um código HTML 
# o html precisa estar dento das aspas triplas pos assim
# permite que uma string seja definida em várias linhas, mantendo sua formatação original
@app.route('/')
def index():
    return """<html>
                <head>
                    <title>Meu Restaurante</title>
                </head>
                <body>
                    <h2>Meu Restaurante</h2>
                    <h3>Acesse o menu:</h3>
                    <ul>
                        <li><a href="/orders">Listar Pedidos</a></li>
                        <li><a href="clientes">Listar Clientes</a></li>
                        <li><a href="funcionario">Listar Funcionários</a></li>
                    </ul>
                    <p>Lembre-se de verificar corretamente os pedidos!</p>
                    <p>Caso algum produto esteja inconsistente. Solicitar a alteração!</p>
                    <p>Não realizamos a troca dos pedidos após a confecção!</p>
                </body>
            </html>
            """

# a mesma coisa que o de cima,
# a diferença é que cria uma rota para a página de listagem de pedidos com endereço "/orders"
@app.route('/orders')
def orders():
    return """
                <html>
                    <head>
                        <title>Meu Restaurante</title>
                    </head>
                    <body>
                        <h1>Pedidos</h1>
                        <ul>
                            <li>Combo 1, comanda 2.</li>
                            <li>Combo 2, comanda 5.</li>
                            <li>Executivo 2, comanda 3</li>
                            <li>Refri laranja, comanda 134</li>
                            <li>Cerveja, comanda 12</li>
                            <li>Batata Frita, comanda 14</li>
                        </ul>
                        <p>Voltar para <a href="/">página inicial</a>!</p>
                    </body>
                </html>
            """

# Mesmo processodo, cria uma rota para a página de listagem de clientes com endereço "/clientes"
@app.route("/clientes")
def clientes():
    return """
                <html>
                    <head>
                        <title>clientes</title>
                    </head>
                    <body>
                       <h1>so isso mesmo<h1>
                    </body>
                </html>
            """

# E por fim cria uma rota para a página de listagem de funcionários (endereço /funcionario)
@app.route("/funcionario")
def funcionario():
    return  """
                <html>
                    <head>
                        <title>funcionarios</title>
                    </head>
                    <body>
                       <h1>Só pra n deixar vazio<h1>
                    </body>
                </html>
            """

# Executa a aplicação se este arquivo for executado diretamente
if __name__ == "__main__":
    app.run()
