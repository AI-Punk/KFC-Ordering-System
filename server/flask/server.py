from flask import Flask
from flask import make_response
from flask import request
import json
import flask
import Models.models
import random

app = Flask(__name__)
order_line = Models.models.OrderLine([])
@app.route('/api/createorder', methods=['POST'])
def create_order():
    # print("###"*10)
    # print(eval(request.get_data()))
    req_data = eval(request.get_data())
    print("/api/createorder == create_order() is visited.")
    print(req_data)
    order = Models.models.Order(req_data['user_id'], int(random.random()*10000), req_data['list'])
    order_line.push(order._dictData())
    response = make_response(json.dumps({
            "order_id": order.order_id
        }))
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'POST'
    response.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type'
    return response

@app.route('/api/getorders', methods=['GET'])
def get_orders():
    response = make_response(json.dumps({
        "orders": order_line._dictData()
    }))
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET'
    response.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type'
    return response
    
if __name__ == "__main__":
    app.run(debug=True)
