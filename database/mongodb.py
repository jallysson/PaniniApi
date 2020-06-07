from pymongo import MongoClient
from settings import MONGODB, PANINI_DB

client = MongoClient(MONGODB)

panini_db = client[PANINI_DB]