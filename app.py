from flask import Flask, jsonify


app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World! Open-paper'

@app.route('/api/')
def hello():
    return jsonify({'bitmap': 'Hello From Python!'})

if __name__ == '__main__':
    app.run()
