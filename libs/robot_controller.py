"""
  Library of EV3 robot functions that are useful in many different applications. For example things
  like arm_up, arm_down, driving around, or doing things with the Pixy camera.

  Add commands as needed to support the features you'd like to implement.  For organizational
  purposes try to only write methods into this library that are NOT specific to one tasks, but
  rather methods that would be useful regardless of the activity.  For example, don't make
  a connection to the remote control that sends the arm up if the ir remote control up button
  is pressed.  That's a specific input --> output task.  Maybe some other task would want to use
  the IR remote up button for something different.  Instead just make a method called arm_up that
  could be called.  That way it's a generic action that could be used in any task.
"""

import ev3dev.ev3 as ev3
import time


class Snatch3r(object):
    """Commands for the Snatch3r robot that might be useful in many different programs."""
    
    # TODO: Implement the Snatch3r class as needed when working the sandox exercises
    # (and delete these comments)

    def __init__(self):
        self.left_motor = ev3.LargeMotor(ev3.OUTPUT_B)
        self.right_motor = ev3.LargeMotor(ev3.OUTPUT_C)
        self.beacon_seeker = ev3.BeaconSeeker(channel=1)
        assert self.left_motor.connected
        assert self.right_motor.connected

    def forward(self, distance, speed, stop_action='brake'):
        degrees = distance * 0.39 * (120/4.2)

        self.left_motor.run_to_rel_pos(position_sp=degrees, speed_sp=speed*8, stop_action=stop_action)
        self.right_motor.run_to_rel_pos(position_sp=degrees, speed_sp=speed*8, stop_action=stop_action)
        self.left_motor.wait_while("running")
        self.right_motor.wait_while("running")

    def backward(self, distance, speed, stop_action='brake'):
        degrees = -distance * 0.39 * (120 / 4.2)
        self.left_motor.run_to_rel_pos(position_sp=degrees, speed_sp=speed*8, stop_action=stop_action)
        self.right_motor.run_to_rel_pos(position_sp=degrees, speed_sp=speed*8, stop_action=stop_action)
        self.left_motor.wait_while("running")
        self.right_motor.wait_while("running")

    def turnleft(self, degrees, speed=100, stop_action='brake'):
        degrees = (degrees/360) * 44 * (360/4.2)
        self.left_motor.run_to_rel_pos(position_sp=degrees, speed_sp=speed*-8, stop_action=stop_action)
        self.left_motor.wait_while("running")

    def turnright(self, degrees, speed=100, stop_action='brake'):
        degrees = (degrees/360) * 44 * (360/4.2)
        self.right_motor.run_to_rel_pos(position_sp=degrees, speed_sp=speed*-8, stop_action=stop_action)
        self.right_motor.wait_while("running")

    def arm_up(self):
        arm_motor = ev3.MediumMotor(ev3.OUTPUT_A)
        touch_sensor = ev3.TouchSensor()
        arm_motor.run_forever(speed_sp=900)
        while not touch_sensor.is_pressed:
            time.sleep(0.01)
        arm_motor.stop(stop_action=ev3.Motor.STOP_ACTION_BRAKE)

    def arm_down(self):
        arm_motor = ev3.MediumMotor(ev3.OUTPUT_A)
        arm_motor.run_forever(speed_sp=-900)
        time.sleep(5.01)
        arm_motor.stop(stop_action=ev3.Motor.STOP_ACTION_BRAKE)

    def shutdown(self):
        self.left_motor.stop_action()
        self.right_motor.stop_action()

    def seekbeacon(self, left_speed):
        print("--------------------------------------------")
        print(" Printing beacon seeking data")
        print("--------------------------------------------")
        ev3.Sound.speak("Printing beacon seeking").wait()
        print(" Press the touch sensor to exit")

        touch_sensor = ev3.TouchSensor()
        assert touch_sensor
        assert self.beacon_seeker

        while not touch_sensor.is_pressed:
            current_heading = self.beacon_seeker.heading
            current_distance = self.beacon_seeker.distance
            print("IR Heading = {}   Distance = {}".format(current_heading, current_distance))
            time.sleep(0.5)

            self.arm_up()
            if current_heading < 0:
                self.turnright(current_heading)
            if current_heading > 0:
                self.turnleft(abs(current_heading))
            self.forward(current_distance, left_speed)
            self.arm_down()
            self.backward(current_distance,left_speed)
            break

        print("Goodbye!")
        ev3.Sound.speak("Goodbye").wait()
        return True
