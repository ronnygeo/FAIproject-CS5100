from mongoOperations import findUser

userId = "fHtTaujcyKvXglE33Z5yIw"


def extractFriends(userId):
	user = findUser(userId)

	#print user
	friends = user["friends"]

	#List of User and his friends
	currentUsers = []

	#adding user to the user list.
	currentUsers.append(user['user_id'])

	#adding friends of user to user list
	for friend in friends:
		if friend not in currentUsers:
			#print findUser(friend)
			currentUsers.append(friend)

	# print currentUsers

	for user in currentUsers:
		print user
		if user != userId:
			print findUser(user)