class Schedule:
    COURSE_LIST = [
        "Statistics",
        "Python",
        "BIDA Capstone"
    ]

    def __init__(self):
        self._courses = {}

        for course in Schedule.COURSE_LIST:
            self._courses[course] = 0

    def register(self, course):
        if course in self._courses:
            self._courses[course] += 1

    def display(self):
        print("Course - Enrollment")

        for course in Schedule.COURSE_LIST:
            print(f"{course}: {self._courses[course]}")