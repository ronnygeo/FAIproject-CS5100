from lib.mongoImport import db_connect, get_collection
import operator
import json
from bson import json_util

db = db_connect("yelp")
review = get_collection("review")
tip = get_collection("tip")

