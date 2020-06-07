import sys
from flask import Flask, jsonify, request

app = Flask(__name__)

# GET /sinopse
@app.route('/sinopse', methods=['GET'])
def get_sinopse():
	return jsonify({'Sinopses': 'Aí sim :D'})

# POST /sinopse
@app.route('/sinopse', methods=['POST'])
def post_sinopse():
    return jsonify({'Message': 'Aí sim :D'})