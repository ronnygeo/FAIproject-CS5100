from pymongo import MongoClient
from settings import REF_USER_ID

import operator
import csv
import json
from bson import json_util

client = MongoClient()

db = client['yelp']

database = db.user_review_friends
user_friends = db.user_friends_limited
business = db.business
review = db.review
userId = REF_USER_ID


def getUserFriends(userId):
    # we are finding all the friends of this particular user.
    data = database.find_one({"_id": userId})
    return data["user_friends"][0]

