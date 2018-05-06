import sys
sys.path.append("../")

from pymongo import MongoClient
from settings import *

client = MongoClient(mongodb_connection)

database_mongodb = client['mangas-database']
