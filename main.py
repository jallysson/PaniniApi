from settings import HOST, PORT
import sys
sys.path.append('collections')
from synopsis import synopsis
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def up():
	return 'PaniniApi Up'

@app.route('/synopsis', methods=['GET'])
def _get_synopsis():
    response = synopsis()
    return jsonify(response)

@app.route('/synopsis', methods=['POST'])
def _post_synopsis():
    response = synopsis(request)
    return jsonify(response)

app.run(host=HOST, port=PORT, debug=True)