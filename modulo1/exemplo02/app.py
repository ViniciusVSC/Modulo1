# Importa a classe Flask do módulo flask
from flask import Flask, render_template

# Cria uma nova instância da aplicação Flask
# "template_folder='templates'"" especifica o diretório onde os arquivos de template da aplicação estão localizados.
app = Flask(__name__, template_folder='templates')

# rota da página inicial chamada "/"
@app.route('/')
def index():
    # renderiza o template "index.html" a partir do arquivo localizado na pasta "templates"
    return render_template("index.html")

# A mesma coisa mas com a rota para pagina pedidos chamada "/orders"
@app.route('/orders')
def orders():
    # renderiza o template "orders.html" a partir do arquivo localizado na pasta "templates"
    return render_template("orders.html")

# inicia a aplicação flask
if __name__ == "__main__":
    app.run()
