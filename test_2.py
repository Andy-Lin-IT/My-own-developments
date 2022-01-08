class Person:
	piople_count = 0
	some_num = 123

	def __init__(self, name, sername, place_of_birth, year_of_birth):
		self.name = name
		self.sername = sername
		self.place_of_birth = place_of_birth
		self.year_of_birth = year_of_birth

		Person.piople_count += 1

	def print_info(self):
		print(f"Name: {self.name}, Surname: {self.sername}, Plase of birth: {self.place_of_birth}, Year of birth: {self.year_of_birth}, People count: {Person.piople_count}")

	def get_age(self, current_year):
		return current_year - self.year_of_birth

p1 = Person('Jack','Mile', 'New York', 1979)
p1.print_info()

print(p1.get_age(2022))

print(Person.some_num)

'''class Circle:
	PI = 3.14

	def __init__(self,radius):
		self.radius = radius

	def get_perimeter(self):
		return self.radius * 2 * self.PI

	def get_area(self):
		return self .PI * self.radius **2


c1 = Circle(5)
print(c1.get_perimeter())
print(c1.get_area())


c2 = Circle(7)
print(c2.get_area())
print(c2.get_perimeter())'''


class DB:
	dbConection = 0

	def write_data(self):
		pass