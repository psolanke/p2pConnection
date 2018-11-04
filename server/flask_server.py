from flask import Flask, jsonify, request
import json
from storage_utils import StorageManager

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World"

@app.route('/api/v1.0/get_public_ip', methods=['GET'])
def get_public_ip():
    return jsonify({'ip': request.remote_addr}), 200

@app.route('/api/v1.0/update_device_registry', methods=['POST'])
def update_registry():
    request_json = request.get_json()
    public_ip = request.remote_addr
    mac_address = request_json['mac_addr']
    remote_port = request.environ.get('REMOTE_PORT')
    StorageManager.update_registry(public_ip , remote_port, mac_address)
    return jsonify(request_json), 200

@app.route('/api/v1.0/get_device_data', methods=['POST'])
def get_device_data():
    request_json = request.get_json()
    mac_address = request_json['mac_addr']
    device_data = StorageManager.get_device(mac_address)
    return jsonify(device_data), 200


if __name__ == '__main__':
    app.run(debug=True)