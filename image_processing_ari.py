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

    # threshold the picture - depends on the intensity
    diff = cv.cvtColor(diff, cv.COLOR_BGR2GRAY)
    # ret, thresh_diff = cv.threshold(diff, 100, 200, cv.THRESH_BINARY)


    contours, hierarchy = cv.findContours(diff, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    # locate contours
    contours = contours[1:]
    rects = []

    for cont in contours:
        x, y, w, h = cv.boundingRect(cont)
        rects.append([x, y, w, h, (0, 0, 255)])

    print(rects)
    # add rectangles to pictures
    for rec in rects:
        thresh_diff = cv.rectangle(diff, (rec[0], rec[1]), (rec[0] + rec[2], rec[1] + rec[3]), rec[4], 3)

    # Now show the image
    cv.imshow('Output', diff)
    cv.waitKey()
    cv.destroyAllWindows()

    diff = diff + diff

    cv.imshow('Output', diff)
    cv.waitKey()
    cv.destroyAllWindows()


list_on = cv.imread("pic_check.jpeg")
list_off = cv.imread("pic_check_off.jpeg")
cv.waitKey()
cv.destroyAllWindows()
locate_leds_and_crops(list_on, list_off)

# create dictionary


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
