from flask import Flask, render_template

app = Flask(__name__)


app.secret_key = "mysecretkey"

@app.route('/')
def Index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(port=4000, debug=True)