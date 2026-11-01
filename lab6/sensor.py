
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