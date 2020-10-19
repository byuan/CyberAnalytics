from flask import Flask, request, jsonify
from global_threats import GlobalThreats

app = Flask(__name__)

@app.route('/')
def health_check():
    return {'status':'ok'}

@app.route('/keywords', methods=['GET','POST','PUT'])
def keywords():
    if request.method == 'GET':
        return jsonify(GlobalThreats().get_keywords())
    else:
        if 'keyword' not in request.json():
            return  'Keyword is required', 400
        if 'weight' not in request.json():
            return  'Weight is required', 400
        if request.method == 'POST':
            return jsonify(GlobalThreats().add_keyword(request.json()))
        elif request.method == 'PUT':
            return jsonify(GlobalThreats().update_keyword(request.json()))


@app.route('/articles', methods=['GET'])
def articles():
    return jsonify(GlobalThreats().get_articles())
    