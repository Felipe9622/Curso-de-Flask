
from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates')


@app.route('/')
def index():
    query = request.args.to_dict()
    return render_template("modelo.html", query=query)


if __name__ == '__main__':
    app.run()