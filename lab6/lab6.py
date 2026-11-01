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




from sensor import Sensor
from device import Device
from room import Room
from alarm import Alarm



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
