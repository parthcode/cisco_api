from flask import Flask, request
import requests

app = Flask(__name__)


@app.route('/ping', methods=['POST'])
def ping():
    if not request.is_json:
        return "Please send a json payload"
    content = request.get_json()
    url_response = requests.get(content['url'])
    return str(url_response.content)


@app.route('/info', methods=['GET'])
def info():
    return "{“Receiver”: “Cisco is the best!”}"


app.run(host='0.0.0.0', port=8090)
