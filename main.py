# 2026 Fall, 95896-A
# Student Name: Hank Lin
# Andrew ID: hanklin


# Name: Hank Lin
# Andrew ID: hanklin

from hanklin_hw2 import SharkAttackManager, SharkAttack


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
                print("Add a new attack data")
                caseNumber = input("Case Number: ")
                year = input("Year: ")
                country = input("Country: ")
                activity = input("Activity: ")
                victimName = input("Victim Name: ")
                fatal = input("Fatal (Y/N): ")
                species = input("Species: ")
                age = input("Age: ")
            
                newRecord = SharkAttack(
                    caseNumber=caseNumber,
                    year=year,
                    country=country,
                    activity=activity,
                    victimName=victimName,
                    fatal=fatal,
                    species=species,
                    age=int(age) if age.strip().isdigit() else None
                )
            
                manager.addAttack(newRecord)
            


            case _:
                print("Invalid Choice")
            
            

        
if __name__ == "__main__":
    main()