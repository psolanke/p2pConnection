from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World"

@app.route('/api/v1.0/get_public_ip', methods=['GET'])
def get_public_ip():
    return jsonify({'ip': request.remote_addr}), 200

@app.route('/api/v1.0/update_registry', methods=['POST'])
def update_registry():
    public_ip = request.remote_addr
    mac_address = request.get_json()
    return jsonify(mac_address), 200

if __name__ == '__main__':
    app.run(debug=True)