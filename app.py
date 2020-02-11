from flask import Flask, jsonify, abort, request

app = Flask(__name__)

cars = [
    {
        "id": 1,
        "name": "Ferrari",
        "model": "GTO",
        "colour": "Orange",
    },
    {
        "id": 2,
        "name": "Skoda",
        "model": "Estelle",
        "colour": "Miserable Brown"
    },
    {
        "id": 3,
        "name": "Porsche",
        "model": "911 Turbo",
        "colour": "Silver"
    }
]

@app.route('/api/v1.0/cars', methods=['GET'])
def get_tasks():
    return jsonify({'cars': cars})

@app.route('/api/v1.0/cars', methods=['POST'])
def create_task():
    if not request.json or not 'name' in request.json:
        abort(400)
    task = {
        'id': cars[-1]['id'] + 1,
        'name': request.json['name'],
        'model': request.json['model'],
        'colour': request.json['colour'],
    }
    cars.append(task)
    return jsonify({'cars': cars}), 201

app.run(host='0.0.0.0', debug=False)
