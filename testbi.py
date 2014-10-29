class Bicycle(object):
	def __init__(self,bike):
		self.bike = bike
	def create_bikes(self):
	    global bikes
	    bikes = {}
	    for i in range(7):
	    	m = raw_input("Please input a model: ")
	    	w = raw_input("Please input a weight for the bike: ")
	    	c = raw_input("Please input a cost")
	    	if bikes.has_key(m):
	    		print 'Please input a different model'
	    	else:
	    		bikes[m] = w
	    		bikes[m] = c
	    return bikes
	def bike_inv(create_bikes):
		for key in bikes:
		  print key,bikes[key]
class Bike_Shop(Bicycle):
	def __init__(self,name):
		self.name = name
	def bike_inv2(bikes):
		bikes2 = {}
		for key in range(5):
			bikes2[key] = bikes[key]
    		bikes2[key] = .20
        return bikes2
test1 = Bicycle("Daves Bike Shop")
test1.create_bikes()
test1.bike_inv()
test2 = Bike_Shop("Daves Place")
test2.bike_inv2()