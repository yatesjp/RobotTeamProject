import ev3dev.ev3 as ev3
import time
import mqtt_remote_method_calls as com
import robot_controller as robo


def main():
    print("program running")
    my_delegate = MyDelegate()
    mqtt_client = com.MqttClient(my_delegate)
    my_delegate.mqtt_client = mqtt_client
    mqtt_client.connect_to_pc()
    my_delegate.loop_forever()
    print("Shutdown complete.")


def song(frequency, time):
    ev3.Sound.tone(147 * frequency, 500 * time).wait()
    ev3.Sound.tone(165 * frequency, 250 * time).wait()
    ev3.Sound.tone(185 * frequency, 250 * time).wait()
    ev3.Sound.tone(196 * frequency, 500 * time).wait()
    ev3.Sound.tone(185 * frequency, 250 * time).wait()
    ev3.Sound.tone(196 * frequency, 250 * time).wait()
    ev3.Sound.tone(247 * frequency, 500 * time).wait()
    ev3.Sound.tone(220 * frequency, 250 * time).wait()
    ev3.Sound.tone(196 * frequency, 500 * time).wait()
    ev3.Sound.tone(185 * frequency, 500 * time).wait()
    ev3.Sound.tone(0 * frequency, 250 * time).wait()
    ev3.Sound.tone(165 * frequency, 500 * time).wait()
    ev3.Sound.tone(220 * frequency, 500 * time).wait()
    ev3.Sound.tone(196 * frequency, 250 * time).wait()
    ev3.Sound.tone(185 * frequency, 250 * time).wait()
    ev3.Sound.tone(165 * frequency, 250 * time).wait()
    ev3.Sound.tone(185 * frequency, 250 * time).wait()
    ev3.Sound.tone(220 * frequency, 500 * time).wait()
    ev3.Sound.tone(196 * frequency, 1000 * time).wait()
    ev3.Sound.tone(0 * frequency, 750 * time).wait()
    ev3.Sound.tone(147 * frequency, 500 * time).wait()
    ev3.Sound.tone(147 * frequency, 500 * time).wait()
    ev3.Sound.tone(165 * frequency, 250 * time).wait()
    ev3.Sound.tone(185 * frequency, 250 * time).wait()
    ev3.Sound.tone(196 * frequency, 500 * time).wait()
    ev3.Sound.tone(185 * frequency, 250 * time).wait()
    ev3.Sound.tone(196 * frequency, 250 * time).wait()
    ev3.Sound.tone(247 * frequency, 500 * time).wait()
    ev3.Sound.tone(220 * frequency, 250 * time).wait()
    ev3.Sound.tone(196 * frequency, 500 * time).wait()
    ev3.Sound.tone(185 * frequency, 500 * time).wait()
    ev3.Sound.tone(0 * frequency, 250 * time).wait()
    ev3.Sound.tone(165 * frequency, 500 * time).wait()
    ev3.Sound.tone(220 * frequency, 500 * time).wait()
    ev3.Sound.tone(196 * frequency, 250 * time).wait()
    ev3.Sound.tone(185 * frequency, 250 * time).wait()
    ev3.Sound.tone(165 * frequency, 250 * time).wait()
    ev3.Sound.tone(185 * frequency, 250 * time).wait()
    ev3.Sound.tone(165 * frequency, 500 * time).wait()
    ev3.Sound.tone(147 * frequency, 1000 * time).wait()
    ev3.Sound.tone(0 * frequency, 750 * time).wait()
    ev3.Sound.tone(147 * frequency, 500 * time).wait()
    ev3.Sound.tone(147 * frequency, 500 * time).wait()
    ev3.Sound.tone(165 * frequency, 500 * time).wait()
    ev3.Sound.tone(185 * frequency, 750 * time).wait()
    ev3.Sound.tone(196 * frequency, 250 * time).wait()
    ev3.Sound.tone(220 * frequency, 500 * time).wait()
    ev3.Sound.tone(147 * frequency, 500 * time).wait()
    ev3.Sound.tone(147 * frequency, 750 * time).wait()
    ev3.Sound.tone(147 * frequency, 250 * time).wait()
    ev3.Sound.tone(0 * frequency, 250 * time).wait()
    ev3.Sound.tone(165 * frequency, 750 * time).wait()
    ev3.Sound.tone(185 * frequency, 250 * time).wait()
    ev3.Sound.tone(196 * frequency, 500 * time).wait()
    ev3.Sound.tone(220 * frequency, 500 * time).wait()
    ev3.Sound.tone(247 * frequency, 1500 * time).wait()
    ev3.Sound.tone(0 * frequency, 750 * time).wait()
    ev3.Sound.tone(196 * frequency, 250 * time).wait()
    ev3.Sound.tone(185 * frequency, 250 * time).wait()
    ev3.Sound.tone(165 * frequency, 500 * time).wait()
    ev3.Sound.tone(165 * frequency, 500 * time).wait()
    ev3.Sound.tone(262 * frequency, 750 * time).wait()
    ev3.Sound.tone(247 * frequency, 250 * time).wait()
    ev3.Sound.tone(220 * frequency, 500 * time).wait()
    ev3.Sound.tone(196 * frequency, 500 * time).wait()
    ev3.Sound.tone(185 * frequency, 750 * time).wait()
    ev3.Sound.tone(165 * frequency, 250 * time).wait()
    ev3.Sound.tone(147 * frequency, 500 * time).wait()
    ev3.Sound.tone(247 * frequency, 500 * time).wait()
    ev3.Sound.tone(220 * frequency, 750 * time).wait()
    ev3.Sound.tone(196 * frequency, 250 * time).wait()
    ev3.Sound.tone(196 * frequency, 1500 * time).wait()
    ev3.Sound.tone(0 * frequency, 750 * time).wait()
    ev3.Sound.tone(147 * frequency, 500 * time).wait()
    ev3.Sound.tone(247 * frequency, 750 * time).wait()
    ev3.Sound.tone(220 * frequency, 250 * time).wait()
    ev3.Sound.tone(196 * frequency, 500 * time).wait()
    ev3.Sound.tone(185 * frequency, 500 * time).wait()
    ev3.Sound.tone(165 * frequency, 1500 * time).wait()
    ev3.Sound.tone(0 * frequency, 750 * time).wait()
    ev3.Sound.tone(165 * frequency, 500 * time).wait()
    ev3.Sound.tone(262 * frequency, 750 * time).wait()
    ev3.Sound.tone(247 * frequency, 250 * time).wait()
    ev3.Sound.tone(220 * frequency, 500 * time).wait()
    ev3.Sound.tone(196 * frequency, 500 * time).wait()
    ev3.Sound.tone(185 * frequency, 1500 * time).wait()
    ev3.Sound.tone(0 * frequency, 750 * time).wait()
    ev3.Sound.tone(165 * frequency, 500 * time).wait()
    ev3.Sound.tone(147 * frequency, 500 * time).wait()
    ev3.Sound.tone(165 * frequency, 250 * time).wait()
    ev3.Sound.tone(185 * frequency, 250 * time).wait()
    ev3.Sound.tone(196 * frequency, 500 * time).wait()
    ev3.Sound.tone(185 * frequency, 250 * time).wait()
    ev3.Sound.tone(196 * frequency, 250 * time).wait()
    ev3.Sound.tone(165 * frequency, 500 * time).wait()
    ev3.Sound.tone(220 * frequency, 500 * time).wait()
    ev3.Sound.tone(185 * frequency, 500 * time).wait()
    ev3.Sound.tone(196 * frequency, 250 * time).wait()
    ev3.Sound.tone(220 * frequency, 250 * time).wait()
    ev3.Sound.tone(247 * frequency, 500 * time).wait()
    ev3.Sound.tone(262 * frequency, 500 * time).wait()
    ev3.Sound.tone(220 * frequency, 750 * time).wait()
    ev3.Sound.tone(196 * frequency, 250 * time).wait()
    ev3.Sound.tone(196 * frequency, 1500 * time).wait()


