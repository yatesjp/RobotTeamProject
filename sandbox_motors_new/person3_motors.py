"""
Functions for TURNING the robot LEFT and RIGHT.
Authors: David Fisher, David Mutchler and Mattias Memering.
"""  # TDO: 1. PUT YOUR NAME IN THE ABOVE LINE.

# TOO: 2. Implment turn_left_seconds, then the relevant part of the test function.
#          Test and correct as needed.
#   Then repeat for turn_left_by_time.
#   Then repeat for turn_left_by_encoders.
#   Then repeat for the turn_right functions.

import ev3dev.ev3 as ev3
import time


def test_turn_left_turn_right():
    """
    Tests the turn_left and turn_right functions, as follows:
      1. Repeatedly:
          -- Prompts for and gets input from the console for:
             -- Seconds to travel
                  -- If this is 0, BREAK out of the loop.
             -- Speed at which to travel (-100 to 100)
             -- Stop action ("brake", "coast" or "hold")
          -- Makes the robot run per the above.
      2. Same as #1, but gets degrees and runs turn_left_by_time.
      3. Same as #2, but runs turn_left_by_encoders.
      4. Same as #1, 2, 3, but tests the turn_right functions.
    """
    print("Testing turn left by seconds")
    while True:
        while True:
            speed = int(input("Input a speed between 0 and 100"))
            seconds = int(input("Input a number of seconds greater than 0"))
            stop_action = str(input("Choose a stop action 'brake', 'coast', or 'hold'"))
            if speed >= 0:
                if seconds >= 0:
                    if stop_action == "brake":
                        break
                    if stop_action == "coast":
                        break
                    if stop_action == "hold":
                        break
            print("One or more of the inputs you gave was invalid, please choose valid inputs.")
        if seconds == 0:
            break
        turn_left_seconds(seconds, speed, stop_action)
    print("Testing turn left by time")
    while True:
        while True:
            speed = int(input("Input a speed between 0 and 100"))
            degrees = int(input("Input a number of degrees greater than 0"))
            stop_action = str(input("Choose a stop action 'brake', 'coast', or 'hold'"))
            if speed >= 0:
                if degrees >= 0:
                    if stop_action == "brake":
                        break
                    if stop_action == "coast":
                        break
                    if stop_action == "hold":
                        break
            print("One or more of the inputs you gave was invalid, please choose valid inputs.")
        if degrees == 0:
            break
        turn_left_by_time(degrees, speed, stop_action)
    print("Testing turn left by encoder")
    while True:
        while True:
            speed = int(input("Input a speed between 0 and 100"))
            degrees = int(input("Input a number of degrees greater than 0"))
            stop_action = str(input("Choose a stop action 'brake', 'coast', or 'hold'"))
            if speed >= 0:
                if degrees >= 0:
                    if stop_action == "brake":
                        break
                    if stop_action == "coast":
                        break
                    if stop_action == "hold":
                        break
            print("One or more of the inputs you gave was invalid, please choose valid inputs.")
        if degrees == 0:
            break
        turn_left_by_encoders(degrees, speed, stop_action)
    print("Testing turn right by seconds")
    while True:
        while True:
            speed = int(input("Input a speed between 0 and 100"))
            seconds = int(input("Input a number of seconds greater than 0"))
            stop_action = str(input("Choose a stop action 'brake', 'coast', or 'hold'"))
            if speed >= 0:
                if seconds >= 0:
                    if stop_action == "brake":
                        break
                    if stop_action == "coast":
                        break
                    if stop_action == "hold":
                        break
            print("One or more of the inputs you gave was invalid, please choose valid inputs.")
        if seconds == 0:
            break
        turn_right_seconds(seconds, speed, stop_action)
    print("Testing turn right by time")
    while True:
        while True:
            speed = int(input("Input a speed between 0 and 100"))
            degrees = int(input("Input a number of degrees greater than 0"))
            stop_action = str(input("Choose a stop action 'brake', 'coast', or 'hold'"))
            if speed >= 0:
                if degrees >= 0:
                    if stop_action == "brake":
                        break
                    if stop_action == "coast":
                        break
                    if stop_action == "hold":
                        break
            print("One or more of the inputs you gave was invalid, please choose valid inputs.")
        if degrees == 0:
            break
        turn_right_by_time(degrees, speed, stop_action)
    print("Testing right left by encoder")
    while True:
        while True:
            speed = int(input("Input a speed between 0 and 100"))
            degrees = int(input("Input a number of degrees greater than 0"))
            stop_action = str(input("Choose a stop action 'brake', 'coast', or 'hold'"))
            if speed >= 0:
                if degrees >= 0:
                    if stop_action == "brake":
                        break
                    if stop_action == "coast":
                        break
                    if stop_action == "hold":
                        break
            print("One or more of the inputs you gave was invalid, please choose valid inputs.")
        if degrees == 0:
            break
        turn_right_by_encoders(degrees, speed, stop_action)


def turn_left_seconds(seconds, speed, stop_action):
    """
    Makes the robot turn in place left for the given number of seconds at the given speed,
    where speed is between -100 (full speed turn_right) and 100 (full speed turn_left).
    Uses the given stop_action.
    """
    left_motor.run_forever(speed_sp=speed)
    time.sleep(seconds)
    left_motor.stop(stop_action=stop_action)


def turn_left_by_time(degrees, speed, stop_action):
    """
    Makes the robot turn in place left the given number of degrees at the given speed,
    where speed is between -100 (full speed turn_right) and 100 (full speed turn_left).
    Uses the algorithm:
      0. Compute the number of seconds to move to achieve the desired distance.
      1. Start moving.
      2. Sleep for the computed number of seconds.
      3. Stop moving.
    """
    seconds = (degrees*10) / speed
    left_motor.run_forever(speed_sp=speed)
    time.sleep(abs(seconds))
    left_motor.stop(stop_action=stop_action)


def turn_left_by_encoders(degrees, speed, stop_action):
    """
    Makes the robot turn in place left the given number of degrees at the given speed,
    where speed is between -100 (full speed turn_right) and 100 (full speed turn_left).
    Uses the algorithm:
      1. Compute the number of degrees the wheels should turn to achieve the desired distance.
      2. Move until the computed number of degrees is reached.
    """
    left_motor.run_to_rel_pos(position_sp=(degrees*10), speed_sp=speed, stop_action=stop_action)


def turn_right_seconds(seconds, speed, stop_action):
    """ Calls turn_left_seconds with negative speeds to achieve turn_right motion. """
    turn_left_seconds(seconds, -speed, stop_action)


def turn_right_by_time(degrees, speed, stop_action):
    """ Calls turn_left_by_time with negative speeds to achieve turn_right motion. """
    turn_left_by_time(degrees, -speed, stop_action)


def turn_right_by_encoders(degrees, speed, stop_action):
    """ Calls turn_left_by_encoders with negative speeds to achieve turn_right motion. """
    turn_left_by_encoders(degrees, -speed, stop_action)


# Connect two large motors on output ports B and C
left_motor = ev3.LargeMotor(ev3.OUTPUT_B)
right_motor = ev3.LargeMotor(ev3.OUTPUT_C)

# Check that the motors are actually conected
assert left_motor.connected
assert right_motor.connected
test_turn_left_turn_right()

