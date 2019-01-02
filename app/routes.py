from app import app
import json

mock_answer = json.dumps({'USD': 69.52,
                          'EUR': 79.66,
                          'GBP': 88.28})


@app.route('/')
@app.route('/rates')
def index():
    return mock_answer