class MyDelegate(object):
    def __init__(self):
        self.robot = robo.Snatch3r()
        self.mqtt_client = None  # To be set later.

    def motor_forward(self, left, right):
        print("Motor Forward")
        self.robot.left_motor.run_forever(speed_sp=left)
        self.robot.right_motor.run_forever(speed_sp=right)

    def motor_left(self, left, right):
        print("Motor Left")
        self.robot.left_motor.run_forever(speed_sp=-left)
        self.robot.right_motor.run_forever(speed_sp=right)

    def motor_right(self, left, right):
        print("Motor Right")
        self.robot.left_motor.run_forever(speed_sp=left)
        self.robot.right_motor.run_forever(speed_sp=-right)

    def motor_back(self, left, right):
        print("Motor Left")
        self.robot.left_motor.run_forever(speed_sp=-left)
        self.robot.right_motor.run_forever(speed_sp=-right)

    def motor_stop(self):
        print("Motor  Stop")
        self.robot.left_motor.stop(stop_action="brake")
        self.robot.right_motor.stop(stop_action="brake")

    def loop_forever(self):
        self.running = True
        my_delegate = MyDelegate()
        mqtt_client = com.MqttClient(my_delegate)
        my_delegate.mqtt_client = mqtt_client
        mqtt_client.connect_to_pc()
        ir_sensor = ev3.InfraredSensor()
        touch_sensor = ev3.TouchSensor()
        while self.running:
            if ir_sensor.proximity < 60:
                self.robot.left_motor.stop(stop_action="brake")
                self.robot.right_motor.stop(stop_action="brake")
                mqtt_client.send_message("stop_alert")
            if touch_sensor.is_pressed:
                song(2, .25)
            time.sleep(0.1)  # Do nothing until the robot does a shutdown.
        btn = ev3.Button()
        while not btn.backspace:
            # do stuff
            time.sleep(0.01)
        if self.mqtt_client:
            self.mqtt_client.close()
        self.robot.shutdown()


main()
