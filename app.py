from flask import Flask

app = Flask(__name__)


@app.route('/')
def Index():
    return 'Probando'


if __name__ == "__main__":
    app.run(port=4000, debug=True)