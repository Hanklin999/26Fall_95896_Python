# 2026 Fall 95896
# Student: Hank Lin
# Andrew ID: hanklin

'''
1. Create a project named Lab6. For each class specification listed in the problems 2-5, create the class in the
parent folder. In addition to any other methods mentioned below, each class should have the following methods:
- constructor using default arguments
- getters and setters for all member data
- a __str__ method. This should return a formatted string containing the member data with labels, such as
"minimum: " + minimum, for the minimum data field in Sensor.
'''


'''
2. Create a class called Sensor.
Data: minimum, maximum, currentValue, interval, location, type, id
Method:
- trip(): This method returns true if the currentValue is less than minimum or greater than maximum
and returns false otherwise
'''

class Sensor:

    def __init__(
            self,
            minimum=0.0,
            maximum=0.0,
            currentValue=0.0,
            interval=0.0,
            location="",
            type="",
            id=0
        ):
            self.__minimum = minimum
            self.__maximum = maximum
            self.__currentValue = currentValue
            self.__interval = interval
            self.__location = location
            self.__type = type
            self.__id = id

    def getMinimum(self):
        return self.__minimum

    def setMinimum(self, minimum):
        self.__minimum = minimum

    def getMaximum(self):
        return self.__maximum

    def setMaximum(self, maximum):
        self.__maximum = maximum


    def getCurrentValue(self):
        return self.__currentValue

    def setCurrentValue(self, currentValue):
        self.__currentValue = currentValue
        
    def getInterval(self):
        return self.__interval

    def setInterval(self, interval):
        self.__interval = interval
        
    def getLocation (self):
        return self.__location 

    def setLocation (self, location ):
        self.__location  = location     
              
    def getType (self):
        return self.__type 

    def setType (self, type ):
        self.__type  = type 
        
    def getId (self):
        return self.__id 

    def setId (self, id ):
        self.__id  = id

    def __str__(self):
        return (
            "minimum: " + str(self.__minimum)
            + ", maximum: " + str(self.__maximum)
            + ", currentValue: " + str(self.__currentValue)
            + ", interval: " + str(self.__interval)
            + ", location: " + self.__location
            + ", type: " + self.__type
            + ", id: " + str(self.__id)
        )
    
    
    def trip(self):
        if (self.__currentValue < self.__minimum or self.__currentValue > self.__maximum):
            return True
        else:
            return False
'''
temperature = Sensor(
    0.0, 120.0, 68.0, 1.0,
    "kitchen", "temperature", 1)

print(temperature)
print(temperature.trip())

temperature.setCurrentValue(150.0)
print(temperature.trip())
'''

#%%
'''
3. Create a class called Device.
Data:
- type
- location
- id
Method:
- actuate(): This method prints formatted data ( __str__(self) method) in all caps.
'''

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
#%%
'''
Create a class called Alarm.
Data:
- message
- id
Method:
- soundTheAlarm(): This method displays the message and simulates a 911 call'''


class Alarm:
    def __init__(
            self,
            message="",
            id=0
        ):
        
            self.__message = message
            self.__id = id

            
    def getMessage(self):
        return self.__message

    def setMessage(self, message):
        self.__message = message

    def getId(self):
        return self.__id

    def setId(self, id):
        self.__id = id     

    # formatted representation
    def __str__(self):
        return (
            "message: " + str(self.__message)
            + ", id: " + str(self.__id)
        )

    # special method
    def soundTheAlarm(self):
        print(self.__message)
        print("Calling 911...")



'''
# test Alarm

bell = Alarm("Ding! Ding!", 1)


bell.setMessage("Warning!")
bell.setId(2)

print(bell.getMessage())
print(bell.getId())
print(bell)

bell.soundTheAlarm()
'''
#%%
'''
6. Create a class called Lab6. This will be the driver for your program. Do the following in the main method:
- create a Sensor object named temperature with data (in the order listed above): 0.0, 120.0, 68.0, 1.0,
kitchen, temperature, id 1
- create a Device object named extinguisher with data fire extinguisher, kitchen, 1
- create a Room object named kitchen with data 12.0, 15.0, kitchen, 1
- create an Alarm object named bell with data "Ding! Ding!", 1
- display all the objects by printing the object instance (in Python, the __str__ method is implicitly called)
'''

'''
7. Continue with main:
Display a welcome message and display the Room information again.
Create a loop that asks the user if they want to enter a new value, Y or N; loop until they enter N. In the loop,
show the current kitchen temperature and prompt the user enter a new temperature; use it to reset the
temperature object's currentValue, then see if that tripped the sensor – if it did, actuate the extinguisher, then
sound the alarm; then reset the kitchen temperature back to what it was.'''


class Lab6:
    def main(self):
        temperature = Sensor( 0.0, 120.0, 68.0, 1.0,"kitchen", "temperature", id = 1)
        
        extinguisher = Device("fire extinguisher", "kitchen", 1)
        
        kitchen = Room(12.0, 15.0, "kitchen", 1)
        
        bell = Alarm("Ding! Ding!", 1)
        
        print(temperature)
        print(extinguisher)
        print(kitchen)
        print(bell)
        
        
        
        print("Welcome!")
        print(kitchen)
        
        WelcomeQuestion = input("Enter a new value? Y or N: ")
        
        while WelcomeQuestion != "N":
            print("Current temperature:", temperature.getCurrentValue())
        
            oldTemp = temperature.getCurrentValue()
            
            
            NewTemp = float(input("Setup a new Temperature:"))
            temperature.setCurrentValue(NewTemp)
            
            if temperature.trip() == True:
                extinguisher.actuate()
                bell.soundTheAlarm()
                
                
            temperature.setCurrentValue(oldTemp)
            
            WelcomeQuestion = input("Enter a new value? Y or N: ")
            
        # a. Sensor and Room are mainly responsible for storing data. Sensor stores the current value.
        #    Device and Alarm are responsible for performing actions. Alarm can sound the alarm.
        # b. Keep the program more structurized and organized, and also easier to read and reuse.
        # c. When a new temperature is assigned to the Sensor, trip() checks whether it is outside the minimum and maximum range.
        #    If the sensor is tripped, the extinguisher Device is actuated, then the bell Alarm displays its message and simulates a 911 call.
        
                
                

            
        
        
        
if __name__ == "__main__":
    app = Lab6()
    app.main()



















