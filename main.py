from settings import HOST, PORT
from endpoints.sinopses import *

@app.route("/")
def up():
	return "PaniniApi Up"

if __name__ == '__main__':
	app.run(host = HOST, port = PORT)