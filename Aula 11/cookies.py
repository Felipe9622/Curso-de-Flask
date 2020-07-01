from flask import Flask, render_template, request, make_response

app = Flask(__name__, template_folder='template aula 11')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/setcoockie')
def setcoockie():
    resp = make_response(render_template('setcookie.html'))
    if request.method == 'POST':
        dados = request.form['c']
        resp.set_cookie('testeCookie')
    return resp


@app.route('/getcoockie')
def getcoockie():
    coockiename = request.cookies.get('testeCookie')
    return '<h1>Valor coockie é: {}</h1'.format(coockiename)


if __name__ == '__main__':
    app.run(debug=True)
