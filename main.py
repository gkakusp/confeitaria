from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def inicial():
    return render_template('index.html')


@app.route('/contato')  # Rota para a página de contato
def contato():
    return render_template('contato2.html')


if __name__ == '__main__':
    app.run()
