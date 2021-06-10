
class Student:

	passingPercentage = 40

	def __init__(self,name,age=15,percentage=80):
		self.name = name
		self.age = age
		self.percentage = percentage

	def studentDetails(self):
		print("Name = ", self.name)
		print("Age =" , self.age)
		print("Percentage = ", self.percentage)
		pass

	def isPassed(self):
		if self.percentage > Student.passingPercentage:
			print("Student is passed")
		else:
			print("Student is not passed")

	@staticmethod
	def welcomeToSchool():
		print("Hey! Welcome To School")

s1 = Student("Parikh")

# s1.isPassed()
# s2 = Student("Varun",26,90)
# s1.studentDetails()
# s2.studentDetails()
# s1.studentDetails()
# Student.studentDetails(s1)
# s1.isPassed()
# s1.welcomeToSchool()


#class_name.function(object_name)