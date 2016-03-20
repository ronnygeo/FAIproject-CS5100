import math


def rad2degr(rad):
	return rad * 180 / math.pi


def degr2rad(degr):
	return degr * math.pi / 180


def getLatLngCenter(latLngInDegr):
	# LATIDX = 0
	# LNGIDX = 1
	sumX = 0
	sumY = 0
	sumZ = 0

	for i in range(len(latLngInDegr)):
		lat = degr2rad(latLngInDegr[i]['LATIDX'])
		lng = degr2rad(latLngInDegr[i]['LNGIDX'])
		# sum of cartesian coordinates
		sumX += math.cos(lat) * math.cos(lng)
		sumY += math.cos(lat) * math.sin(lng)
		sumZ += math.sin(lat)
	avgX = sumX / len(latLngInDegr)
	avgY = sumY / len(latLngInDegr)
	avgZ = sumZ / len(latLngInDegr)

	# convert average x, y, z coordinate to latitude and longtitude
 	lng = math.atan2(avgY, avgX)
	hyp = math.sqrt(avgX * avgX + avgY * avgY)
	lat = math.atan2(avgZ, hyp)

	return [rad2degr(lat), rad2degr(lng)]