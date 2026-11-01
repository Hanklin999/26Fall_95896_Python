"""
Defines a simplified version of the Note classes used in a previous lab.
A Note stores a name, body, and noteNumber and serves as the parent class for all note types.
"""

class Note: 
    __noteCount = 0 
    __FOOTER = "***** Powered by Make-A-Note *****" 
    
    def __init__(self, name, body): 
        self.__name = name 
        self.__body = body 
        Note.__noteCount += 1 # Increment how many notes have been created
        self.__noteNumber = Note.__noteCount # Set this note's id to the current count

    def setName(self, name):
        self.__name = name
    
    def getName(self):
        return self.__name

    def setBody(self, body):
        self.__body = body
    
    def getBody(self):
        return self.__body
    
    def getNumber(self):
        return self.__noteNumber

    def __str__(self): 
        return (f"Note # {self.__noteNumber}\n" 
                f"Name: {self.__name}\n" 
                f"Body: {self.__body}\n" 
                f"{self.__FOOTER}" )
    
