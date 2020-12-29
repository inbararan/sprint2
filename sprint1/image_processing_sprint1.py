import cv2 as cv
import numpy

mode = "Night"

window_crop_name = "Crop"
window_thresh_name = 'Thresholded'
# window_contoured_name = 'Contoured'

cv.namedWindow(window_crop_name)
cv.namedWindow(window_thresh_name)
# cv.namedWindow(window_contoured_name)

def crop(frame):
    h = frame.shape[0]
    w = frame.shape[1]
    wfactorl = 0.3
    wfactorr = 0.45
    hfactor = 0.4
    f = frame[int(h*hfactor):int(h-h*hfactor), int(w*wfactorl):int(w-w*wfactorr)]
    cv.imshow(window_crop_name, f)
    return f

def get_night_thresholds():
    return ((0, 0, 200), (180, 20, 255), (0, 0, 200), (180, 20, 255))
def get_day_thresholds():
    return ((0, 0, 200), (40, 20, 255), (140, 0, 200), (180, 20, 255))

def calc_thresh(frame):
    (lowHSV1, highHSV1, lowHSV2, highHSV2) = get_night_thresholds() if mode == "Night" else get_day_thresholds()

    frame_HSV = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    frame_threshold1 = cv.inRange(frame_HSV, lowHSV1, highHSV1)
    frame_threshold2 = cv.inRange(frame_HSV, lowHSV2, highHSV2)
    thresholded = cv.bitwise_or(frame_threshold1, frame_threshold2)

    kernel = numpy.ones((5, 5), numpy.uint8)
    thresholded = cv.dilate(thresholded, kernel, iterations=1)

    cv.imshow(window_thresh_name, thresholded)
    return thresholded

def contourify(thres_frame):
    centers = []
    countours, hierarchy = cv.findContours(thres_frame, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

    for contour in countours:
        M = cv.moments(contour)
        if M["m00"] == 0:
            continue
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])
        centers.append((cX, cY, cv.contourArea(contour)))
        print("DEBUG", (cX, cY), cv.contourArea(contour))

    # cv.drawContours(thres_frame, countours, -1, (15, 65, 100), 3)
    # cv.imshow(window_contoured_name, thres_frame)
    return thres_frame, centers

def process(frame):
    """Accepts image, returns list of centers"""
    cropped = crop(frame)
    frame_threshold = calc_thresh(cropped)
    contoured, centers = contourify(frame_threshold)
    return centers
