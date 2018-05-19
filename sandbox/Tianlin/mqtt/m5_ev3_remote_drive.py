#!/usr/bin/env python3
"""
For the full problem statement and details see the corresponding m5_pc_remote_drive.py comments.

There are many solutions to this problem.  The easiest solution on the EV3 side is to NOT bother makes a wrapper
class for the robot object.  Since the challenge presented is very direct it's easiest to just use the Snatch3r class
directly as the delegate to the MQTT client.

The code below is all correct.  The loop_forever line will cause a crash right now.  You need to implement that function
in the Snatch3r class in the library (remember the advice from the lecture).  Pick one team member to implement it then
have everyone else Git update.  Here is some advice for the Snatch3r method loop_forever and it's partner, shutdown.

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

Additionally you will discover a need to create methods in your Snatch3r class to support drive, shutdown, stop, and
more. Once the EV3 code is ready, run it on the EV3 you can work on the PC side code for the MQTT Remote Control.

Author: David Fisher.
"""
import mqtt_remote_method_calls as com
import robot_controller as robo
import ev3dev as ev3
import time

def main():
    my_delegate = MyDelegate()
    mqtt_client = com.MqttClient(my_delegate)
    my_delegate.mqtt_client = mqtt_client
    mqtt_client.connect_to_pc()
    my_delegate.loop_forever()
    print("Shutdown complete.")


class MyDelegate(object):
    def __init__(self):
        self.robot = robo.Snatch3r()
        self.mqtt_client = None  # To be set later.

    def arm_up(self):
        print("Arm up")
        self.robot.arm_up()

    def arm_down(self):
        print("Arm down")
        self.robot.arm_down()

    def motor_forward(self,left,right):
        print("Motor Forward")
        self.robot.left_motor.run_forever(speed_sp=left)
        self.robot.right_motor.run_forever(speed_sp=right)

    def motor_left(self,left,right):
        print("Motor Left")
        self.robot.left_motor.run_forever(speed_sp=-left)
        self.robot.right_motor.run_forever(speed_sp=right)

    def motor_right(self,left,right):
        print("Motor Right")
        self.robot.left_motor.run_forever(speed_sp=left)
        self.robot.right_motor.run_forever(speed_sp=-right)

    def motor_back(self,left,right):
        print("Motor Left")
        self.robot.left_motor.run_forever(speed_sp=-left)
        self.robot.right_motor.run_forever(speed_sp=-right)

    def motor_stop(self):
        print("Motor  Stop")
        self.robot.left_motor.stop(stop_action ="brake")
        self.robot.right_motor.stop(stop_action ="brake")

    def shutdown(self):
        self.robot.shutdown()

    def beaconseeker(self):
        self.robot.beacon_seeker()

    def loop_forever(self):
        self.running = True
        while self.running:
            time.sleep(0.1)  # Do nothing until the robot does a shutdown.
        btn = ev3.Button()
        while not btn.backspace:
            # do stuff
            time.sleep(0.01)
        if self.mqtt_client:
            self.mqtt_client.close()
        self.robot.shutdown()
# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
