from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from datetime import datetime, date, timedelta
from app.global_threats import GlobalThreats

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
    if request.args.get('days'):
        n_days = int(request.args.get('days'))
    keywords_data = GlobalThreats().get_keywords_analysis(n_days=n_days)


    keyword_by_day = {}
    max_date = datetime(1900,1,1)
    min_date = datetime.today()
    
    for keyword in keywords_data:
        data = {'x': keyword['date'],'y': keyword['weighted count']}

        data_date = datetime.strptime(keyword['date'],'%Y-%m-%d')
        if data_date > max_date:
            max_date = data_date
        elif data_date < min_date:
            min_date = data_date

        if keyword['word'] in keyword_by_day:
            keyword_by_day[keyword['word']].append(data)
        else:
            keyword_by_day[keyword['word']] = [data]
    
    labels = []
    delta = max_date - min_date
    for i in range(delta.days + 1):
        labels.append((min_date + timedelta(days=i)).strftime('%Y-%m-%d'))
    keyword_by_day['labels'] = labels

    return keyword_by_day
    