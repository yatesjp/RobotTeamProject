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
import math
import time


class Snatch3r(object):
    """Commands for the Snatch3r robot that might be useful in many different programs."""
    
    # Done: Implement the Snatch3r class as needed when working the sandox exercises
    # (and delete these comments)

    def __init__(self):
        self.left_motor = ev3.LargeMotor(ev3.OUTPUT_B)
        self.right_motor = ev3.LargeMotor(ev3.OUTPUT_C)
        self.ir_sensor = ev3.InfraredSensor()
        self.returner = None
        assert self.left_motor.connected
        assert self.right_motor.connected
        assert self.ir_sensor.connected

    def forward(self, inches, speed=100, stop_action='brake'):
        degrees = inches * (360/4.2)
        self.left_motor.run_to_rel_pos(position_sp=degrees, speed_sp=speed*8, stop_action=stop_action)
        self.right_motor.run_to_rel_pos(position_sp=degrees, speed_sp=speed*8, stop_action=stop_action)
        self.left_motor.wait_while("running")
        self.right_motor.wait_while("running")

    def backward(self, inches, speed=100, stop_action='brake'):
        degrees = inches * -(360/4.2)
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

    def beacon_seeker(self):
        beacon_seeker =ev3.BeaconSeeker(ev3.OUTPUT_A)
        beacon_seeker.run_forever(speed_sp=-900)
        time.sleep(5.01)
        beacon_seeker.stop(stop_action=ev3.Motor.STOP_ACTION_BRAKE)

    def spinleft(self, lspeed, rspeed):
        self.left_motor.run_forever(speed_sp=-1 * lspeed)
        self.right_motor.run_forever(speed_sp=rspeed)

    def spinright(self, lspeed, rspeed):
        self.left_motor.run_forever(speed_sp=lspeed)
        self.right_motor.run_forever(speed_sp=-1 * rspeed)

    def loop_forever(self):
        # This is a convenience method that I don't really recommend for most programs other than m5.
        #   This method is only useful if the only input to the robot is coming via mqtt.
        #   MQTT messages will still call methods, but no other input or output happens.
        # This method is given here since the concept might be confusing.
        self.running = True
        while self.running:
            time.sleep(0.1)  # Do nothing (except receive MQTT messages) until an MQTT message calls shutdown.

    def shutdown(self):
        # Modify a variable that will allow the loop_forever method to end. Additionally stop motors and set LEDs green.
        # The most important part of this method is given here, but you should add a bit more to stop motors, etc.
        self.running = False

    def halt(self):
        self.left_motor.stop(stop_action='brake')
        self.right_motor.stop(stop_action='brake')

    def goforward(self, lspeed, rspeed):
        self.left_motor.run_forever(speed_sp=lspeed)
        self.right_motor.run_forever(speed_sp=rspeed)

    def goback(self, lspeed, rspeed):
        self.left_motor.run_forever(speed_sp=-1 * lspeed)
        self.right_motor.run_forever(speed_sp=-1 * rspeed)

    def motion(self, td, lspeed, rspeed):
        self.left_motor.run_forever(speed_sp=lspeed)
        self.right_motor.run_forever(speed_sp=rspeed)
        time.sleep(td)
        self.halt()

    def checkir(self):
        if self.ir_sensor.proximity < 10:
            self.halt()

    def onwarduntil(self, degrees):
        self.left_motor.run_to_rel_pos(position_sp=degrees, speed_sp=600, stop_action='brake')
        self.right_motor.run_to_rel_pos(position_sp=degrees, speed_sp=600, stop_action='brake')
        pos1 = self.right_motor.position
        pos2 = pos1
        while self.left_motor.is_running:
            pos2 = self.right_motor.position
            self.checkir()

        posit = pos2 - pos1
        self.returner.send_message('receivecoords', [posit])
