import sys
sys.path.append("../Model")

from mongodb import *

def get_sinopse():
	album = database_mongodb['sinopse_collection']
	sinopse = album.find_one()
	del sinopse['_id']
	return sinopse