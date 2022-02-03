import requests, json
from chalice import Chalice

app = Chalice(app_name='tradingview-webhook-alerts')

BASE_URL = "https://paper-api.alpaca.markets"
API_KEY = 'alpaca-api-key'
SECRET_KEY = 'alpaca-secret-key'

ORDERS_URL = "{}/v2/orders".format(BASE_URL)
HEADERS = {'APCA-API-KEY-ID': API_KEY, 'APCA-API-SECRET-KEY': SECRET_KEY}


@app.route('/buy_stocks', methods=['POST'])
def buy_stock():
    request = app.current_request
    webhook_msg = request.json_body

    data = {
        "symbol": webhook_msg['ticker'],
        "qty": 1,
        "side": "buy",
        "type": "limit",
        "limit_price": webhook_msg['close'],
        "time_in_force": "gtc",
        "order_class": "simple",
        "take_profit": {
            "limit_price": webhook_msg['close'] * 1.05
        },
        "stop_loss": {
            "stop_price": webhook_msg['close'] * 0.98,
        }
    }

    r = requests.post(ORDERS_URL, json=data, headers=HEADERS)

    response = json.loads(r.content)

    return {
        'webhook_message': webhook_msg,
        'response': response,
        # 'id': response['id'],
        # 'client_order_id': response['client_order_id']
    }
