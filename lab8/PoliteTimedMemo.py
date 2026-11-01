
from TimedMemo import TimedMemo



class PoliteTimedMemo(TimedMemo):
    
    DEFAULT_GREETING = "Dear"
    DEFAULT_CLOSING = "Yours truly,"

    def __init__(self, name, body, fromPerson, toPerson):
        super().__init__(name, body, fromPerson, toPerson)

    
    def __str__(self):
        return (f"Date: {self.today}\n"
                f"Name: {self.name}\n"
                f"{self.DEFAULT_GREETING} {self.toPerson}:\n"
                f"{self.body}\n"
                f"{self.DEFAULT_CLOSING}\n"
                f"{self.fromPerson}\n"
                f"Note#: {self.noteNumber}\n"
                f"{self.FOOTER}")
