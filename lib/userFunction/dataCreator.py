from mongoOperations import getUsers
from userExtract import extractFriends
from locationEstimation import getUserLocation
import json

users = getUsers()
data = {}
friends = {}
i = 0
print "STATUS:"
usersCount = users.count()
for user in users:
	i += 1
	print "Processing User ", i,", ", user['name'],", of ", usersCount
	userId = user['user_id']
	data[userId] = getUserLocation(userId)
	#print data[userId]
	friends[userId] = extractFriends(userId)

with open('../../static/json/user_country_data.json', 'w+') as outfile:
	json.dump(data, outfile)

with open('../../static/json/user_friends_data.json', 'w+') as outfile:
	json.dump(friends, outfile)

