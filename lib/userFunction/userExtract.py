from mongoOperations import findUser

userId = "fHtTaujcyKvXglE33Z5yIw"


def extractFriends(userId):
	"""
	:param userId:
	:return: Returns a list of all friends of the user.
	Finds all the friends of a particular user.
	"""
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

	return currentUsers

	# print currentUsers

	# for user in currentUsers:
	# 	print user
	# 	if user != userId:
	# 		print findUser(user)