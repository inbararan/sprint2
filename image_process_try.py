from __future__ import print_function
from color_state import State
import cv2
import numpy as np
import argparse
import copy
import time
import multiprocessing as mp
from sys import argv
import keyboard
from point_detector import detect_on_points


class Camera():

    def __init__(self, rtsp_url):
        # load pipe for data transmittion to the process
        self.parent_conn, child_conn = mp.Pipe()
        # load process
        self.p = mp.Process(target=self.update, args=(child_conn, rtsp_url))
        # start process
        self.p.daemon = True
        self.p.start()

    def end(self):
        # send closure request to process

        self.parent_conn.send(2)

    def update(self, conn, rtsp_url):
        # load cam into seperate process

        print("Cam Loading...")
        cap = cv2.VideoCapture(rtsp_url, cv2.CAP_FFMPEG)
        print("Cam Loaded...")
        run = True

        while run:

            # grab frames from the buffer
            cap.grab()

            # recieve input data
            rec_dat = conn.recv()

            if rec_dat == 1:
                # if frame requested
                ret, frame = cap.read()
                conn.send(frame)

            elif rec_dat == 2:
                # if close requested
                cap.release()
                run = False

        print("Camera Connection Closed")
        conn.close()

    def get_frame(self, resize=None):
        ###used to grab frames from the cam connection process

        ##[resize] param : % of size reduction or increase i.e 0.65 for 35% reduction  or 1.5 for a 50% increase

        # send request
        self.parent_conn.send(1)
        frame = self.parent_conn.recv()

        # reset request
        self.parent_conn.send(0)

        # resize if needed
        if resize == None:
            return frame
        else:
            return self.rescale_frame(frame, resize)

    def rescale_frame(self, frame, percent=65):

        return cv2.resize(frame, None, fx=percent, fy=percent)


def get_pics():
    frames = []
    frame_to_check = []
    frame_off = []
    cam = Camera("http://" + argv[1] + ":5000/video_feed")

    print("Camera is alive?: " + str(cam.p.is_alive()))

    while (1):
        frame = cam.get_frame()
        frames.append(copy.deepcopy(frame))
        cv2.imshow("Feed", frame)
        if keyboard.is_pressed("o"):
            frame_off = copy.deepcopy(frame)
        if keyboard.is_pressed("f"):
            frame_to_check = copy.deepcopy(frame)
            break
        key = cv2.waitKey(1)

    cv2.destroyAllWindows()
    cam.end()
    return frame_to_check, frame_off


def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, ",", y)
        refPt.append([x, y])
        font = cv2.FONT_HERSHEY_SIMPLEX
        strXY = str(x) + ", " + str(y)
        cv2.putText(img, strXY, (x, y), font, 0.5, (255, 255, 0), 2)
        cv2.imshow("image", img)

    if event == cv2.EVENT_RBUTTONDOWN:
        blue = img[y, x, 0]
        green = img[y, x, 1]
        red = img[y, x, 2]
        font = cv2.FONT_HERSHEY_SIMPLEX
        strBGR = str(blue) + ", " + str(green) + "," + str(red)
        cv2.putText(img, strBGR, (x, y), font, 0.5, (0, 255, 255), 2)
        cv2.imshow("image", img)
    if len(refPt) == 5:
        cv2.setMouseCallback("image", (lambda x: x + 1))


def return_to_ophir():
    frame_to_check, frame_off = get_pics()
    events = [i for i in dir(cv2) if 'EVENT' in i]

    refPt = []

    while True:
        # *********GET 5 POINTS OF THE LOCATIONS*****************************
        # This will display all the available mouse click events

        # Here, you need to change the image name and it's path according to your directory
        img = frame_to_check
        cv2.imshow("image", img)
        if len(refPt) == 5:
            break
        # calling the mouse click event
        cv2.setMouseCallback("image", click_event)

        cv2.waitKey(1)
    cv2.destroyAllWindows()

    states = []
    while len(states) <= 30:
        cam = Camera("http://" + argv[1] + ":5000/video_feed")
        cur_frame = cam.get_frame()
        bools = detect_on_points()

    states = [State(1, 0, 1, 1, 0), State(0, 0, 1, 1, 0), State(1, 0, 1, 0, 0), State(0, 0, 1, 1, 1),
              State(1, 0, 0, 1, 0), State(1, 0, 1, 1, 0), State(0, 0, 1, 1, 0), State(1, 0, 1, 0, 0),
              State(1, 0, 0, 1, 0), State(1, 0, 1, 1, 0), State(1, 0, 0, 0, 0), State(1, 0, 1, 0, 0),
              State(1, 0, 1, 1, 0), State(0, 0, 1, 1, 0), State(1, 0, 1, 0, 0), State(0, 0, 1, 1, 1),
              State(1, 0, 0, 1, 0), State(1, 0, 1, 1, 0), State(0, 0, 1, 1, 0), State(1, 0, 1, 0, 0),
              State(1, 0, 0, 1, 0), State(1, 0, 1, 1, 0), State(0, 0, 1, 1, 0), State(1, 0, 1, 0, 0),
              State(1, 0, 1, 1, 0), State(0, 0, 1, 1, 0), State(1, 0, 1, 0, 0), State(0, 0, 1, 1, 1),
              State(1, 0, 0, 1, 0), State(1, 0, 1, 1, 0), State(0, 1, 1, 1, 0), State(0, 0, 1, 0, 0),
              State(1, 0, 0, 1, 0), State(1, 0, 1, 1, 0), State(0, 0, 1, 1, 0), State(1, 0, 1, 0, 0),
              State(0, 1, 1, 1, 0), State(0, 0, 1, 1, 0), State(1, 1, 0, 0, 0), State(0, 0, 1, 1, 1),
              State(1, 1, 1, 1, 0), State(1, 0, 1, 1, 0), State(0, 0, 1, 1, 0), State(1, 0, 1, 0, 0),
              State(1, 1, 1, 1, 1), State(1, 0, 1, 1, 0), State(0, 0, 1, 1, 0), State(1, 0, 1, 0, 0),
              State(1, 1, 0, 1, 0), State(0, 0, 1, 1, 0), State(1, 1, 1, 0, 0), State(0, 0, 1, 1, 1),
              State(1, 1, 0, 1, 1), State(1, 0, 1, 1, 0), State(0, 0, 1, 1, 0), State(1, 0, 1, 0, 0),
              State(1, 0, 0, 1, 0), State(1, 0, 1, 1, 0), State(0, 0, 1, 1, 0), State(1, 0, 1, 0, 0)]
    return states