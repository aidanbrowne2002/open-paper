from flask import Flask, jsonify
import test_bitmap


app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World! Open-paper'

@app.route('/api/')
def hello():
    bitmapimg = test_bitmap.createImage()
    return jsonify({'bitmap':bitmapimg})

if __name__ == '__main__':
    app.run()
