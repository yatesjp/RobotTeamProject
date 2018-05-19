"Authors: Tianlin Wang."


import tkinter
from tkinter import ttk
import mqtt_remote_method_calls as com


def main():
    mqtt_client = com.MqttClient()
    mqtt_client.connect_to_ev3()

    root = tkinter.Tk()
    root.title("MQTT Remote")

    main_frame = ttk.Frame(root, padding=20, relief='raised')
    main_frame.grid()

    left_speed_label = ttk.Label(main_frame, text="Left")
    left_speed_label.grid(row=0, column=0)
    left_speed_entry = ttk.Entry(main_frame, width=8)
    left_speed_entry.insert(0, '100')
    left_speed_entry.grid(row=1, column=0)

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

    draw_button = ttk.Button(main_frame, text="Draw")
    draw_button.grid(row=7, column=0)
    # draw_button and '<Draw>' key
    draw_button['command'] = (lambda: drawIt())

    seek_button = ttk.Button(main_frame, text="Seek")
    seek_button.grid(row=7, column=2)
    seek_button['command'] = (lambda: beaconseeker(mqtt_client, int(left_speed_entry.get())))

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


def beaconseeker(mqtt_client, left_speed):
    print("find beacon")
    mqtt_client.send_message("beaconseeker", [left_speed])


class PenData(object):
    def __init__(self):
        self.color = 'blue'
        self.mouse_position_x = None
        self.mouse_position_y = None
        self.is_dragging = False


def drawIt():
    pen_data = PenData()
    root1 = tkinter.Tk()
    draw_frame = ttk.Frame(root1, padding=5)
    draw_frame.grid()

    instructions = 'Click the left mouse button to make circles,\n'
    instructions = instructions + 'drag the left mouse button to draw'
    label = ttk.Label(draw_frame, text=instructions)
    label.grid()

    # Make a tkinter.Canvas on a Frame.
    # Note that Canvas is a tkinter (NOT a ttk) class.
    canvas = tkinter.Canvas(draw_frame, background='lightgray')
    canvas.grid()

    # Make callbacks for mouse events.
    # canvas.bind('<Button-1>', lambda event: left_mouse_click(event))
    canvas.bind('<B1-Motion>',
                lambda event: left_mouse_drag(event, pen_data))
    canvas.bind('<B1-ButtonRelease>',
                lambda event: left_mouse_release(pen_data))  # @UnusedVariable

    root1.mainloop()
    return True


# def start_point():
#     canvas = event.widget
#     canvas.
#     canvas.create_oval(event.x - 10, event.y - 10,
#                        event.x + 10, event.y + 10,
#                        fill='green', width=3)


def left_mouse_drag(event, data):
    # data.mouse_position_x and _y keep track of the PREVIOUS mouse
    # position while we are dragging.
    canvas = event.widget
    if data.is_dragging:
        canvas.create_line(data.mouse_position_x, data.mouse_position_y,
                           event.x, event.y,
                           fill=data.color, width=5)
    else:
        data.is_dragging = True  # Start dragging

    data.mouse_position_x = event.x
    data.mouse_position_y = event.y


def left_mouse_release(data):
    data.is_dragging = False


main()