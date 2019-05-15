# li = [-6, -5, -4, 1, 2, 3]

# s_li = sorted(li, key=lambda a: abs(a + 4))
# # s_li = sorted(li, cmp=lambda a: abs(a + 4))

# print(s_li)

from operator import attrgetter


class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return "({},{},${})".format(self.name, self.age, self.salary)


e1 = Employee("Carl", 37, 20000)
e2 = Employee("Sarah", 24, 50000)
e3 = Employee("John", 45, 100000)

employees = [e1, e2, e3]

# s_employees = sorted(employees, key=lambda e: e.salary)
s_employees = sorted(employees, key=attrgetter("age"))

print(s_employees)
