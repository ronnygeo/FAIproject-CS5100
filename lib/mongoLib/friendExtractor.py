from pymongo import MongoClient
from settings import REF_USER_ID

import operator
import csv
import json
from bson import json_util

client = MongoClient()

db = client['yelp']

user_friends = db.user_friends_limited
business = db.business
review = db.review


userId = REF_USER_ID


# we are finding all the friends of this particular user.
friends = db.user_friends_limited.find_one({"user_id": userId})

with open('../../static/json/'+ userId + '_friends.json', 'w+') as outfile:
    json.dump(friends, outfile, default=json_util.default)


#myfile = open('static/csv/'+ max_review_user + '_reviews_business_model.csv', 'wb')
#wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
#wr.writerow(data)
