from database.mongodb import panini_db
from settings import SYNOPSIS_COLLECTION, REPOSITORY
import json
from jsonschema import validate

with open('collections/schemas/synopsis-schema.json') as json_file:
  schema = json.load(json_file)

collection = panini_db[SYNOPSIS_COLLECTION]

def synopsis(request=None):
	if request:
		try:
			validate(instance=request.json, schema=schema)
			collection.insert_one(request.json).inserted_id
			return {'message': 'Saved :D'}
		except:
			return {
				'message': 'You sent an invalid json schema :/',
				'sample': REPOSITORY
			}
		
	response = []
	for synopsis in collection.find():
		del synopsis['_id']
		response.append(synopsis)
	return response