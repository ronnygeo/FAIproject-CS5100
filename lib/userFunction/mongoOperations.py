from pymongo import MongoClient

client = MongoClient()

db = client['yelp']
user_collection = db.user
review_collection = db.review
business_collection = db.business
tip_collection = db.tip

def getUsers():
    return user_collection.find()

def findUser(userId):
    return user_collection.find_one({"user_id": userId})

def findReviews(userId):
    return review_collection.find({"user_id": userId})

def findBusiness(businessId):
    return business_collection.find_one({"business_id": businessId})

#
# def test():
#     for movie in movie_collection.find():
#         for r in ratings_collection.find({"movieId": movie["movieId"]}):
#             print movie, r
#             break
#         for t in tags_collection.find({"movieId": movie["movieId"]}):
#             print t
#             break
#         for l in links_collection.find({"movieId": movie["movieId"]}):
#             print l
#             break
#         break

# print ratings_collection.find({"userId": 295}).count()



# for rating in ratings_collection.find():
#	print rating["movieId"]
