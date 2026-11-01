from abc import ABC, abstractmethod

class Student(ABC):
    id = 0

    def __init__(self, name, gpa):
        self._name = name
        self._gpa = gpa
        self._id = self.setID()

    def setID(self):
        Student.id += 1
        return Student.id

    @abstractmethod
    def complain(self):
        pass

    def __str__(self):
        return (
            f"Name: {self._name}\n"
            f"gpa: {self._gpa}\n"
            f"id: {self._id}"
        )