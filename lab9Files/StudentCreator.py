
from undergraduate import Undergraduate
from graduate import Graduate


class StudentCreator():
        
    @staticmethod
    def createRecord(kindOfStudent, name, gpa, otherThing):
        if kindOfStudent == "Undergraduate":
            return Undergraduate(name, gpa, otherThing)
            
        elif kindOfStudent == "Graduate":
            return Graduate(name, gpa, otherThing)
        

        






