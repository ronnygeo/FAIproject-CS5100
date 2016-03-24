from pymongo import MongoClient
from bson.code import Code
from mongoOperations import *

client = MongoClient()

db = client['yelp']
user_collection = db.user
review_collection = db.review
business_collection = db.business

db.create_collection('user_review')

users = []
i = 1
for user in user_collection.find():
	print "user", i
	user['reviews'] = review_collection.find({'user_id': user['user_id']})
	r = 1
	for review in user['reviews']:
		print "review", r
		review['business_data'] = findBusiness([review['business_id']])
		r += 1
	users.append(user)
	i += 1

result = db.user_review.insert_many(users)
print result.inserted_ids