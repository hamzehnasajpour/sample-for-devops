from flask import Flask, jsonify, request

app = Flask(__name__)

rate = None

@app.route('/set_rate', methods=['POST'])
def set_rate():
    global rate
    data = request.get_json()
    if not data or 'currency_pair' not in data:
        return jsonify({'message': 'currency_pair parameter is missing.'}), 400
    if not data or 'rate' not in data:
        return jsonify({'message': 'rate parameter is missing.'}), 400
    currency_pair = data['currency_pair']
    rate = data['rate']
    return jsonify({'rate': rate, 'message': f'Rate for {currency_pair} is set to {rate}.'})

@app.route('/get_rate', methods=['GET'])
def get_rate():
    global rate
    currency_pair = request.args.get('currency_pair')
    if not currency_pair:
        return jsonify({'message': 'currency_pair parameter is missing.'}), 400
    if rate is None:
        return jsonify({'message': f'No rate set for {currency_pair} yet.'}), 404
    return jsonify({'rate': rate, 'message': f'Rate for {currency_pair} is {rate}.'})

if __name__ == '__main__':
    app.run()
