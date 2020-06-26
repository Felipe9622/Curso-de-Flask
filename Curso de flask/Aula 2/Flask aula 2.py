from flask import Flask

app = Flask (__name__)

@app.route("/")
def index():
    return "index"

def teste():
    return "<h1><p>Bem Vindo a aula 2 de flask</p></h1>"

def nova():
    return"<h2>nova rota criada</h2>"

app.add_url_rule('/teste','teste', teste)
app.add_url_rule('/nova','nova',nova)





if __name__ == '__main__':
    app.run(debug=True, port="3000")