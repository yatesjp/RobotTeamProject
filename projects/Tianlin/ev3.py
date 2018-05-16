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