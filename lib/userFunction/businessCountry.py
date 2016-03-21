class BusinessCountry(object):

	def __init__(self, count=0, coords=None):
		self.count = count
		if coords == None:
			self.coords = []
		else:
			self.coords = coords

	def addCoord(self, coord):
		self.coords.append(coord)
		self.increaseCount()

	def increaseCount(self):
		self.count += 1

	def getCount(self):
		return self.count

	def getCoords(self):
		return self.coords