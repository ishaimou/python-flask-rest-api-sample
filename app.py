from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/', methods=['GET'])
def success():
	if(request.method == 'GET'):
		data = {"status": "success"}
		return jsonify(data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
