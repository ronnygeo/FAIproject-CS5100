from mongoOperations import *
from latLonConversion import getLatLngCenter

userId = "fHtTaujcyKvXglE33Z5yIw"
user = findUser(userId)

reviews = findReviews(userId)

latlondeg = []
#print reviews.count()
for review in reviews:
	business = findBusiness(review['business_id'])
	#print business
	latBus = business['latitude']
	lonBus = business['longitude']

	latlondeg.append({"LATIDX": latBus, "LNGIDX": lonBus})

print latlondeg
print getLatLngCenter(latlondeg)
	#
	# lon1, lat1, lon2, lat2 = map(radians, [lonBus, latBus, lonUser, latUser])
	# dlon = lon2 - lon1
	# dlat = lat2 - lat1
	# a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
	# c = 2 * atan2(sqrt(a), sqrt(1-a))
	# radius = 6371
	# distance = radius * c
	# if distance < rad:
	# 	newData.append(b)


