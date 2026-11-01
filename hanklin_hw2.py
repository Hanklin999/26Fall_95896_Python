# 2026 Fall, 95896-A
# Student Name: Hank Lin
# Andrew ID: hanklin

# Problem 1

# 1. Read line

import csv

attackData = []

with open("shark_attacks.csv", "r") as file:

    headers = file.readline().strip().split(",")

    reader = csv.reader(file)

    for row in reader:
        attackData.append(row)

countryWidth = len("FEDERATED STATES OF MICRONESIA")
        
print(
    f"{headers[0].title():<20}"
    f"{headers[2].title():<10}"
    f"{headers[4].title():<{countryWidth}}"
    f"{headers[7].title():<35}"
    f"{headers[12].title():<15}"
)


# display the first 25 rows in a formatted table

for row in attackData[:25]:
    print(
        f"{row[0]:<20}"
        f"{row[2]:<10}"
        f"{row[4]:<{countryWidth}}"
        f"{row[7]:<35}"
        f"{row[12]:<15}"
    )


# 2. Write the functions

def isFatalAttack(fatalValue: str) -> bool:
    return fatalValue == "Y"
    
def ageCategory(age: int) -> str:
    if age < 13:
        return "Child"
    elif age < 18:
        return "Teen"
    elif age < 65:
        return "Adult"
    else:
        return "Senior"
    
def displayAttacksByCountry(country: str) -> None:
    count = 0

    for row in attackData:
        if row[4].strip().upper() == country.strip().upper():
            print(
                f"{row[0]:<20}"
                f"{row[2]:<10}"
                f"{row[4]:<35}"
                f"{row[7]:<35}"
                f"{row[12]:<15}"
            )
            count += 1

    print(f"Total attacks in {country}: {count}")
    
    
# 3. Create Variables
# a. Store the results in a dictionary named countryCount

countryCount = {}

for row in attackData:
    country = row[4]
    
    if country in countryCount:
        countryCount[country] += 1
    else:
        countryCount[country] = 1

print(countryCount)
    
# b. activitySet

activitySet = set()

for row in attackData:
    activity = row[7]
    
    activitySet.add(activity)

activityList = sorted(activitySet)

print(activityList)


# c. activityVicitims

activityVicitims = {}

for row in attackData:
    activity = row[7]
    victim_name = row[8]
    
    if activity in activityVicitims:
        activityVicitims[activity].append(victim_name)
    else:
        activityVicitims[activity] = [victim_name]

print(activityVicitims)


    
# 4. parent class named Attack

class Attack:
    
    def __init__(self, caseNumber, year, country):
        self.caseNumber = caseNumber
        self.year = year
        self.country = country
        
    def __str__(self):
        return (
            f"Case Number: {self.caseNumber}, "
            f"Year: {self.year}, "
            f"Country: {self.country}"
        )

# child class

class SharkAttack(Attack):
    
    def __init__(self,  caseNumber, year, country, 
                 activity, victimName, fatal, species, age = None):
        
        super().__init__(caseNumber, year, country)
        
        self.activity = activity
        self.victimName =victimName
        self.fatal = fatal
        self.species = species
        self.age = age
        
        
    def __str__(self):
        return(
            f"Case Number: {self.caseNumber}, "
            f"Year: {self.year}, "
            f"Country: {self.country}, "
            f"Activity: {self.activity}, "
            f"Victim: {self.victimName}, "
            f"Fatal: {self.fatal}, "
            f"Species: {self.species}"        
            )
        
# 5. SharkAttackManager

class SharkAttackManager:
    
    def __init__(self):
        self.attacks = []

    def readAttackFile(self, filename):
        # read shark attack records from CSV
        with open(filename) as file:
            reader = csv.reader(file)
            
            for row in reader:
                
                attack = SharkAttack(
                caseNumber=row[0],
                year=row[2],
                country=row[4],
                activity=row[7],
                victimName=row[8],
                fatal=row[12],
                species=row[14],
                age=int(row[10].strip()) if row[10].strip().isdigit() else None
            )
            
                self.addAttack(attack)
            
            
    def displayAllAttacks(self):
        # Display All attacks data
        for attack in self.attacks:
            print(attack)            
           
    def displayFatalAttacks(self):
        # Display All Fatal Attacks (isFatal = True)
        for attack in self.attacks:
            if isFatalAttack(attack.fatal):
                print(attack)
                
    def displayAttacksByCountry(self, country):
        # Display Attacks from specific country
        count = 0
        for attack in self.attacks:
            
            if attack.country.strip().lower() == country.strip().lower():
                print(attack)
                count += 1
                
        print(f"Total attacks in {country}: {count}")
        
    def getMostCommonActivity(self):
        # Get Most Common Activity
        activityCount = {}
    
        for attack in self.attacks:   
            activity = attack.activity
    
            if activity in activityCount:
                activityCount[activity] += 1
            else:
                activityCount[activity] = 1
        return max(activityCount, key=activityCount.get)
                
    def getAverageVictimAge(self):
        # Get Average Victim Age
        ttlAge = 0
        ttlVictim = 0
        
        for attack in self.attacks:
            if attack.age is not None:
                ttlAge += attack.age
                ttlVictim += 1
        if ttlVictim == 0:
                return None
            
        return ttlAge / ttlVictim
    
    def addAttack(self, attack):
        # add new record
        self.attacks.append(attack)
    



def main():
    manager = SharkAttackManager()
    
    manager.readAttackFile("shark_attacks.csv")
    
    while True:
        
        print("0. Quit")
        print("1. Display all attacks")
        print("2. Display fatal attacks")
        print("3. Search by country")
        print("4. Display most common activity")
        print("5. Display average victim age")
        print("6. Add new attack")
        
        choice = int(input("Please input your next step:"))
        
        match choice:
            case 0:
                break
            case 1:
                manager.displayAllAttacks()
            case 2:
                manager.displayFatalAttacks()
            case 3:
                country = input("Enter Country:")
                manager.displayAttacksByCountry(country)
            case 4:
                activity = manager.getMostCommonActivity()
                print(f"Most Common Activity: {activity}")
            case 5:
                age = manager.getAverageVictimAge()
                print(f"Average victim age: {age:.2f}")
            case 6:
                newRecord = input("Add a new attack data")
                manager.addAttack(newRecord)
            case _:
                print("Invalid Choice")
            
            

        
if __name__ == "__main__":
    main()
    
        
# 6.

# a.

q6a = lambda x: x ** 2

print(q6a(5))
print(q6a(10))

# b.

q6b = lambda x:str(x) * 3

print(q6b(5))
print(q6b("dog"))

# c.

q6c = lambda x, y : x + y

print(q6c(5,10))
print(q6c(2.1, -1.5))

# d.
q6d = lambda x, y : (x + y)/2

print(q6d(5,10))
print(q6d(2.1, -1.5))

# e.
q6e = lambda x : list(range(0,x))

print(q6e(5))
print(q6e(10))

# f.
q6f = lambda x, y: list(range(x,y))

print(q6f(5,10))
print(q6f(2,3))