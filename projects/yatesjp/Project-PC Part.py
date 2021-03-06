"""
Author: Jonah Yates

The purpose of this program is to provide the computer support for the project's ultimate goal, which is to create
a map.

This portion specifically will call for the use of the canvas portion of tkinter to receive input from a user telling
the robot where to go. It will attempt to go there, and if in doing so it encounter's some object, it will stop and
mark off the area on the canvas, effectively creating a map for the user.

The program is only partly functional, in that it will only make it to the point where movement occurs. It will not
use the sensor and stop when it is supposed to. In addition, when it stops, it will not trigger a marker to be put on
the canvas, as I could not figure it out before the due date.

The code you'll see here is the attempt at getting it to do what I wanted to do, so you may see that I was close to
achieving my goals, but could not quite debug it successfully.

This locker number 38-20-6
ME430-9

"""

import tkinter
from tkinter import ttk

import math

import mqtt_remote_method_calls as com


class ThePoint(object):
    def __init__(self, xx, yy):
        self.x = xx
        self.y = yy

    def clone(self):
        return ThePoint(self.x, self.y)


# The starting value of the robot
currentpoint = ThePoint(300, 300)
# The starting angle of the robot
orientation = 1 * math.pi / 2


def main():
    mqtt_client = com.MqttClient()
    mqtt_client.connect_to_ev3()

    root = tkinter.Tk()
    main_frame = ttk.Frame(root, padding=5)
    main_frame.grid()

    title = 'Yates Mapper'
    label = ttk.Label(main_frame, text=title)
    label.grid()

    global canvas
    canvas = tkinter.Canvas(main_frame, background='lightGray', height=600, width=600)
    canvas.grid()
    canvas.bind('<Button-1>', lambda event: left_mouse_click(event, mqtt_client))

    root.mainloop()


def left_mouse_click(event, mqtt_client):
    destpoint = ThePoint(event.x, event.y)
    angle = calcangle(currentpoint.clone(), destpoint)
    #print(angle)
    rotate(angle, mqtt_client)
    global distance
    distance = calcdistance(currentpoint.clone(), destpoint)
    #print(distance)
    drive(distance, mqtt_client)


def calcangle(frompoint, topoint):
    ydiff = topoint.y - frompoint.y
    xdiff = topoint.x - frompoint.x
    angle = math.atan2(-1 * ydiff, xdiff) - orientation
    angle = standardize(angle)
    return angle


def calcdistance(pt1, pt2):
    xx = (pt1.x - pt2.x)**2
    yy = (pt1.y - pt2.y)**2
    dist = (xx + yy)**(1/2)
    return dist


def rotate(angle, mqtt_client):
    speed = 600
    matcoeff = 0.48479
    rads = math.fabs(angle) * matcoeff # matcoeff in time per radian
    if angle < 0:
        mqtt_client.send_message("motion", [rads, speed, -1 * speed])
    elif angle > 0:
        mqtt_client.send_message("motion", [rads, -1 * speed, speed])

    global orientation
    orientation = orientation + angle
    orientation = standardize(orientation)
    print(orientation)


def receivecoords(degtrav):
    disttrav = degtrav * 5 / 54
    global orientation
    global currentpoint
    newx = currentpoint.x + math.cos(orientation) * disttrav
    newy = currentpoint.y + math.sin(orientation) * disttrav
    if math.fabs(distance - disttrav) > 5:
        newx2 = currentpoint.x + math.cos(orientation) * (disttrav + 60)
        newy2 = currentpoint.y + math.sin(orientation) * (disttrav + 60)
        canvas.create_oval(newx2 - 5, newy2 - 5, newx2 + 5, newy2 + 5, fill='black', width=1)
    currentpoint = ThePoint(newx, newy)


def drive(distance, mqtt_client):
    degreestomove = distance * 54 / 5
    mqtt_client.send_message('onwarduntil', [degreestomove])


def standardize(x):
    if x < -1 * math.pi:
        x = 2 * math.pi + x
    if x > math.pi:
        x = -2 * math.pi + x
    return x

main()
