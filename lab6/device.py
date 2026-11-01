
class Device:
    def __init__(
            self,
            type="",
            location="",
            id=0
        ):
        
            self.__type = type
            self.__location = location
            self.__id = id
            
    def getType(self):
        return self.__type

    def setType(self, type):
        self.__type = type

    def getLocation(self):
        return self.__location

    def setLocation(self, location):
        self.__location = location


    def getId(self):
        return self.__id

    def setId(self, id):
        self.__id = id
        

    # formatted representation
    def __str__(self):
        return (
            "type: " + str(self.__type)
            + ", location: " + str(self.__location)
            + ", id: " + str(self.__id)
        )

    # Q3 special method
    def actuate(self):
        print(self.__str__().upper())

'''
smartphone = Device("Smartphone", "Pittsburgh", 4500)

print(smartphone)

smartphone.setLocation("NewYork")
print(smartphone)

smartphone.actuate()
'''