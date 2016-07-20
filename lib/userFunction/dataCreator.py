from mongoOperations import getUsers, getUsersFromUserFriends
from userExtract import extractFriends
from locationEstimation import getUserLocation
import json

users = getUsersFromUserFriends(500)
data = {}
# friends = {}
friends = []
i = 0
# print "STATUS:"
usersCount = users.count()
print usersCount
for user in users:
    friend = {}
    i += 1
    print "Processing User", i,"of", usersCount
    # print "Percentage Complete: ", float(i/usersCount) * 100,"%"
    userId = user['user_id']
    data[userId] = getUserLocation(userId)
    data[userId]["user_id"] = userId
    data[userId]["friends"] = user["friends"]
    friends.append(data[userId])


# from pymongo import MongoClient
#
# client = MongoClient()
#
# db = client['yelp']
#
# db.user_test.insert_many(friends)

with open('../../static/json/user_location_data.json', 'w+') as outfile:
    json.dump(friends, outfile)
