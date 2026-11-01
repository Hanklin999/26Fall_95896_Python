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