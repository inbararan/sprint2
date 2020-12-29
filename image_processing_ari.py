from __future__ import print_function
from color_state import State
import cv2 as cv
import numpy as np
import argparse

# FIRST FUNCTION - RECEIVE COUPLE OF PICTURES
# AND LOCATES THE DIFFERENCE

def create_average(list_pics_on, list_pics_off):
    # get the average pictures of the pictures filmed
    tmp = []
    for idx_row in range(len(list_pics_on)):
        tmp = np.average(list_pics_on[idx_row])
        list_pics_on[idx_row] = tmp
        tmp = []

    tmp = []
    for idx_row in range(len(list_pics_off)):
        tmp = np.average(list_pics_off[idx_row])
        list_pics_off[idx_row] = tmp
        tmp = []

    #find the rectangles that the leds are in
    locs = locate_leds_and_crops(list_pics_on, list_pics_off)


def locate_leds_and_crops(light_on, light_off):
    # get first pic on and second off
    # find the differences
    diff = cv.absdiff(light_off, light_on)
    cv.imshow('Output', diff)
    cv.waitKey()
    cv.destroyAllWindows()

    # threshold the picture - depends on the intensity
    diff = cv.cvtColor(diff, cv.COLOR_BGR2GRAY)
    ret, thresh_diff = cv.threshold(diff, 50, 200, cv.THRESH_BINARY)

    contours, hierarchy = cv.findContours(thresh_diff, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    # locate contours
    contours = contours[1:]
    rects = []

    for cont in contours:
        x, y, w, h = cv.boundingRect(cont)
        rects.append([x, y, w, h, (0, 0, 255)])

    print(rects)
    # add rectangles to pictures
    for rec in rects:
        thresh_diff = cv.rectangle(thresh_diff, (rec[0], rec[1]), (rec[0] + rec[2], rec[1] + rec[3]), rec[4], 3)

    # Now show the image
    cv.imshow('Output', thresh_diff)
    cv.waitKey()
    cv.destroyAllWindows()

list_on = cv.imread("light_on_2.jpeg")
list_off = cv.imread("light_off_2.jpeg")
cv.waitKey()
cv.destroyAllWindows()
locate_leds_and_crops(list_on, list_off)

#create dictionary
def return_to_ophir():
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
# max_value = 255
# max_value_H = 360 // 2
# low_H = 0
# low_S = 0
# low_V = 0
# high_H = max_value_H
# high_S = max_value
# high_V = max_value
# window_capture_name = 'Video Capture'
# window_detection_name = 'Object Detection'
# low_H_name = 'Low H'
# low_S_name = 'Low S'
# low_V_name = 'Low V'
# high_H_name = 'High H'
# high_S_name = 'High S'
# high_V_name = 'High V'
#
#
# def on_low_H_thresh_trackbar(val):
#     global low_H
#     global high_H
#     low_H = val
#     low_H = min(high_H - 1, low_H)
#     cv.setTrackbarPos(low_H_name, window_detection_name, low_H)
#
#
# def on_high_H_thresh_trackbar(val):
#     global low_H
#     global high_H
#     high_H = val
#     high_H = max(high_H, low_H + 1)
#     cv.setTrackbarPos(high_H_name, window_detection_name, high_H)
#
#
# def on_low_S_thresh_trackbar(val):
#     global low_S
#     global high_S
#     low_S = val
#     low_S = min(high_S - 1, low_S)
#     cv.setTrackbarPos(low_S_name, window_detection_name, low_S)
#
#
# def on_high_S_thresh_trackbar(val):
#     global low_S
#     global high_S
#     high_S = val
#     high_S = max(high_S, low_S + 1)
#     cv.setTrackbarPos(high_S_name, window_detection_name, high_S)
#
#
# def on_low_V_thresh_trackbar(val):
#     global low_V
#     global high_V
#     low_V = val
#     low_V = min(high_V - 1, low_V)
#     cv.setTrackbarPos(low_V_name, window_detection_name, low_V)
#
#
# def on_high_V_thresh_trackbar(val):
#     global low_V
#     global high_V
#     high_V = val
#     high_V = max(high_V, low_V + 1)
#     cv.setTrackbarPos(high_V_name, window_detection_name, high_V)
#
#
# parser = argparse.ArgumentParser(description='Code for Thresholding Operations using inRange tutorial.')
# parser.add_argument('--camera', help='Camera divide number.', default=0, type=int)
# args = parser.parse_args()
# cap = cv.VideoCapture(args.camera)
# cv.namedWindow(window_capture_name)
# cv.namedWindow(window_detection_name)
# cv.createTrackbar(low_H_name, window_detection_name, low_H, max_value_H, on_low_H_thresh_trackbar)
# cv.createTrackbar(high_H_name, window_detection_name, high_H, max_value_H, on_high_H_thresh_trackbar)
# cv.createTrackbar(low_S_name, window_detection_name, low_S, max_value, on_low_S_thresh_trackbar)
# cv.createTrackbar(high_S_name, window_detection_name, high_S, max_value, on_high_S_thresh_trackbar)
# cv.createTrackbar(low_V_name, window_detection_name, low_V, max_value, on_low_V_thresh_trackbar)
# cv.createTrackbar(high_V_name, window_detection_name, high_V, max_value, on_high_V_thresh_trackbar)
# while True:
#
#     ret, frame = cap.read()
#     if frame is None:
#         break
#     frame_HSV = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
#     frame_threshold = cv.inRange(frame_HSV, (low_H, low_S, low_V), (high_H, high_S, high_V))
#
#     cv.imshow(window_capture_name, frame)
#     cv.imshow(window_detection_name, frame_threshold)
#
#     key = cv.waitKey(30)
#     if key == ord('q') or key == 27:
#         break
