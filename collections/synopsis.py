from database.mongodb import panini_db
from settings import SYNOPSIS_COLLECTION

collection = panini_db[SYNOPSIS_COLLECTION]

def synopsis(request=None):
	if request:
		collection.insert_one(request.json).inserted_id
		return {'message': 'Ok :D'}
		
	response = []
	for synopsi in collection.find():
		del synopsi['_id']
		response.append(synopsi)
	return response