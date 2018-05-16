#!/usr/bin/env python3
"""
This module is the mini-project for the MQTT unit.  This module will be running on your PC and communicating with the
m5_ev3_remote_drive.py module that is running on your EV3 (you have to write that module too, but it's easier).
Only the Tkinter GUI has been made for you.  You will need to implement all of the MQTT communication.  The goal is to
have a program running on your computer that can control the EV3.

You will need to have the following features:
  -- Clickable drive direction buttons to drive forward (up), backwards (down), left, right, and stop (space)
    -- Keyboard shortcut keys that behave the same as clicking the buttons (this has already been wired up for you)
  -- An entry box for the left and right drive motor speeds.
    -- If both become set to 900 all of the drive direction buttons will go fast, for example forward goes 900 900
    -- If both become set to 300 all of the drive direction buttons will go slower, for example reverse goes -300 -300
    -- If 500 then left does -500 500, which causes the robot to spin left (use half speed -250 250 if too fast)
    -- If set differently to say 600 left, 300 right the robot will drive and arc, for example forward goes 600 300
  -- In addition to the drive features there needs to be a clickable button for Arm Up and Arm Down
    -- There also need to be keyboard shortcut for Arm Up (u) and Arm Down (j).  Arm calibration is not required.

  -- Finally you need 2 buttons for ending your program:
    -- Quit, which stops only this program and allows the EV3 program to keep running
    -- Exit, which sends a shutdown message to the EV3, then ends it's own program as well.

You can start by running the code to see the GUI, but don't expect button clicks to do anything useful yet.

Authors: David Fisher and Tianlin Wang.
"""  # Done: 1. PUT YOUR NAME IN THE ABOVE LINE.

import tkinter
from tkinter import ttk
import ev3dev.ev3 as ev3
import time

import mqtt_remote_method_calls as com


def main():
    mqtt_client = com.MqttClient()

    root = tkinter.Tk()
    root.title("MQTT Remote")

    main_frame = ttk.Frame(root, padding=20, relief='raised')
    main_frame.grid()

    left_speed_label = ttk.Label(main_frame, text="Left")
    left_speed_label.grid(row=0, column=0)
    left_speed_entry = ttk.Entry(main_frame, width=8)
    left_speed_entry.insert(0, '600')
    left_speed_entry.grid(row=1, column=0)

    right_speed_label = ttk.Label(main_frame, text="Right")
    right_speed_label.grid(row=0, column=2)
    right_speed_entry = ttk.Entry(main_frame, width=8, justify=tkinter.RIGHT)
    right_speed_entry.insert(0, '600')
    right_speed_entry.grid(row=1, column=2)

    stop_button = ttk.Button(main_frame, text="Stop")
    stop_button.grid(row=3, column=1)
    # stop_button and '<space>' key (note, does not need left_speed_entry, right_speed_entry)
    stop_button['command'] = lambda: send_stop(mqtt_client)
    root.bind('<space>', lambda event: send_stop(mqtt_client))

    # right_button = ttk.Button(main_frame, text="Right")
    # right_button.grid(row=3, column=2)
    # right_button and '<Right>' key
    # right_button['command'] = lambda: send_right(mqtt_client, int(left_speed_entry.get()), int(right_speed_entry.get()))
    # root.bind('<Right>',
    #           lambda event: send_right(mqtt_client, int(left_speed_entry.get()), int(right_speed_entry.get())))
    #
    # back_button = ttk.Button(main_frame, text="Back")
    # back_button.grid(row=4, column=1)
    # back_button and '<Down>' key
    # back_button['command'] = lambda: send_back(mqtt_client, int(left_speed_entry.get()), int(right_speed_entry.get()))
    # root.bind('<Down>', lambda event: send_back(mqtt_client, int(left_speed_entry.get()), int(right_speed_entry.get())))

    up_button = ttk.Button(main_frame, text="Up")
    up_button.grid(row=5, column=0)
    up_button['command'] = lambda: send_up(mqtt_client)
    root.bind('<u>', lambda event: send_up(mqtt_client))

    down_button = ttk.Button(main_frame, text="Down")
    down_button.grid(row=6, column=0)
    down_button['command'] = lambda: send_down(mqtt_client)
    root.bind('<j>', lambda event: send_down(mqtt_client))

    # Buttons for quit and exit
    q_button = ttk.Button(main_frame, text="Quit")
    q_button.grid(row=5, column=2)
    q_button['command'] = (lambda: quit_program(mqtt_client, False))

    e_button = ttk.Button(main_frame, text="Exit")
    e_button.grid(row=6, column=2)
    e_button['command'] = (lambda: quit_program(mqtt_client, True))

    # draw_button = ttk.Button(main_frame, text="Draw")
    # draw_button.grid(row=7, column=0)
    # draw_button and '<Draw>' key
    # draw_button['command'] = (lambda: drawIt())

    seek_button = ttk.Button(main_frame, text="Seek")
    seek_button.grid(row=7, column=2)
    # draw_button and '<Draw>' key
    seek_button['command'] = (lambda: seekbeacon())

    #
    # seconds = current_heading/(speed*1.8)

    root.mainloop()


