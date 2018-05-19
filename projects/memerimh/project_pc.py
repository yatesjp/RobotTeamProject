
import tkinter
from tkinter import ttk

import mqtt_remote_method_calls as com


def main():
    my_delegate = MyDelegate()
    mqtt_client = com.MqttClient(my_delegate)
    mqtt_client.connect_to_ev3()
    my_delegate.mqtt_client = mqtt_client

    root = tkinter.Tk()
    root.title("MQTT Remote")

    main_frame = ttk.Frame(root, padding=20, relief='raised')
    main_frame.grid()

    speed_label = ttk.Label(main_frame, text="Left")
    speed_label.grid(row=0, column=0)
    speed_entry = ttk.Entry(main_frame, width=8)
    speed_entry.insert(0, "600")
    speed_entry.grid(row=1, column=0)

    forward_button = ttk.Button(main_frame, text="Forward")
    forward_button.grid(row=2, column=1)
    forward_button['command'] = lambda: send_forward(mqtt_client, int(speed_entry.get()), int(speed_entry.get()))
    root.bind('<Up>', lambda event: send_forward(mqtt_client, int(speed_entry.get()), int(speed_entry.get())))

    left_button = ttk.Button(main_frame, text="Left")
    left_button.grid(row=3, column=0)
    left_button['command'] = lambda: send_left(mqtt_client, int(speed_entry.get()), int(speed_entry.get()))
    root.bind('<Left>', lambda event: send_left(mqtt_client, int(speed_entry.get()), int(speed_entry.get())))

    stop_button = ttk.Button(main_frame, text="Stop")
    stop_button.grid(row=3, column=1)
    stop_button['command'] = lambda: send_stop(mqtt_client)
    root.bind('<space>', lambda event: send_stop(mqtt_client))

    right_button = ttk.Button(main_frame, text="Right")
    right_button.grid(row=3, column=2)
    right_button['command'] = lambda: send_right(mqtt_client, int(speed_entry.get()), int(speed_entry.get()))
    root.bind('<Right>', lambda event: send_right(mqtt_client, int(speed_entry.get()), int(speed_entry.get())))

    back_button = ttk.Button(main_frame, text="Back")
    back_button.grid(row=4, column=1)
    back_button['command'] = lambda: send_back(mqtt_client, int(speed_entry.get()), int(speed_entry.get()))
    root.bind('<Down>', lambda event: send_back(mqtt_client, int(speed_entry.get()), int(speed_entry.get())))

    e_button = ttk.Button(main_frame, text="Exit")
    e_button.grid(row=6, column=2)
    e_button['command'] = (lambda: quit_program(mqtt_client, True))

    root.mainloop()

def send_forward(mqtt_client, leftspeed, rightspeed):
    print("motor_forward")
    mqtt_client.send_message("motor_forward", [leftspeed,rightspeed])

def send_back(mqtt_client, leftspeed, rightspeed):
    print("motor_back")
    mqtt_client.send_message("motor_back", [leftspeed,rightspeed])

def send_left(mqtt_client, leftspeed, rightspeed):
    print("motor_left")
    mqtt_client.send_message("motor_left", [leftspeed,rightspeed])

def send_right(mqtt_client, leftspeed, rightspeed):
    print("motor_right")
    mqtt_client.send_message("motor_right", [leftspeed,rightspeed])

def send_stop(mqtt_client):
    print("motor_stop")
    mqtt_client.send_message("motor_stop")



# Quit and Exit button callbacks
def quit_program(mqtt_client, shutdown_ev3):
    if shutdown_ev3:
        print("shutdown")
        mqtt_client.send_message("shutdown")
    mqtt_client.close()
    exit()

class MyDelegate(object):
    def __init__(self):
        self.mqtt_client = None  # To be set later.
    def stop_alert(self):
        print("Movement stopped due to obstruction!")

main()
