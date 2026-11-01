'''
TimedMemo(name, body, from, to): constructor. Use
date.today() to get the current date. (make sure to
import the function usingfrom datetime import
date)
__str__(): override of Memo::toString()
'''


# TimedMemo.py
from Memo import Memo
from datetime import date

class TimedMemo(Memo):
    def __init__(self, name, body, fromPerson, toPerson):
        super().__init__(name, body, fromPerson, toPerson)
        self.today = date.today()

    def __str__(self):
        return (
            f"Date: {self.today}\n"
            + super().__str__()
        )