from color_state import State
import cv2 as cv
import numpy as np
import argparse

squares_side = 6
limit_on = 40


def detect_on_points(full_img, points, off_img):
    """
    This function creates circles and find colors.
    """
    gray_full = cv.cvtColor(full_img, cv.COLOR_BGR2GRAY)
    gray_off = cv.cvtColor(off_img, cv.COLOR_BGR2GRAY)

    diff = cv.absdiff(gray_full, off_img)
    ret, thresh_diff = cv.threshold(diff, 50, 200, cv.THRESH_BINARY)

    bools = []
    for point in points:
        avg_point = np.average(thresh_diff[point[0] - squares_side:point[0] + squares_side][point[0] - squares_side:point[0] + squares_side])
        if avg_point > limit_on:
            bools.append(1)
        else:
            bools.append(0)
    return State(bools[0], bools[1], bools[2], bools[3], bools[4])
