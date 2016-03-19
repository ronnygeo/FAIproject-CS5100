from lib.mongoImport import db_connect, get_collection
import operator
import json
from bson import json_util

db = db_connect("yelp")
business = get_collection("business")
review = get_collection("review")
tip = get_collection("tip")
