# 2026 Fall 95896
# Student: Hank Lin
# Andrew ID: hanklin

# Problem 1

'''
The application you develop will keep track of university students’ attendance at events, track their hours, and
award points based on their participation. Test data (not all of it may be correct, see #1) will be stored in a data
file named “students.csv”, which is a CSV file of name,year,activity,time records. For each of the
functions described below, use type hints for the parameters and return values.

1. Write a function named parse_record( ) that accepts a single record string that contains a name,
university year, name of an event, and hours attended. The function verifies/ changes values so that:
• no fields are empty
• the year is a valid integer
• the year is between 1 and 4
• the number of hours is a float
• the number of hours is greater than 0
'''

def parse_record(record: str) -> dict | None:
    
    parts = record.strip().split(",")
    
    name    = parts[0].strip()
    year    = parts[1].strip()
    event   = parts[2].strip()
    hours    = parts[3].strip()
    
    if name == "" or year == "" or event == "" or hours == "":
        return None
    try:
        year = int(year)
    except:
        return None
    
    if year > 4 or year <1:
        return None
    try:
        hours = float(hours)
    except:
        return None
    
    if hours <= 0:
        return None

    student = {
        "name" : name,
        "year" : year,
        "event" : event,
        "hours"  : hours
        
        }
    
    return student


        
#%%

'''
2. Students earn participation points for events based on the number of hours they spend at an event.
Write a function named participation_points( ) that accepts the number of hours and returns the
appropriate number of points.
'''

def participation_points(hours: float) -> int:
    if hours <= 2.0 :
        return 10
    elif hours < 6.0 :
        return 20
    else:
        return 30

# testing        
#for student in students:
#    student["point"] = participation_points(student["hour"])
        
        
#%%

'''
3. The university classifies students based on their total participation hours. Write a function named
participation_standing( ) that accepts the hours a student worked, determines whether a student
belongs to one of the following participation levels, and returns that str value (for example, return “Silver” for 7
hours).'''

def participation_standing(hours: float) -> str:
    if hours < 6 :
        return "Bronze"
    elif hours < 11 :
        return "Silver"
    elif hours < 21 :
        return "Gold"
    else:
        return "Diamond"
 
#testing       
#for student in students:
#    student["standing"] = participation_standing(student["hour"])


#%%

'''
4. Create a function named run_menu( ) that accepts a list of student data and shows the following menu,
which allows a user to:
a. Search for a student by name.
b. Display all students who participated in a specific event.
c. Display all students in a specific participation standing.
d. Quit the program. 
'''


def run_menu(students: list) -> None:
    choice = ""

    while choice != "d":
        print("a. Search for a student by name")
        print("b. Display students in an event")
        print("c. Display students in a standing")
        print("d. Quit")

        choice = input("Enter choice: ").lower()
        
        
        if choice == "a":
            search_name = input("Enter Name:")
            for student in students:
                if student["name"] == search_name:
                    print(student)
                    
        elif choice == "b":
            search_event = input("Enter Event:")
            student_list_b = []
            
            for student in students:
                if student["event"] == search_event:
                    student_list_b.append(student)
            print(student_list_b)
        
        elif choice == "c":
            search_standing = input("Enter Standing:")
            student_list_c = []
            
                
            for student in students:
               if participation_standing(student["hours"]) == search_standing:
                    student_list_c.append(student)
            
            print(student_list_c)
            
        elif choice == "d":
            pass
        
        else:
            print("Invalid choice, please try again.")

#%%
'''
5. The university would like to recognize students who participated for at least 7 hours. 
Write a function named filter_high_participation( ) that takes a list of student data and returns a new list containing only
students who participated for 10 or more hours.

Solve this problem using a traditional loop. 
Then rewrite the solution using a list comprehension in a function named filter_high_participation_comprehension( ).
That is, you’ll have two functions that do exactly the same work but accomplish it in different ways.
'''

def filter_high_participation(students: list) -> list:
    high_participation_list = []
    for student in students:
        if student["hours"]>= 7:
            high_participation_list.append(student)
    
    return high_participation_list
    print(high_participation_list)
    
def filter_high_participation_comprehension(students: list ) -> list:
    return [student for student in students if student["hours"] >= 10]
    
    
#%%
'''
6. Write a function named get_names_loop( ) that takes the list of student data and create and returns a list
containing only student names. 
Solve the problem using a traditional loop. 
Then rewrite the solution to the same problem using map() and a lambda function; name this function get_names_map( ).

Repeat the process to create a list containing only participation hours – that is, two functions named
get_hours_loop( ) and get_hours_map( ).

'''

def get_names_loop(students: list) -> list:
    name_loop_list = []
    for student in students:
        name_loop_list.append(student["name"])
    return name_loop_list
    
def get_names_map(students: list) -> list:
    return list(map(lambda student:student["name"], students))
    



def get_hours_loop(students: list) -> list:
    hours_loop_list = []
    for student in students:
        hours_loop_list.append(student["hours"])
    return hours_loop_list
    
def get_hours_map(students: list) -> list:
    return list(map(lambda student:student["hours"], students))
    

#%%
'''
7. The university wants to know which events were the most popular. Write functions to compute the following
statistics:
• how many students participated in each event; name the function event_statistics( ), which
takes the student data as a parameter and returns a map of {event name:number of students} for each
event.
• the most popular event; name the function most_popular_event( ), which takes the map described
above as the parameter and returns the str name.
• the least popular event; name the function least_popular_event( ), similar to the above.
Your solution should not hardcode event names. It should work correctly even if new events are added later.
'''

def event_statistics(students:list) -> dict:
    event_dict = {}
    for student in students:
        event_name = student["event"]
        if event_name in event_dict:
            event_dict[event_name] +=1
        else:
            event_dict[event_name] =1
    
    return event_dict


def most_popular_event(students:list) -> str:
    popular_event = max(event_statistics(students), key = event_statistics(students).get)
    return popular_event

def least_popular_event(students:list) -> str:
    least_event = min(event_statistics(students), key = event_statistics(students).get)
    return least_event

#%%
'''8. Create a function named generate_report( ), which takes the student data as a parameter; it prints a
formatted report for every activity record.'''

def generate_report(students: list) -> None:
    for student in students:
        
        print(f"Student: {student['name']}")
        print(f"Year: {student['year']}")
        print(f"Event: {student['event']}")
        print(f"Hours: {student['hours']}")
        print(f"Points: {participation_points(student['hours'])}")
        print(f"Standing: {participation_standing(student['hours'])}")
        print()


    

#%%
''' 9. 
Write a main program that uses your functions to do the following:
- read the data file into a list of str values
- parses each record to create the student data list of dict’s
- gets and prints the statistics, most popular event, and least popular event
- generate the report
- run the interactive menu
'''


def main():

    # read data into a list of str values
    
    
    with open("students.csv", "r") as f:
        records = f.readlines()
            
    # parses each record to create student list dict
    students = []
    
    for record in records:
        student = parse_record(record)
        
        if student is not None:
            students.append(student)
    
    #gets and prints the statistics, most popular event, and least popular event
    
    
    event_statistics(students)
    print(event_statistics(students))
    
    most_popular_event(students)
    print(most_popular_event(students))
    least_popular_event(students)
    print(least_popular_event(students))
    
    
    #generate report
    generate_report(students)
    
    #run the interactive menu
    run_menu(students)
    
        
        
        
        
        
        
        
        
if __name__ == "__main__":
    main()