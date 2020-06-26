from Tools.scripts.make_ctype import method
from flask import Flask, request

app = Flask(__name__)

@app.route('/',methods=["GET","POST"])
def index():
    print(request,method,request.args)
    return "Finalizado"

if __name__=='__main__':
    app.run(debug=True)