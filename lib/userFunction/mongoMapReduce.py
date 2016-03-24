from pymongo import MongoClient
from bson.code import Code

client = MongoClient()

db = client['yelp']
user_collection = db.user
review_collection = db.review
business_collection = db.business


mapper = Code("""
               function () {
                   emit(this.user_id, 1);
               }
               """)

reducer = Code("""
                function (key, values) {
                  var total = 0;
                  for (var i = 0; i < values.length; i++) {
                    total += values[i];
                  }
                  return total;
                }
                """)

result = user_collection.map_reduce(mapper, reducer, "myresults")

print result