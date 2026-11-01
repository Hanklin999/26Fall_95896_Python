from student import Student

class Graduate(Student):
    def __init__(self, name, gpa, capstone):
        super().__init__(name, gpa)
        self._capstone = capstone

    def complain(self):
        return "Why did I take Python?"

    def __str__(self):
        return (
            super().__str__()
            + f"\nCapstone: {self._capstone}"
        )