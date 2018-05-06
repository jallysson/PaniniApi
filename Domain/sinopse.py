import sys
sys.path.append("../Model")

from mongodb import *

album = database_mongodb['sinopse_collection']

def get_sinopse_domain():
	sinopses = []
	for sinopse in album.find():
		del sinopse['_id']
		sinopses.append(sinopse)
	return sinopses

def post_sinopse_domain(request):
	album.insert_one(request).inserted_id