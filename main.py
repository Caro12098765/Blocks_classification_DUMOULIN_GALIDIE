from flask import Flask, request

# ML Pkg
import pickle as p
import json

import joblib

app = Flask(__name__)

random_forest_model = p.load(open('modelRandomForest.pickle', 'rb'))

def create(data):
    result = []
    for key, value in data.items():
        result.append(float(value))
    return result

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello():
    return '/api_Block_Classification for api services)'

#for only one prediction
@app.route('/api_Block_Classification', methods=['POST'])
def random_forest():
    data = request.get_json(force=True)
    input_list = [create(data)]

    if len(input_list[0]) != 10:
        response = {"response":"error could not predict your data, please verify your data"}
    else:
        prediction = random_forest_model.predict(input_list)[0]
        response = {"response": int(prediction)}
    return response

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port='5000')