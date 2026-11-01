from student import Student

class Undergraduate(Student):
    def __init__(self, name, gpa, major):
        super().__init__(name, gpa)
        self._major = major

    def complain(self):
        return "Not enough beer"

    def __str__(self):
        return (
            super().__str__()
            + f"\nMajor: {self._major}"
        )