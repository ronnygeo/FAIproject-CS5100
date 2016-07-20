from mongoOperations import getUsers, getUsersFromUserFriends, getUsersFromUserFriendsAsc
from userExtract import extractFriends
from locationEstimation import getUserLocation
import ujson

users = getUsersFromUserFriendsAsc(1)
res = []
usersCount = users.count()
for user in users:
	data = {}
	userId = user['user_id']
	data = getUserLocation(userId)
	data["user_id"] = userId
	data["friends"] = []
	i = 0
	for f in user["friends"]:
		if f != userId:
			friend = {}
			friend = getUserLocation(f)
			# friend["user_id"] = f
			# print friend
			data["friends"].append(friend)
	res.append(data)

# from pymongo import MongoClient
#
# client = MongoClient()
#
# db = client['yelp']
#
# db.user_test.insert_many(res)
#
with open('../../static/json/user_friends_location_data.json', 'w+') as outfile:
	ujson.dump(res, outfile)
