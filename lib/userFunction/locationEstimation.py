from mongoOperations import *

userId = "fHtTaujcyKvXglE33Z5yIw"
user = findUser(userId)

reviews = findReviews(userId)

#print reviews.count()
for review in reviews:
	business = findBusiness(review['business_id'])
	print business
