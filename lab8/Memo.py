'''
Memo: adds the “From” and “To” fields
'''

# Memo.py
from Note import Note

class Memo(Note):
    def __init__(self, name, body, fromPerson, toPerson):
        super().__init__(name, body)
        self.fromPerson = fromPerson
        self.toPerson = toPerson

    def __str__(self):
        return (
            f"From: {self.fromPerson}\n"
            f"To: {self.toPerson}\n"
            + super().__str__()
        )
    
#Note 本來就有: name, body, noteNumber
#Memo 要自己創出: 
    # fromPerson: String, who wrote the memo
    # toPerson: String, who the memo is for
    