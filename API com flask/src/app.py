from flask import Flask, url_for

app = Flask(__name__)


@app.route("/helloworld")
def hello_world():
    return {"message": "Hello, World!"}


@app.route("/bemvindo/<usuario>/<int:idade>")
def bem_vindo(usuario, idade):
    return {
        "Usuário": usuario,
        "Idade": idade,
    }


@app.route("/projects/")
def projects():
    return "The Project Page"


@app.route("/about", methods=["Get", "POST"])
def about():
    return "The About Page"


with app.test_request_context():
    print(url_for("hello_world"))
    print(url_for("projects"))
    print(url_for("about", next="/"))
    print(url_for("bem_vindo", usuario="joao", idade=24))
