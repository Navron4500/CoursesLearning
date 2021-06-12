

class Vehicle:

	def __init__(self,color,maxSpeed):
		self.color = color
		self._maxSpeed = maxSpeed

	@classmethod
	def getMaxSpeed(cls):
		return 15

	def setMaxSpeed(self,maxSpeed):
		self._maxSpeed = maxSpeed

	def print(self):
		print("Color :" ,self.color)
		print("MaxSpeed :",self._maxSpeed)

class Car(Vehicle):

	def __init__(self,color,maxSpeed,numGears,isConvertible):

		super().__init__(color,maxSpeed)
		self.numGears = numGears
		self.isConvertible = isConvertible

	def print(self):
		# super().print()
		print("Color :" ,self.color)
		print("MaxSpeed :",self._maxSpeed)
		print("NumGears :",self.numGears)
		print("IsConvertible :", self.isConvertible)


# c = Car("red",15,3,False)
# c.print()
#print()
v = Vehicle("red",18)
v.print()
print()
v._maxSpeed = 19
get = v.getMaxSpeed()
print(get)