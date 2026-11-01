class BadWeekday(Exception):
    WEEKDAYS = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday"
    ]

    def __init__(self, message=""):
        super().__init__(
            "Must be one of these: Monday, Tuesday, Wednesday, Thursday, or Friday. "
            + message
        )
    