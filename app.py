# airline_demand_app/app.py
from flask import Flask, render_template, request, jsonify
import requests
from bs4 import BeautifulSoup
import random

app = Flask(__name__)

# Mock function to simulate airline data scraping or API call
def get_airline_data():
    # Simulated airline data
    return [
        {"origin": "SYD", "destination": "MEL", "price": random.randint(100, 300), "date": "2025-07-15"},
        {"origin": "SYD", "destination": "BNE", "price": random.randint(100, 250), "date": "2025-07-15"},
        {"origin": "MEL", "destination": "SYD", "price": random.randint(100, 300), "date": "2025-07-16"},
        {"origin": "PER", "destination": "SYD", "price": random.randint(150, 350), "date": "2025-07-17"},
    ]

@app.route('/')
def index():
    data = get_airline_data()
    return render_template('index.html', data=data)

@app.route('/api/data')
def api_data():
    data = get_airline_data()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
