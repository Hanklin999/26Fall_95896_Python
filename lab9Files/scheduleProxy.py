from schedule import Schedule

class ScheduleProxy:
    def __init__(self):
        self._schedule = Schedule()

    def register(self, course):
        print(f"Recording to log: registering {course}")
        self._schedule.register(course)

    def display(self):
        print("Recording to log: displaying enrollment status")
        self._schedule.display()