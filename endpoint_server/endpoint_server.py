import re, uuid
from flask import Flask, jsonify, request
import json
import requests


# from ../client/client import P2PClient

PUBLIC_SERVER_ADDRESS = 'http://psolanke.pythonanywhere.com'
UPDATE_DEVICE_REGISTRY_API_PATH = '/api/v1.0/update_device_registry'
HEADERS = {'Content-type': 'application/json', 'Accept': 'text/plain'}

app = Flask(__name__)

def get_host_MAC_address():
    return ':'.join(re.findall('..', '%012x' % uuid.getnode()))

@app.route('/')
def index():
    return get_host_MAC_address()

def register_self(mac_address):
    data = json.dumps({'mac_addr':mac_address})
    response = requests.post(PUBLIC_SERVER_ADDRESS+UPDATE_DEVICE_REGISTRY_API_PATH,
                            data=data, 
                            headers=HEADERS)
    return response.json()['port_num']

# @app.route('/api/v1.0/get_public_ip', methods=['GET'])
# def get_public_ip():
#     return jsonify({'ip': request.remote_addr}), 200

# @app.route('/api/v1.0/update_device_registry', methods=['POST'])
# def update_registry():
#     request_json = request.get_json()
#     public_ip = request.remote_addr
#     mac_address = request_json['mac_addr']
#     remote_port = request.environ.get('REMOTE_PORT')
#     StorageManager.update_registry(public_ip , remote_port, mac_address)
#     return jsonify(request_json), 200

# @app.route('/api/v1.0/get_device_data', methods=['POST'])
# def get_device_data():
#     request_json = request.get_json()
#     mac_address = request_json['mac_addr']
#     device_data = StorageManager.get_device(mac_address)
#     return jsonify(device_data), 200


if __name__ == '__main__':
    mac_address = get_host_MAC_address()
    port_num = register_self(mac_address)
    app.run(host='0.0.0.0', port=port_num)
