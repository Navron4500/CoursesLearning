
class Student:

	__passingPercentage = 40

	def __init__(self,name,age=15,percentage=80):
		self.__name = name
		self.age = age
		self.percentage = percentage

	def studentDetails(self):
		print("Name = ", self.__name)
		print("Age =" , self.age)
		print("Percentage = ", self.percentage)
		

	def isPassed(self):
		if self.percentage > Student.passingPercentage:
			print("Student is passed")
		else:
			print("Student is not passed")

	@staticmethod
	def welcomeToSchool():
		print("Hey! Welcome To School")

s1 = Student("Parikh")
#print(s1.__name)
#print(s1.age)
s1.age = 20
print(Student._Student__passingPercentage)
s1.studentDetails()
# s1.name = "Ankush"
# s1.age = 20
# print(s1.name)
# print(s1.age)
#s1.studentDetails()
# s1.isPassed()
# s2 = Student("Varun",26,90)
# s1.studentDetails()
# s2.studentDetails()
# s1.studentDetails()
# Student.studentDetails(s1)
# s1.isPassed()
# s1.welcomeToSchool()


#class_name.function(object_name)