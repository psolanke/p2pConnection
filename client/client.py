import requests
import json
import argparse

DEV_SERVER_ADDRESS = 'http://127.0.0.1:5000'
PUBLIC_SERVER_ADDRESS = 'http://psolanke.pythonanywhere.com'
UPDATE_DEVICE_REGISTRY_API_PATH = '/api/v1.0/update_device_registry'
GET_DEVICE_DATA_API_PATH = '/api/v1.0/get_device_data'

class P2PClient(object):
    HEADERS = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    def __init__(self, dev_flag):
        if dev_flag:
            self.server_address = DEV_SERVER_ADDRESS
        else:
            self.server_address = PUBLIC_SERVER_ADDRESS

    def register_self(self, mac_address):
        data = json.dumps({'mac_addr':mac_address})
        response = requests.post(self.server_address+UPDATE_DEVICE_REGISTRY_API_PATH,
                                data=data, 
                                headers=self.HEADERS)
        print(response.json())

    def get_device_data(self, mac_address):
        data = json.dumps({'mac_addr':mac_address})
        response = requests.post(self.server_address+GET_DEVICE_DATA_API_PATH,
                                data=data, 
                                headers=self.HEADERS)
        print(response.json())
        return response.json()['public_ip'], response.json()['port_num']

    def get_device_index_page(self, public_ip, port_num):
        response = requests.post('http://122.170.109.221:'+port_num, 
                                headers=self.HEADERS)
        print(response.text)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Client for p2p')
    parser.add_argument('--dev', action='store_true',help='Argument to specify using dev server or public server')
    args = parser.parse_args()
    p2p_obj = P2PClient(args.dev)
    device_mac = 'ec:08:6b:10:2d:ca'
    ip , port = p2p_obj.get_device_data(device_mac)
    p2p_obj.get_device_index_page(ip, port)   
