from flask import Flask, jsonify, request
import test_bitmap
import requests
import logging
import json
from get_requests import city







app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World! Open-paper'


@app.route('/api/initial/', methods=['GET'])
def initalAPI():
    ip = request.headers['X-Real-IP']
    city = city.getcity(ip)
    device = request.args.get('device')
    return jsonify({'api': 'http://aidanbrowne2002.eu.pythonanywhere.com/api/weather/','check-in': '60', 'update': '1', 'city': city}), 200


@app.route('/api/weather/')
def hello():


    logging.basicConfig(format='%(levelname)s - %(asctime)s - %(message)s (line: %(lineno)d) [%(filename)s]',
                        datefmt='%d/%m/%Y %I:%M:%S', filename='logs.log', encoding='utf-8', level=logging.DEBUG)

    ip = request.headers['X-Real-IP']
    location_responce = requests.get(f"https://geolocation-db.com/jsonp/{ip}")
    if response.status_code == 200:
        city = location_responce.json()['city']

    api_key = '78f2e9d22945768088e9d0da792f8d68'


    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

    response = requests.get(url)

    if response.status_code == 200:
        logging.info(f'Weather data fetched successfully for {city}')
        data = response.json()
        temp = data['main']['temp']
        desc = data['weather'][0]['description']
        print(f'Temperature: {temp - 273.15} C')
        print(f'Description: {desc}')
    else:
        logging.error(f'Error fetching weather data for {city}')
        print('Error fetching weather data')
    bitmapimg = test_bitmap.createImage(city,round((temp- 273.15),1), desc)
    bitmapimgtext = str(bitmapimg)
    return jsonify({'bitmap': bitmapimgtext})

@app.route("/get_my_ip", methods=["GET"])
def get_my_ip():
    return jsonify({'ip': request.headers['X-Real-IP']}), 200

if __name__ == '__main__':
    app.run()
