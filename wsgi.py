from flask import Flask, jsonify

application  = Flask(__name__)

customers = [{'cid': '1-2345-67', 'value': 'Active'}, {'cid': '2-2345-67', 'value': 'Active'},
             {'cid': '3-2345-67', 'value': 'Active'}, {'cid': '4-2345-67', 'value': 'Active'},
             {'cid': '5-2345-67', 'value': 'Active'}, {'cid': '6-2345-67', 'value': 'Active'},
             {'cid': '7-2345-67', 'value': 'Active'}]

@application.route('/', methods=['GET'])
def default():
    return jsonify({'message': 'alive'})

@application.route('/customers/active', methods=['GET'])
def getList():
    return jsonify({'customers': customers})

@application.route('/customers/active/<string:cid>', methods=['GET'])
def getOne(cid):
    customersResult = [customer for customer in customers if customer['cid'] == cid]
    return jsonify({'customer': customersResult[0]})

if __name__ == '__main__':
    application.run()
