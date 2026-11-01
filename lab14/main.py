"""
Robot Delivery Simulation - Python version

A warehouse keeps producing parcels and dropping them on a queue.
A handful of robot threads keep grabbing parcels off that queue and
"delivering" them (just sleeping for the delivery time). Each robot
has limited battery and stops once it can't afford the next delivery.

This is a Python rewrite of a Java threading lab exercise.

Run:
    python3 main.py
"""
import time
import threading
import queue

from parcel import Parcel
from stats import Stats
from shared_counter import SharedCounter
from robot import deliver_parcels


def run_simulation(num_robots):
    # New up the shared data structures
    parcel_queue = queue.Queue()
    stats = Stats(num_robots)
    active_robots = SharedCounter(num_robots)
    print_lock = threading.Lock()

    print("Package Delivery Times, per robot\n")
    print("".join(f"Robot#{i}\t\t\t" for i in range(num_robots)))
    print("-" * 50)

    # YOUR CODE HERE
    # Create one threading.Thread per robot, targeting deliver_parcels,
    # with args (robot_id, parcel_queue, stats, active_robots, print_lock)
    # for robot_id in range(num_robots). Keep references to the threads
    # in a list, then start each one.
    

    threads = []
    
    for robot_id in range(num_robots):
        t = threading.Thread(target=deliver_parcels, args=(robot_id,parcel_queue, stats, active_robots, print_lock))
        
        threads.append(t)
        t.start()
    # >>> This is the checkpoint for this assignment. Show your setup
    # code (everything above this line) to one of the TAs for 2 points.
    # The remainder of the assignment is due at the usual time.

    start = time.time()

    # YOUR CODE HERE
    # This is the warehouse loop: while not every robot has run out of
    # battery (i.e. while active_robots.is_zero() is False), create a
    # new Parcel() and put it on parcel_queue, then time.sleep(0.05)
    # (a scaled-down version of "every 5 time units") before creating
    # the next one.

    # YOUR CODE HERE
    # Join all the robot threads

    elapsed_ms = round((time.time() - start) * 1000)
    print_summary(stats, num_robots, elapsed_ms, parcel_queue)


def print_summary(stats, num_robots, elapsed_ms, parcel_queue):
    print("\n\nRobot Summary")
    print(f"{'Robot#':>9} {'# parcels':>10} {'Parcel Time':>15} {'Running Time':>15}")

    totals = {"parcels": 0, "total_time": 0, "running_time": 0}

    for robot_id in range(num_robots):
        s = stats.for_robot(robot_id)
        for key in totals:
            totals[key] += s[key]
        print(f"{robot_id:>9} {s['parcels']:>10} {s['total_time']:>15} {s['running_time']:>15}")

    print("-" * 55)
    print(f"{'Totals: ' + str(num_robots):>9} {totals['parcels']:>10} "
          f"{totals['total_time']:>15} {totals['running_time']:>15}")

    print(f"\nTotal elapsed time: {elapsed_ms}")
    print(f"Number of parcels left on queue: {parcel_queue.qsize()}")


if __name__ == "__main__":
    num_robots = int(input("Enter the number of robots: "))
    run_simulation(num_robots)
