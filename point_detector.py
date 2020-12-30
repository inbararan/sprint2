from color_state import State
import cv2 as cv
import numpy as np
import argparse

squares_side = 5
limit_on = 10


def detect_on_points(full_img, points, off_img):
    """
    This function creates circles and find colors.
    """
    bools = []
    for point in points:
        x_min = point[0] - squares_side
        x_max = point[0] + squares_side
        y_min = point[1] - squares_side
        y_max = point[1] + squares_side
        slice_full_color = full_img[y_min:y_max, x_min:x_max]
        slice_off_image = off_img[y_min:y_max, x_min:x_max]
        slice_full_gray = cv.cvtColor(slice_full_color, cv.COLOR_BGR2GRAY)
        slice_off_gray = cv.cvtColor(slice_off_image, cv.COLOR_BGR2GRAY)
        slice_it = cv.absdiff(slice_full_gray, slice_off_gray)
        avg_point = np.average(slice_it)
        if avg_point > limit_on:
            bools.append(1)
        else:
            bools.append(0)


    # gray_full = cv.cvtColor(full_img, cv.COLOR_BGR2GRAY)
    # gray_off = cv.cvtColor(off_img, cv.COLOR_BGR2GRAY)
    #

    # diff = cv.absdiff(gray_full, gray_off)
    # for point in points:
    #     cv.circle(diff, tuple(point), squares_side, (255, 0, 0), thickness=-1)

    # cv.imshow("out", slice)
    # cv.waitKey(1)

    # ret, thresh_diff = cv.threshold(diff, 50, 200, cv.THRESH_BINARY)
    return bools
