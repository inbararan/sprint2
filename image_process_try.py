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
import get_frames_from_video
# get_frame_from_vid = get_frames_from_video.create_get_frame_func()


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
    frame_to_check = []
    frame_off = []
    cam = Camera("http://" + argv[1] + ":5000/video_feed")
    # cam = cv2.VideoCapture(0)
    # print("Camera is alive?: " + str(cam.p.is_alive()))

    while (1):
        frame = cam.get_frame()
        # frame = get_frame_from_vid()
        # ret, frame = cam.read()
        cv2.imshow("Feed", frame)
        if keyboard.is_pressed("o"):
            frame_off = copy.deepcopy(frame)
            print("o pressed!")
        if keyboard.is_pressed("f"):
            frame_to_check = copy.deepcopy(frame)
            break
        key = cv2.waitKey(1)

    cv2.destroyAllWindows()
    cam.end()
    # cam.release()
    return frame_to_check, frame_off


def click_event(event, x, y, flags, param):
    if len(refPt) >= 5:
        return
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, ",", y)
        refPt.append([x, y])
        font = cv2.FONT_HERSHEY_SIMPLEX
        strXY = str(x) + ", " + str(y)
        # cv2.putText(img, strXY, (x, y), font, 0.5, (255, 255, 0), 2)
        cv2.imshow("image", img)

    if event == cv2.EVENT_RBUTTONDOWN:
        blue = img[y, x, 0]
        green = img[y, x, 1]
        red = img[y, x, 2]
        font = cv2.FONT_HERSHEY_SIMPLEX
        strBGR = str(blue) + ", " + str(green) + "," + str(red)
        # cv2.putText(img, strBGR, (x, y), font, 0.5, (0, 255, 255), 2)
        cv2.imshow("image", img)
    # if len(refPt) == 5:
    #     cv2.setMouseCallback("image", (lambda x: x + 1))


refPt = []


def return_to_ophir():
    frame_to_check, frame_off = get_pics()

    events = [i for i in dir(cv2) if 'EVENT' in i]

    while True:
        # *********GET 5 POINTS OF THE LOCATIONS*****************************
        # This will display all the available mouse click events

        # Here, you need to change the image name and it's path according to your directory
        global img
        img = frame_to_check
        cv2.imshow("image", img)
        if len(refPt) == 5:
            break
        # calling the mouse click event
        cv2.setMouseCallback("image", click_event)

        cv2.waitKey(1)
    cv2.destroyAllWindows()

    states = []
    check_if_already = False
    # cam = cv2.VideoCapture(0)
    cam = Camera("http://" + argv[1] + ":5000/video_feed")
    while True:
        cur_frame = cam.get_frame()
        cv2.imshow("Feed", cur_frame)
        cv2.waitKey(1)
        # cur_frame = get_frame_from_vid()
        # ret, cur_frame = cam.read()
        if cur_frame is None:
            break
        bools = detect_on_points(cur_frame, refPt, frame_off)
        # print(bools)
        # if keyboard.is_pressed("j"):
        #     states.append(State(2, 2, 2, 2, 2))
        #     print("j pressed!")
        if keyboard.is_pressed("s"):
            break
        # if len(states) > 20 and len(states) % 2 == 0 and bools == [1, 1, 1, 1, 1]:
        #    break
        if bools == [1, 1, 1, 1, 1] or bools == [0, 0, 0, 0, 0]:
            continue
        if not(bools[4] == 1 and bools[0] == 0 and bools[1] == 0 and bools[2] == 0 and bools[3] == 0) and not check_if_already:
            states.append(State(bools[0], bools[1], bools[2], bools[3], 0))
            check_if_already = True
        elif bools[4] == 1 and bools[0] == 0 and bools[1] == 0 and bools[2] == 0 and bools[3] == 0:
            check_if_already = False
    # cam.release()
    cam.end()
    cv2.destroyAllWindows()
    if len(states) % 2 != 0:
        states.append(State(0, 0, 0, 0, 0))
    print(states)
    return states
