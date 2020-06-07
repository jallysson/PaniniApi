from settings import HOST, PORT
import sys
sys.path.append('collections')
from synopsis import synopsis
from flask import Flask, jsonify, request

app = Flask(__name__)
methods = ['GET', 'POST']

@app.route('/')
def up():
	return 'PaniniApi Up'

@app.route('/synopsis', methods=methods)
def _synopsis():
    return synopsis(request)


app.run(host=HOST, port=PORT, debug=True)