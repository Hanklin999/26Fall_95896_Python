from StudentCreator import StudentCreator
from undergraduate import Undergraduate
from graduate import Graduate
from schedule import Schedule
from scheduleProxy import ScheduleProxy


# Test Factory
u = StudentCreator.createRecord(
    "Undergraduate", "Alice", 3.5, "Statistics"
)

g = StudentCreator.createRecord(
    "Graduate", "Bob", 3.8, "BIDA Project"
)

assert isinstance(u, Undergraduate)
assert isinstance(g, Graduate)

print("Factory test passed")


# Test __str__ and complain
print(u)
print(u.complain())

print(g)
print(g.complain())

print("Student methods test passed")


# Test Schedule
schedule = Schedule()

schedule.register("Python")
schedule.register("Python")

assert schedule._courses["Python"] == 2

schedule.display()

print("Schedule test passed")


# Test Proxy
proxy = ScheduleProxy()

proxy.register("Python")

assert proxy._schedule._courses["Python"] == 1

proxy.display()

print("Proxy test passed")