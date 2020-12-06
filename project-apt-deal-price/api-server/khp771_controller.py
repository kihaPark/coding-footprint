from flask import Blueprint, render_template, abort, request
from jinja2 import TemplateNotFound
import json
from prediction_man import predictionMan
from statistics_man import statisticsMan
from query_man import queryMan


khp771 = Blueprint('khp771', __name__)

pm = predictionMan()
sm = statisticsMan()
qm = queryMan()

@khp771.route('/khp771/')
def khp_test_page():
    deal_count = sm.data_to_dict(id=0)
    # pyung_price = sm.data_to_dict(id=2)
    # render_template('index.html')
    return json.dumps(deal_count, ensure_ascii=False)

# 현황 파악 섹션
@khp771.route('/khp771/deal_count')
def deal_count():
    result = sm.data_to_dict(id=0)
    return json.dumps(result, ensure_ascii=False)

@khp771.route('/khp771/pyung_price')
def pyung_price():
    result = sm.data_to_dict(id=2)
    return json.dumps(result, ensure_ascii=False)


# 지역별 세부 내용 섹션
@khp771.route('/khp771/size_deal_count', methods=['GET'])
def size_deal_count():
    region = request.args.get('region') 
    result = sm.data_to_dict(id=4, region=region)
    return json.dumps(result, ensure_ascii=False)

@khp771.route('/khp771/size_pyung_price', methods=['GET'])
def size_pyung_price():
    region = request.args.get('region') 
    result = sm.data_to_dict(id=6, region=region)
    return json.dumps(result, ensure_ascii=False)

@khp771.route('/khp771/brand_apt_pyung_price', methods=['GET'])
def brand_apt_pyung_price():
    region = request.args.get('region') 
    result = sm.brand_apt_pyung_price(region=region)
    return json.dumps(result, ensure_ascii=False)

@khp771.route('/khp771/brand_apt_deal_count', methods=['GET'])
def brand_apt_deal_count():
    region = request.args.get('region') 
    result = sm.brand_apt_deal_count(region=region)
    return json.dumps(result, ensure_ascii=False)

@khp771.route('/khp771/recent_deal_list', methods=['GET'])
def recent_deal_list():
    region = request.args.get('region') 
    result = qm.recent_deal_list(region=region)
    print(result)
    return json.dumps(result, ensure_ascii=False)


# 예측 섹션
@khp771.route('/khp771/predict_price', methods=['GET'])
def predict_price():
    region = request.args.get('region') 
    region_sub = request.args.get('region_sub') 
    pyung = request.args.get('pyung') 
    result = pm.predict_price(region=region, region_sub=region_sub, pyung=pyung)
    return json.dumps(result, ensure_ascii=False)

@khp771.route('/khp771/predict_price_all', methods=['GET'])
def predict_price_all():
    region = request.args.get('region') 
    pyung = request.args.get('pyung') 
    result = pm.predict_price_all(region=region, pyung=pyung)
    return json.dumps(result, ensure_ascii=False)

@khp771.route('/khp771/get_apply_home', methods=['GET'])
def get_apply_home():
    region = request.args.get('region')
    is_pyung = request.args.get('is_pyung') 
    result = pm.get_apply_home(region=region, is_pyung=is_pyung)
    return json.dumps(result, ensure_ascii=False)


# 차트 섹션
@khp771.route('/khp771/chart_deal_count', methods=['GET'])
def chart_deal_count():
    region1 = request.args.get('region1')
    region2 = request.args.get('region2')
    result = sm.compare_data(id=0, region1=region1, region2=region2)
    return json.dumps(result, ensure_ascii=False)

@khp771.route('/khp771/chart_pyung_price', methods=['GET'])
def chart_pyung_price():
    region1 = request.args.get('region1')
    region2 = request.args.get('region2')
    result = sm.compare_data(id=2, region1=region1, region2=region2)
    return json.dumps(result, ensure_ascii=False)




