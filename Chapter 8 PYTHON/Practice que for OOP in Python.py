# QUE: Define a Circle class to create with radius r using the constructor.
#      Define an Area() method of the class which class which calculates the area of the circle.
#      Define a Perimeter() method of the class which allows you to calculate the perimeter if the circle.

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return (22/7) * self.radius ** 2
    
    def perimeter(self):
        return 2 * (22/7) * self.radius
    
c1 = Circle(21)
print(c1.area())
print(c1.perimeter())


# QUE: Define a Employee class with attributes role, department & salary. This class also has a showDetails() method.
#      Create an Engineer class that inherits properties from Employee & has additional attributes : name & age.

class Employee:
    def __init__(self, role, dept, salary):
        self.role = role
        self.dept = dept
        self.salary = salary

    def showDetails(self):
        print("role =", self.role,"\ndept =",self.dept, "\nsalary =", self.salary)

class Engineer(Employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("Engineer", "IT", "75,000")

engg1 = Engineer("Rudra", "23")
engg1.showDetails()


# QUE: Create a class Order which stores item & its price.
#      Use Dunder function '__gt__()' to convey that:
#           order1 > order2 if price of order1 > price of order2

class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price

    def __gt__(self, odr2):
        return self.price > odr2.price 

odr1 = Order("chips", 20)
odr2 = Order("tea", 15)

print(odr1 > odr2)