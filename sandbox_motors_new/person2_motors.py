"""
Functions for SPINNING the robot LEFT and RIGHT.
Authors: David Fisher, David Mutchler and Tianlin Wang.
"""  # Done: 1. PUT YOUR NAME IN THE ABOVE LINE.

# Done: 2. Implment spin_left_seconds, then the relevant part of the test function.
#          Test and correct as needed.
#   Then repeat for spin_left_by_time.
#   Then repeat for spin_left_by_encoders.
#   Then repeat for the spin_right functions.


import ev3dev.ev3 as ev3
import time


def test_spin_left_spin_right():
    """
    Tests the spin_left and spin_right functions, as follows:
      1. Repeatedly:
          -- Prompts for and gets input from the console for:
             -- Seconds to travel
                  -- If this is 0, BREAK out of the loop.
             -- Speed at which to travel (-100 to 100)
             -- Stop action ("brake", "coast" or "hold")
          -- Makes the robot run per the above.
      2. Same as #1, but gets degrees and runs spin_left_by_time.
      3. Same as #2, but runs spin_left_by_encoders.
      4. Same as #1, 2, 3, but tests the spin_right functions.
    """
    ev3.Sound.speak("Drive using input").wait()

    print('test spin_left_seconds')
    while True:
        traveltime = int(input("Enter a time to drive (seconds): "))
        speed = int(input("Enter a speed for the motors (-100 to 100): "))
        stopping = input("Enter a stop action for the motors from brake, coast or hold : ")
        if speed > 0 and traveltime > 0:
            if stopping == "brake":
                break
            if stopping == "coast":
                break
            if stopping == "hold":
                break
        if speed == 0 or traveltime == 0:
            break
        print("One or more of the inputs you gave was invalid, please choose valid inputs.")
    spin_left_seconds(traveltime, speed, stopping)

    print('test spin_left_time')
    while True:
        degrees = int(input("Input a number of degrees greater than 0"))
        speed = int(input("Enter a speed for the motors (-100 to 100): "))
        stopping = input("Enter a stop action for the motors from brake, coast or hold : ")
        if speed > 0 and degrees > 0:
            if stopping == "brake":
                break
            if stopping == "coast":
                break
            if stopping == "hold":
                break
        if speed == 0 or degrees == 0:
            break
        print("One or more of the inputs you gave was invalid, please choose valid inputs.")
    spin_left_by_time(degrees, speed, stopping)

    print('test spin_left_encoders')
    while True:
        degrees = int(input("Input a number of degrees greater than 0"))
        speed = int(input("Enter a speed for the motors (-100 to 100): "))
        stopping = input("Enter a stop action for the motors from brake, coast or hold : ")
        if speed > 0 and degrees > 0:
            if stopping == "brake":
                break
            if stopping == "coast":
                break
            if stopping == "hold":
                break
        if speed == 0 or degrees == 0:
            break
        print("One or more of the inputs you gave was invalid, please choose valid inputs.")
    spin_left_by_encoders(degrees, speed, stopping)

    print('test spin_right_seconds')
    while True:
        traveltime = int(input("Enter a time to drive (seconds): "))
        speed = int(input("Enter a speed for the motors (-100 to 100): "))
        stopping = input("Enter a stop action for the motors from brake, coast or hold : ")
        if speed > 0 and traveltime > 0:
            if stopping == "brake":
                break
            if stopping == "coast":
                break
            if stopping == "hold":
                break
        if speed == 0 or traveltime == 0:
            break
        print("One or more of the inputs you gave was invalid, please choose valid inputs.")
    spin_right_seconds(traveltime, speed, stopping)

    print('test spin_right_time')
    while True:
        degrees = int(input("Input a number of degrees greater than 0"))
        speed = int(input("Enter a speed for the motors (-100 to 100): "))
        stopping = input("Enter a stop action for the motors from brake, coast or hold : ")
        if speed > 0 and degrees > 0:
            if stopping == "brake":
                break
            if stopping == "coast":
                break
            if stopping == "hold":
                break
        if speed == 0 or degrees == 0:
            break
        print("One or more of the inputs you gave was invalid, please choose valid inputs.")
    spin_right_by_time(degrees, speed, stopping)

    print('test spin_right_encoders')
    while True:
        degrees = int(input("Input a number of degrees greater than 0"))
        speed = int(input("Enter a speed for the motors (-100 to 100): "))
        stopping = input("Enter a stop action for the motors from brake, coast or hold : ")
        if speed > 0 and degrees > 0:
            if stopping == "brake":
                break
            if stopping == "coast":
                break
            if stopping == "hold":
                break
        if speed == 0 or degrees == 0:
            break
        print("One or more of the inputs you gave was invalid, please choose valid inputs.")
    spin_right_by_encoders(degrees, speed, stopping)


def spin_left_seconds(seconds, speed, stop_action):
    """
    Makes the robot spin in place left for the given number of seconds at the given speed,
    where speed is between -100 (full speed spin_right) and 100 (full speed spin_left).
    Uses the given stop_action.
    """

    speed = 8 * speed
    left_motor.run_forever(speed_sp=speed)
    right_motor.run_forever(speed_sp=-speed)
    time.sleep(seconds)
    left_motor.stop()
    right_motor.stop(stop_action=stop_action)


def spin_left_by_time(degrees, speed, stop_action):
    """
    Makes the robot spin in place left the given number of degrees at the given speed,
    where speed is between -100 (full speed spin_right) and 100 (full speed spin_left).
    Uses the algorithm:
      0. Compute the number of seconds to move to achieve the desired distance.
      1. Start moving.
      2. Sleep for the computed number of seconds.
      3. Stop moving.
    """

    seconds = (degrees/90)*(abs(speed)/50)*1.8

    speed = 8 * speed
    right_motor.run_forever(speed_sp=-speed)
    time.sleep(seconds)
    left_motor.stop()
    right_motor.stop(stop_action=stop_action)


def spin_left_by_encoders(degrees, speed, stop_action):
    """
    Makes the robot spin in place left the given number of degrees at the given speed,
    where speed is between -100 (full speed spin_right) and 100 (full speed spin_left).
    Uses the algorithm:
      1. Compute the number of degrees the wheels should spin to achieve the desired distance.
      2. Move until the computed number of degrees is reached.
    """
    seconds = (degrees / 90) * (abs(speed) / 50) * 1.8
    left_motor.run_to_rel_pos(position_sp=seconds, speed_sp=speed, stop_action=stop_action)
    right_motor.run_to_rel_pos(position_sp=seconds, speed_sp=-speed, stop_action=stop_action)


def spin_right_seconds(seconds, speed, stop_action):
    """ Calls spin_left_seconds with negative speeds to achieve spin_right motion. """
    real_speed = -int(speed)
    spin_left_seconds(seconds, real_speed, stop_action)


def spin_right_by_time(degrees, speed, stop_action):
    """ Calls spin_left_by_time with negative speeds to achieve spin_right motion. """
    real_speed = -int(speed)
    spin_left_by_time(degrees, real_speed, stop_action)


def spin_right_by_encoders(degrees, speed, stop_action):
    """ Calls spin_left_by_encoders with negative speeds to achieve spin_right motion. """
    real_speed = -int(speed)
    spin_left_by_encoders(degrees, real_speed, stop_action)


left_motor = ev3.LargeMotor(ev3.OUTPUT_B)
right_motor = ev3.LargeMotor(ev3.OUTPUT_C)

assert left_motor.connected
assert right_motor.connected

test_spin_left_spin_right()