import json
from database.mongodb import panini_db
from settings import SYNOPSIS_COLLECTION

collection = panini_db[SYNOPSIS_COLLECTION]

def synopsis(request):


	return json.loads(request.data)

	# sinopses = []
	# for sinopse in album.find():
	# 	del sinopse['_id']
	# 	sinopses.append(sinopse)
	# return sinopses

	# return 'Test'
	
# def post_sinopse_domain(request):
# 	album.insert_one(request).inserted_id