from flask import Flask

app = Flask(__name__)


@app.route('/hello')
@app.route("/hello/<nome>")
def hello(nome=""):
    return "<h1> Hello {}</h1>".format(nome)


@app.route('/blog/')
@app.route('/blog/<int:postID>')
def blog(postID=-1):
    if postID >= 0:
        return "<h1>blog info {}</h1>".format(postID)
    else:
        return "<h2>blog todo<h2>"


@app.route('/blog/')
@app.route('/blog/<float:postID>')
def blog2(postID=-1):
    if postID >= 0:
        return "<h1>blog float {}</h1>".format(postID)
    else:
        return "<h2>blog float todo<h2>"


if __name__ == '__main__':
    app.run(debug=True)
