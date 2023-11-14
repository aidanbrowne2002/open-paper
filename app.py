from flask import Flask, jsonify


app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World! Open-paper'

@app.route('/api/')
def hello():
    return jsonify({'bitmap':'000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'})

if __name__ == '__main__':
    app.run()
