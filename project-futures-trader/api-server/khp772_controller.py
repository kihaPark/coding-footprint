from flask import Blueprint, render_template, abort, request
from jinja2 import TemplateNotFound
import json
from rl_futures_trader import FuturesTrader


khp772 = Blueprint('khp772', __name__)

ft = FuturesTrader()

@khp772.route('/khp772/begin-trade')
def begin_trade():
    result = ft.begin_trade()
    # print('begin-trade!!')
    return json.dumps(result, ensure_ascii=False)

@khp772.route('/khp772/next-trade')
def next_trade():
    result = ft.next_trade()
    # print('next-trade!!')
    return json.dumps(result, ensure_ascii=False)




