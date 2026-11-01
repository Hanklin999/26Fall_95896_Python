"""
A robot just repeatedly grabs a parcel and "delivers" it.

This is written as a plain function (not a class) because the robot
doesn't really need to hold state between deliveries other than its
battery level, which we can just track with a local variable.
"""
import time


def deliver_parcels(robot_id, parcel_queue, stats, active_robots, print_lock):
    battery = 100
    start = time.time()

    while True:
        # YOUR CODE HERE
        # get a parcel from parcel_queue
        # if parcel.delivery_time is more than the remaining battery,
        #   put the parcel back on the queue and break out of the loop
        #   (it goes to the back -- it may or may not get delivered
        #   later, and it's not perfectly fair to that parcel, but
        #   that's the simulation)

        # YOUR CODE HERE
        # time.sleep() for the delivery (parcel.delivery_time / 100)
        #   to simulate the delivery
        # subtract delivery_time from battery

        with print_lock:
            # Don't change this, but *do* notice how it's synchronized
            print("\t\t\t" * robot_id + f"parcel #{parcel.id} in {parcel.delivery_time}")

        # YOUR CODE HERE
        # record this delivery in stats

    # YOUR CODE HERE
    # compute elapsed_ms from start, record this robot's running time
    #   in stats, then decrement active_robots
