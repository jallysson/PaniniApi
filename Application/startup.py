import sys
sys.path.append("Controller")
from sinopse_controller import *

@app.route("/")
def index():
	return "PaniniApi Up"

if __name__ == '__main__':
	app.run(debug = True)