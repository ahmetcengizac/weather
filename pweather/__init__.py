from flask import Flask, render_template, request
import requests
import time
from typing import Any

app = Flask(__name__)


@app.route('/temperature', methods=['POST'])
def temperature():
    zipcode = request.form['zip']
    country_code = request.form['country']
    r = requests.get('http://api.openweathermap.org/data/2.5/weather?zip='+zipcode+','+country_code+'&appid=ccf1834504db592be91d979082b92de2')
    json_object = r.json()
    temp_k = float(json_object['main']['temp'])
    temp_c = round(temp_k - 273.15 ,2)
    return render_template('temperature.html', temp=temp_c)

@app.route('/')
def index():
	return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)