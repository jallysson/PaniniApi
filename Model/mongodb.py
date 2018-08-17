from pymongo import MongoClient
import sys

sys.path.append("../")
from settings import *

client = MongoClient(mongodb_connection)

database_mongodb = client['mangas-database']