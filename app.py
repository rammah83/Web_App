from flask import Flask

app = Flask(__name__)


@app.get('/')
def home():
    return "<h1>hello world!!</h1>"


if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True, use_reloader=True)
