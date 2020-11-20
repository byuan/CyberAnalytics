from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from datetime import datetime, date, timedelta
from app.global_threats import GlobalThreats
from app.google_trends import GoogleTrends
from app.thermometer import Thermometer

app = Flask(__name__)
CORS(app)

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

@app.route('/analysis/keywords', methods=['GET'])
def analysis_keywords():
    n_days = 7
    if request.args.get('days'):
        n_days = int(request.args.get('days'))
    return jsonify(GlobalThreats().get_keywords_analysis(n_days=n_days))

@app.route('/analysis/keywordsByDay', methods=['GET'])
def analysis_keywords_weighted_by_day():
    n_days = 7
    source = None
    keywords_data = []
    if request.args.get('days'):
        n_days = int(request.args.get('days'))
    if request.args.get('source') and request.args.get('source') != 'all':
        source = str(request.args.get('source'))
        keywords_data = GlobalThreats().get_keywords_analysis_by_source(source,n_days=n_days)
    else:
        keywords_data = GlobalThreats().get_keywords_analysis(n_days=n_days)

    keyword_by_day = {}
    for keyword in keywords_data:
        data = {'x': keyword['date'],'y': keyword['weighted count']}

        if keyword['word'] in keyword_by_day:
            keyword_by_day[keyword['word']].append(data)
        else:
            keyword_by_day[keyword['word']] = [data]

    return keyword_by_day

@app.route('/googleTrends')
def google_analytics():
    return GoogleTrends().get_interest_overtime()

@app.route('/analysis/thermometer', methods=['GET'])
def analysis_thermometer():
    gt = GlobalThreats()
    min_score = gt.get_minimum_score()[0]['weighted count']
    max_score = gt.get_maximum_score()[0]['weighted count']
    todays_score = gt.get_todays_score()[0]['weighted count']
    return {'threat_level':int(round(((todays_score - min_score) * 100) / (max_score - min_score)))}

@app.route('/analysis/thermometerHistorical')
def analysis_thermometer_historical():
    return jsonify({'Risk':Thermometer().get_historical()})
    