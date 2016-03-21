from mongoOperations import *
from latLonConversion import getLatLngCenter
import reverse_geocoder as rg
import operator
from businessCountry import BusinessCountry

def getUserLocation(userId):
	"""
	:param userId:
	:return: userCoords [lat, lon]
	Function to triangular the location of a user based on his reviewed business locations.
	"""
	user = findUser(userId)

	reviews = findReviews(userId)
	bCountry = {}
	latlondeg = []
	#print reviews.count()
	for review in reviews:
		businessCountryObj = BusinessCountry()
		business = findBusiness(review['business_id'])
		#print business['name']
		latBus = business['latitude']
		lonBus = business['longitude']
		#print latBus, lonBus
		businessCountryId = rg.search((latBus, lonBus))[0]["cc"]
		#print businessCountry
		#adding the business location to our dictionary.
		try:
			#bCountry[businessCountryId][0] += 1
			bCountry[businessCountryId].addCoord((latBus, lonBus))
		except KeyError:
			bCountry[businessCountryId] = businessCountryObj
			bCountry[businessCountryId].addCoord((latBus, lonBus))
	# print bCountry.iteritems().next()[1][0]
	userCountryKey = max(bCountry.iteritems(), key=operator.itemgetter(1))[0]
	# print bCountry
	# print userCountryKey

	for k, v in bCountry.items():
		#print v
		#print v.getCount()
		#print v.getCoords()
		if k == userCountryKey:
			#print v[1]
			for loc in v.getCoords():
				latlondeg.append({"LATIDX": loc[0], "LNGIDX": loc[1]})

	#print latlondeg
	# Triangularing user coords.
	userCoords = getLatLngCenter(latlondeg)
	userCountry = rg.search((userCoords[0], userCoords[1]))[0]['cc']
	userCoords.append(userCountry)
	#print userCountry
	return userCountry

	# lon1, lat1, lon2, lat2 = map(radians, [lonBus, latBus, lonUser, latUser])
	# dlon = lon2 - lon1
	# dlat = lat2 - lat1
	# a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
	# c = 2 * atan2(sqrt(a), sqrt(1-a))
	# radius = 6371
	# distance = radius * c
	# if distance < rad:
	# 	newData.append(b)

#print getUserLocation("fHtTaujcyKvXglE33Z5yIw")

#print getUserLocation("4mk28YCp7kCKI6WUp3Gl7w")

#getUserLocation("kGgAARL2UmvCcTRfiscjug")