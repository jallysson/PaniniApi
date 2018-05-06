import sys
sys.path.append("../Domain")

from sinopse import *
from flask import Flask, jsonify, request

app = Flask(__name__)

# GET /sinopse
@app.route('/sinopse')
def get_sinopse():
	response = get_sinopse_domain()
	return jsonify(response)

# POST /sinopse
@app.route('/sinopse', methods=['POST'])
def post_sinopse():
    post_sinopse_domain(request.json)
    return jsonify({'status': 200, 'mensagem': 'sinopse salva com sucesso.'})