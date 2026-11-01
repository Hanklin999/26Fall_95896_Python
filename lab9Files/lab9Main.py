# Main program for Lab 9

students = []

# Problem 1:
# Replace these object creations with calls to the Factory Method class
from StudentCreator import StudentCreator

'''
u = StudentCreator.createRecord(
    "Undergraduate",
    "Hank",
    3.8,
    "Information Systems"
)

g = StudentCreator.createRecord(
    "Graduate",
    "Amy",
    3.9,
    "AI Capstone"
)

students.append(u)
students.append(g)
'''

# Problem 2:
# Display each student and their complaint

for student in students:
    print(student)
    print(student.complain())
    
    
    
# Problem 3:
# Create a Schedule object
# Register every student for Python
# Display the schedule
from scheduleProxy import ScheduleProxy
schedule = ScheduleProxy()

for student in students:
    print(student._name)
    schedule.register("Python")
schedule.display( )


# Problem 4:
# Replace Schedule with ScheduleProxy
# Complete ScheduleProxy so that it logs actions

