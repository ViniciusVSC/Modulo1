# Importa a classe Flask do módulo flask
from flask import Flask, render_template

# Criação da instância do Flask, especificando o diretório onde se encontra os templates na pasta templates
app = Flask(__name__, template_folder='templates')

# Rota para a página inicial
@app.route('/')
def index():
    # Renderiza o template index.html
    return render_template("index.html")

# Rota para a página de pedidos
@app.route('/orders')
def orders():
    # Lista de pedidos
    pedidos = ["Combo 1, comanda 2","Executivo 2, comanda 3",
                "Refri laranja, comanda 134","Cerveja, comanda 12",
                "Batata Frita, comanda 14"]
    # Renderiza o template orders.html, passando a lista de pedidos que colocamos como parâmetro
    # usando orders=pedidos
    return render_template("orders.html", orders=pedidos)

# Executa a aplicação Flask
if __name__ == "__main__":
    app.run()
