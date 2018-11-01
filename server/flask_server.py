from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api/v1.0/get_public_ip', methods=['GET'])
def get_public_ip():
	return jsonify({'ip': request.remote_addr}), 200

if __name__ == '__main__':
	app.run(debug=True)