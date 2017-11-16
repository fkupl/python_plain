from flask import Flask, jsonify

application  = Flask(__name__)

languages = [{'cid': '1-2345-67', 'value': 'Active'}, {'cid': '2-2345-67', 'value': 'Active'},
             {'cid': '3-2345-67', 'value': 'Active'}, {'cid': '4-2345-67', 'value': 'Active'},
             {'cid': '5-2345-67', 'value': 'Active'}, {'cid': '6-2345-67', 'value': 'Active'},
             {'cid': '7-2345-67', 'value': 'Active'}]

@application.route('/', methods=['GET'])
def default():
    return jsonify({'message': 'It works!'})

@application.route('/customers', methods=['GET'])
def getList():
    return jsonify({'customers': languages})

@application.route('/customers/<string:cid>', methods=['GET'])
def getOne(isoParam):
    customers = [customer for customer in customers if customer['cid'] == cid]
    return jsonify({'customer': customers[0]})

if __name__ == '__main__':
    application.run()
