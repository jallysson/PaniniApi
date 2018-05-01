import sys
sys.path.append("../Domain")

from sinopse import *
from flask import Flask, jsonify, request

app = Flask(__name__)

# GET /sinopse/
@app.route('/sinopse')
def sinopse():
	response = get_sinopse()
	return jsonify(response)