#%%
'''
4. Create a class called Room.
Data:
- length
- width
- name
- id
Method:
- getArea(): This method computes and returns the room’s area
'''


class Room:
    def __init__(
            self,
            length=0.0,
            width=0.0,
            name="",
            id=0
        ):
        
            self.__length = length
            self.__width = width
            self.__name = name
            self.__id = id
            
    def getLength(self):
        return self.__length

    def setLength(self, length):
        self.__length = length

    def getWidth(self):
        return self.__width

    def setWidth(self, width):
        self.__width = width


    def getName(self):
        return self.__name

    def setName(self, name):
        self.__name = name

    def getId(self):
        return self.__id

    def setId(self, id):
        self.__id = id        

    # formatted representation
    def __str__(self):
        return (
            "length: " + str(self.__length)
            + ", width: " + str(self.__width)
            + ", name: " + self.__name
            + ", id: " + str(self.__id)
        )



    # Q3 special method
    def getArea(self):
        return float(self.__length * self.__width)

'''
house = Room(12.3, 5.0, "hamerschlag",4500)

print(house)

house.setLength(45000)
print(house)

house.getArea()


'''