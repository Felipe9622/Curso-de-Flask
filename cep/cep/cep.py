from flask import Flask, render_template, request
import pyttsx3


voz = pyttsx3.init()
app = Flask(__name__, template_folder='templates')



@app.route("/")
def index():
    return render_template("index.html")

@app.route("/teste")
def get():
    return render_template("endereço.html")

@app.route("/endereço")
def post():
    return render_template("resultado.html")

@app.route("/recebe/", methods=['GET','POST'])
def recebe():
    if request.method == "GET":
        return """Nome:{} <br> 
        CEP:{} <br> 
        Rua:{} <br> 
        Bairro:{} <br> 
        Cidade:{} <br> 
        Estado:{} <br>
        IBGE:{} <br>""".format(request.args.get("nome"),request.args.get("cep"),request.args.get("rua"),request.args.get("bairro"),request.args.get("cidade"),request.args.get("uf"),request.args.get("ibge"))
    elif request.method =="POST":
        return "teste"
        voz.setProperty('rate', 155)
        voz.setProperty('volume', 2)
        voz.say("busca ,foi realizada, com sucesso")


app.run()
voz.runAndWait()