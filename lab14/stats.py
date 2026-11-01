"""
Keeps delivery stats for every robot.

Each robot gets a dict of {"parcels", "total_time", "running_time"}.
This object is shared by the warehouse and every robot thread, so the
three methods below *must* be made thread-safe using self._lock.
"""
import threading


class Stats:

    def __init__(self, num_robots):
        self._lock = threading.Lock()
        self._data = {
            robot_id: {"parcels": 0, "total_time": 0, "running_time": 0}
            for robot_id in range(num_robots)
        }

    # YOUR CODE HERE: three thread-safe methods
    # Protect each method's body with "with self._lock:", the same
    # pattern used in SharedCounter.

    def record_delivery(self, robot_id, delivery_time):
        # increments this robot's parcel count by one and adds
        # delivery_time to this robot's total delivery time
        pass

    def record_running_time(self, robot_id, elapsed_ms):
        # sets this robot's running time
        pass

    def for_robot(self, robot_id):
        # returns a COPY of this robot's stats dict, so the caller
        # can't mutate our internal state directly
        pass
