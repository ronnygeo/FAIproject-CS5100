from mongoOperations import getUsers
from userExtract import extractFriends
from locationEstimation import getUserLocation
import json

users = getUsers()
data = {}
friends = {}

for user in users:
	userId = user['user_id']
	data[userId] = getUserLocation(userId)
	friends[userId] = extractFriends(userId)

with open('../../static/json/user_country_data.json', 'w+') as outfile:
	json.dump(data, outfile)

with open('../../static/json/user_friends_data.json', 'w+') as outfile:
	json.dump(friends, outfile)

