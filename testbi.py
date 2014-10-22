class Bicycle(object):
	def __init__(self,bike):
		self.bike = bike
	def create_bikes(self):
		if self.bike:
			bikes = {
	        "BMX1000": [10, 500],
	        "SPX1000": [20, 20],
	        "DMX1000": [15, 300],
	        "LMX1000": [30, 100],
	        "PMX1000": [40, 50],
	        "JMX1000": [35, 25],
	        "MMX1000": [5, 1000],
	        "MX1000": [10, 100],
	        "SMX1000": [30, 150],
	        "ZMX1000": [25, 350],
	        }
	        return bikes
class Bike_Shops(Bicycle):
	def __int__(self,name):
		self.name = name
	def get_bike_inv(create_bikes):
		bi_inv = {}
		for key in bikes:
			if bike:
				bi_inv[key] = bikes[key]
				bi_inv[key] = bikes[key] 
				bi_inv[key] = bikes[key] * .20 + bikes[key]
		print bi_inv
test1 = Bicycle(True)
test2 = Bike_Shops("Daves Bike Shop")
test2.get_bike_inv()