def send_up(mqtt_client):
    print("arm_up")
    mqtt_client.send_message("arm_up")


def send_forward(mqtt_client, leftspeed, rightspeed):
    print("motor_forward")
    mqtt_client.send_message("motor_forward", [leftspeed, rightspeed])


def send_back(mqtt_client, leftspeed, rightspeed):
    print("motor_back")
    mqtt_client.send_message("motor_back", [leftspeed, rightspeed])


def send_left(mqtt_client, leftspeed, rightspeed):
    print("motor_left")
    mqtt_client.send_message("motor_left", [leftspeed, rightspeed])


def send_right(mqtt_client, leftspeed, rightspeed):
    print("motor_right")
    mqtt_client.send_message("motor_right", [leftspeed, rightspeed])


def send_stop(mqtt_client):
    print("motor_stop")
    mqtt_client.send_message("motor_stop")


def send_down(mqtt_client):
    print("arm_down")
    mqtt_client.send_message("arm_down")


def quit_program(mqtt_client, shutdown_ev3):
    if shutdown_ev3:
        print("shutdown")
        mqtt_client.send_message("shutdown")
    mqtt_client.close()
    exit()


# def drawIt():
#     pen_data = PenData()
#     root1 = tkinter.Tk()
#     draw_frame = ttk.Frame(root1, padding=5)
#     draw_frame.grid()
#
#     instructions = 'Click the left mouse button to make circles,\n'
#     instructions = instructions + 'drag the left mouse button to draw'
#     label = ttk.Label(draw_frame, text=instructions)
#     label.grid()
#
#     # Make a tkinter.Canvas on a Frame.
#     # Note that Canvas is a tkinter (NOT a ttk) class.
#     canvas = tkinter.Canvas(draw_frame, background='lightgray')
#     canvas.grid()
#
#     # Make callbacks for mouse events.
#     # canvas.bind('<Button-1>', lambda event: left_mouse_click(event))
#     canvas.bind('<B1-Motion>',
#                 lambda event: left_mouse_drag(event, pen_data))
#     canvas.bind('<B1-ButtonRelease>',
#                 lambda event: left_mouse_release(pen_data))  # @UnusedVariable
#
#     # Make a button to change the color.
#     button = ttk.Button(draw_frame, text='Flip pen color')
#     button.grid()
#     button['command'] = lambda: flip_pen_color(pen_data)
#
#     root1.mainloop()
#     return True


# def start_point():
#     canvas = event.widget
#     canvas.
#     canvas.create_oval(event.x - 10, event.y - 10,
#                        event.x + 10, event.y + 10,
#                        fill='green', width=3)


# def left_mouse_drag(event, data):
#     # data.mouse_position_x and _y keep track of the PREVIOUS mouse
#     # position while we are dragging.
#     canvas = event.widget
#     if data.is_dragging:
#         canvas.create_line(data.mouse_position_x, data.mouse_position_y,
#                            event.x, event.y,
#                            fill=data.color, width=5)
#     else:
#         data.is_dragging = True  # Start dragging
#
#     data.mouse_position_x = event.x
#     data.mouse_position_y = event.y
#
#
# def left_mouse_release(data):
#     data.is_dragging = False
#
#
# def flip_pen_color(data):
#     if data.color == 'blue':
#         data.color = 'red'
#     else:
#         data.color = 'blue'


def seekbeacon():
    print("--------------------------------------------")
    print(" Printing beacon seeking data")
    print("--------------------------------------------")
    ev3.Sound.speak("Printing beacon seeking").wait()
    print(" Press the touch sensor to exit")

    touch_sensor = ev3.TouchSensor()
    beacon_seeker = ev3.BeaconSeeker()
    assert touch_sensor
    assert beacon_seeker

    while not touch_sensor.is_pressed:
        current_heading = beacon_seeker.heading(channel=1)
        current_distance = beacon_seeker.distance
        print("IR Heading = {}   Distance = {}".format(current_heading, current_distance))
        time.sleep(0.5)

    print("Goodbye!")
    ev3.Sound.speak("Goodbye").wait()
    return True



main()