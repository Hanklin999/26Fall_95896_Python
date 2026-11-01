# 2026 Fall 95896
# Student: Hank Lin
# Andrew ID: hanklin


'''
1. Create a project named Lab7 with a driver file named Lab7.py. Copy these classes from Lab6: Sensor,
Device, Room, and Alarm.
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

    # special method
    def getArea(self):
        return float(self.__length * self.__width)


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

#%%
'''
2. Create the following collection classes. 
Each class will contain a Python list that stores objects of the specified type.
Each class should include:
    - A default constructor that initializes an empty list.
    - add(item): Adds an object to the list.
    - display(): Displays each object in the list by looping through the list and printing each object.
Classes:
    - SensorCollection: contains Sensor objects, named sensors.
    - AlarmCollection: contains Alarm objects, named alarms.
'''    




class SensorCollection:
    def __init__(self):
        self.__sensors = []
        
    def add(self, item):
        self.__sensors.append(item)

    def display(self):
        for item in self.__sensors:
            print(item)

class AlarmCollection:
    def __init__(self):
        self.__alarms = []
        
    def add(self, item):
        self.__alarms.append(item)
        
    def display(self):
        for item in self.__alarms:
            print(item)



# sensorCollection = SensorCollection()

# sensor1 = Sensor()
# sensor2 = Sensor()

# sensorCollection.add(sensor1)
# sensorCollection.add(sensor2)

# sensorCollection.display()


#%%
'''
3. Modify the Room class to include the following member data: SensorCollection and
AlarmCollection. So Room should contain:
- A SensorCollection object
- An AlarmCollection object
- One Device object
- plus length, width, and id from previously

Add the following methods to Room:
- addSensor(sensor): Adds a Sensor object to the room's SensorCollection.
- addAlarm(alarm): Adds an Alarm object to the room's AlarmCollection.
- addDevice(device): Assigns the Device object to the room.
- display()
- Prints the Room information.
- Prints the Device information (if one exists).
- Calls display() on the SensorCollection and on the AlarmCollection.
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
            
            self.__sensorCollection = SensorCollection()
            self.__alarmCollection = AlarmCollection()
            self.__device = None
        
    def addSensor(self, sensor):
        self.__sensorCollection.add(sensor)

    def addAlarm(self, alarm):
        self.__alarmCollection.add(alarm)
        
    def addDevice(self, device):
        self.__device = device
        
        
    def display(self):
        print(self)
        
        if self.__device is not None:
            print(self.__device)

        self.__sensorCollection.display()
        self.__alarmCollection.display()

        


    def __str__(self):
        return (
            "length: " + str(self.__length)
            + ", width: " + str(self.__width)
            + ", name: " + self.__name
            + ", id: " + str(self.__id)
        )








#%%


class Lab7:
    def main(self):
        
        room1 = Room(12.0, 15.0, "kitchen", "#1")
        
        
        # Qˋ 
        extinguisher = Device("fire extinguisher","kitchen","#1")
        room1.addDevice(extinguisher)

        for i in range (0,5):
            temps = Sensor( 0.0, 120.0, 68.0, 1.0,"kitchen", "temperature", i + 1)
            
            room1.addSensor(temps)
            
        for i in range (0,3):
            tempb = Alarm("Ding! Ding!", i + 1)
            
            room1.addAlarm(tempb)
            
        room1.display()
        
        
        chemicalFoamer = Device( "chemical foamer", "kitchen", 2)
        
        
        

        room1.addDevice(chemicalFoamer)

        room1.display()
        
        
        
if __name__ == "__main__":
    app = Lab7()
    app.main()
