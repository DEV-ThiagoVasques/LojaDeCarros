from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def inicio():
    nome = "Thiago"
    return render_template("index.html", nome=nome)

app.run(debug=True)