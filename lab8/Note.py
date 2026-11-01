"""
Defines the Note class used in the Make A Note application.
A Note stores a name and body and serves as the parent class for all note types.
"""

class Note: 
    noteCount = 0 
    FOOTER = "***** Powered by Make-A-Note *****" 
    
    
    
    
    def __init__(self, name, body): 
        self.name = name 
        self.body = body 
        Note.noteCount += 1 # Increment how many notes have been created
        self.noteNumber = Note.noteCount # Set this note's id to the current count

    def __str__(self): 
        return (f"Name: {self.name}\n" 
                f"Body: {self.body}\n" 
                f"Note# {self.noteNumber}\n" 
                f"{self.FOOTER}" )
    
    
    def getNoteNumber(self):
        return self.noteNumber
    
    def getName(self):
        return self.name
        
