"""
Driver program for the Make A Note application.
Provides menu for creating and displaying notes and sub-menus for creating and displaying different types of notes.
"""

# imports here if needed
from Memo import Memo
from NoteCollection import NoteCollection
from TimedMemo import TimedMemo
from PoliteTimedMemo import PoliteTimedMemo



# String values for the main menu - title first
mainMenu = [ "Main Menu", 
                "Create a new Note", 
                "Display existing Note(s)", 
                "Quit" ] 

# String values for the create sub-menu - title first
createMenu = [ "Note Creation", 
                "Create a Memo", 
                "Create a Timed Memo", 
                "Create a Polite Memo", 
                "Return to previous menu" ] 

# String values for the display sub-menu - title first
displayMenu = [ "Display Options", 
                "Display all Notes", 
                "Display Note by Number", 
                "Display Notes by Name", 
                "Return to previous menu" ] 


def getMenuChoice(menu):
    """ Displays menu and prompts the user for a choice. """
    
    print("\n" + menu[0])

    # Display the menu, whatever its size is
    for i in range(1, len(menu)):
        print(f"{i}. {menu[i]}")

    choice = int(input("Enter your choice: "))
    return choice

def main(): 
    # Create an empty NoteCollection 
    noteCollection = NoteCollection() 

    # Loop until the user chooses quit
    choice = 0
    while choice != 3:
        # Get the main menu choice
        choice = getMenuChoice(mainMenu)

        # Create a new Note
        if choice == 1:
            subchoice = 0
            while subchoice != 4:
                # Get the create submenu choice
                subchoice = getMenuChoice(createMenu)

                if subchoice in [1, 2, 3]:
                    name = input("Enter memo name: ")
                    body = input("Enter memo body: ")
                    fromPerson = input("Enter who this is from: ")
                    toPerson = input("Enter who this is to: ")

                # Create a Memo
                if subchoice == 1:
                    # Your code here: create a Memo object and add it to the NoteCollection
                    memo = Memo(name, body, fromPerson, toPerson)
                    noteCollection.add(memo)

                # Create a TimedMemo
                elif subchoice == 2:
                    timedMemo = TimedMemo(name, body, fromPerson, toPerson)
                    noteCollection.add(timedMemo)


                # Create a PoliteTimedMemo
                elif subchoice == 3:
                    politeTimedMemo = PoliteTimedMemo(name, body, fromPerson, toPerson)
                    noteCollection.add(politeTimedMemo)

        # Display Notes
        elif choice == 2:
            subchoice = 0
            while subchoice != 4:

                # Get display submenu choice
                subchoice = getMenuChoice(displayMenu)

                # Display all notes
                if subchoice == 1:
                    notes = noteCollection.getAllNotes()
                    for note in notes:
                        print(note)

                # Display a note by number
                elif subchoice == 2:
                    number = int(input("Enter note number: "))
                    note = noteCollection.getNoteByNumber(number)
                
                    if note is not None:
                        print(note)
                    else:
                        print("None found")
                    


                # Display a note by name
                elif subchoice == 3:
                    name = input("Enter note name: ")
                    notes = noteCollection.getNoteByName(name)
                
                    if len(notes) > 0:
                        for note in notes:
                            print(note)
                    else:
                        print("None found")

                # Quit
                elif subchoice == 4:
                    print("Returning to main menu")

if __name__ == "__main__": 
    main()
