from color_state import State
import cv2 as cv
import numpy as np
import argparse

squares_side = 10
limit_on = 10


def detect_on_points(full_img, points, off_img):
    """
    This function creates circles and find colors.
    """
    gray_full = cv.cvtColor(full_img, cv.COLOR_BGR2GRAY)
    gray_off = cv.cvtColor(off_img, cv.COLOR_BGR2GRAY)

    diff = cv.absdiff(gray_full, gray_off)
    # ret, thresh_diff = cv.threshold(diff, 50, 200, cv.THRESH_BINARY)

    bools = []
    for point in points:
        x_min = point[0] - squares_side
        x_max = point[0] + squares_side
        y_min = point[1] - squares_side
        y_max = point[1] + squares_side
        slice = diff[x_min:x_max,y_min:y_max]
        avg_point = np.average(slice)
        if avg_point > limit_on:
            bools.append(1)
        else:
            bools.append(0)
    return bools
