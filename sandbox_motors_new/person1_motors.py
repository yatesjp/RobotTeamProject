"""
Functions for moving the robot FORWARD and BACKWARD.
Authors: David Fisher, David Mutchler and Jonah Yates.
"""  # Done: 1. PUT YOUR NAME IN THE ABOVE LINE.

# Done: 2. Implment forward_seconds, then the relevant part of the test function.
#          Test and correct as needed.
#   Then repeat for forward_by_time.
#   Then repeat for forward_by_encoders.
#   Then repeat for the backward functions.

import ev3dev.ev3 as ev3
import time
import math

def main():
    test_forward_backward()

def test_forward_backward():
    """
    Tests the forward and backward functions, as follows:
      1. Repeatedly:
          -- Prompts for and gets input from the console for:
             -- Seconds to travel
                  -- If this is 0, BREAK out of the loop.
             -- Speed at which to travel (-100 to 100)
             -- Stop action ("brake", "coast" or "hold")
          -- Makes the robot run per the above.
      2. Same as #1, but gets inches and runs forward_by_time.
      3. Same as #2, but runs forward_by_encoders.
      4. Same as #1, 2, 3, but tests the BACKWARD functions.
    """

    ev3.Sound.speak("Drive using input").wait()

    while True:
        travtime = int(input("Enter a time to drive (seconds): "))
        if travtime == 0:
            print('See ya later!')
            break
        speed = int(input("Enter a speed for the motors (0 to 100%): "))
        stopping = input("Enter a stop action for the motors: ")

        forward_seconds(travtime, speed, stopping)


def forward_seconds(seconds, speed, stop_action):
    """
    Makes the robot move forward for the given number of seconds at the given speed,
    where speed is between -100 (full speed backward) and 100 (full speed forward).
    Uses the given stop_action.
    """

    # Connect two large motors on output ports B and C
    left_motor = ev3.LargeMotor(ev3.OUTPUT_B)
    right_motor = ev3.LargeMotor(ev3.OUTPUT_C)

    # Check that the motors are actually connected
    assert left_motor.connected
    assert right_motor.connected

    speed = 8 * speed

    left_motor.run_forever(speed_sp = speed)
    right_motor.run_forever(speed_sp = speed)
    time.sleep(seconds)
    left_motor.stop()
    right_motor.stop(stop_action = stop_action)


def forward_by_time(inches, speed, stop_action):
    """
    Makes the robot move forward the given number of inches at the given speed,
    where speed is between -100 (full speed backward) and 100 (full speed forward).
    Uses the algorithm:
      0. Compute the number of seconds to move to achieve the desired distance.
      1. Start moving.
      2. Sleep for the computed number of seconds.
      3. Stop moving.
    """

    speed = speed * 8
    time = inches / 49 * 4000 / math.fabs(speed)

    # Connect two large motors on output ports B and C
    left_motor = ev3.LargeMotor(ev3.OUTPUT_B)
    right_motor = ev3.LargeMotor(ev3.OUTPUT_C)


    # Check that the motors are actually connected
    assert left_motor.connected
    assert right_motor.connected

    left_motor.run_forever(speed_sp=speed)
    right_motor.run_forever(speed_sp=speed)
    time.sleep(time)
    left_motor.stop()
    right_motor.stop(stop_action=stop_action)


def forward_by_encoders(inches, speed, stop_action):
    """
    Makes the robot move forward the given number of inches at the given speed,
    where speed is between -100 (full speed backward) and 100 (full speed forward).
    Uses the algorithm:
      1. Compute the number of degrees the wheels should spin to achieve the desired distance.
      2. Move until the computed number of degrees is reached.
    """

    degreestobemoved = inches / 49 * 1000

    # Connect two large motors on output ports B and C
    left_motor = ev3.LargeMotor(ev3.OUTPUT_B)
    right_motor = ev3.LargeMotor(ev3.OUTPUT_C)

    # Check that the motors are actually connected
    assert left_motor.connected
    assert right_motor.connected

    left_motor.run_to_rel_pos(speed_sp=speed, position_sp = degreestobemoved, 'brake')
    right_motor.run_to_rel_pos(speed_sp=speed, position_sp = degreestobemoved, 'brake')
    time.sleep(time)
    left_motor.stop()
    right_motor.stop(stop_action=stop_action)


def backward_seconds(seconds, speed, stop_action):
    """ Calls forward_seconds with negative speeds to achieve backward motion. """

    forward_seconds(seconds, speed, stop_action)

def backward_by_time(inches, speed, stop_action):
    """ Calls forward_by_time with negative speeds to achieve backward motion. """

    forward_by_time(inches, speed, stop_action)

def backward_by_encoders(inches, speed, stop_action):
    """ Calls forward_by_encoders with negative speeds to achieve backward motion. """

    forward_by_encoders(inches, speed, stop_action)

main()
test_forward_backward()