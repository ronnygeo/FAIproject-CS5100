from pymongo import MongoClient

import operator
import csv
import json
from bson import json_util

client = MongoClient()

db = client['yelp']

business = db.business
review = db.review
database = db.user_review_friends

userdb = {}
reviewdb = []

def getUserReviews(userId):
	# we are finding all the reviews from this particular user.
	for r in db.review.find({"user_id": {"$in": userId}}):
		#getting the details of the business.
		cursor = db.business.find({"business_id": r["business_id"],
										  "categories": {"$in": ["Restaurants", "Fast Food", "Food", "Coffee & Tea"] }})
		if cursor.count():
			business_data = cursor[0]
			business_attr = business_data["attributes"]
			#print r["business_id"]
			#print r["stars"]
			#print business_attr
			new_info = r.copy()
			new_info.update(business_data)
			new_info["userRating"] = r["stars"]
			reviewdb.append(new_info)
	return reviewdb


def getUserReviews3(userId):
	for r in db.review_business.find({"user_id": {"$in": userId}}):
		business_data = r["business_detail"]
		del r["business_detail"]
		new_info = r.copy()
		new_info.update(business_data)
		new_info["userRating"] = r["stars"]
		reviewdb.append(new_info)
	return reviewdb


def getUserReviews2(userId):

	for r in database.find_one({"_id": {"$in": userId}})["reviews"]:
		business_data = r["business_detail"][0]
		del r["business_detail"]
		new_info = r.copy()
		new_info.update(business_data)
		new_info["userRating"] = r["stars"]
		reviewdb.append(new_info)
	return reviewdb

