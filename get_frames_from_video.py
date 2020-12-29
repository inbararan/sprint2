# Writer: Gal Harari
# Date: 29/12/2020
import cv2


def create_frames():
    vidcap = cv2.VideoCapture('output2290.avi')
    success, image = vidcap.read()
    count = 0
    lst = [image]
    while success:

        # cv2.imwrite("frame%d.jpg" % count, image)     # save frame as JPEG file
        success, image = vidcap.read()
        lst.append(image)

        print('Read a new frame: ', success)
        count += 1
    return lst


def create_get_frame_func():
    frames = create_frames()
    global i
    i = 0

    def get_cur_frame():
        global i
        if i < len(frames):
            ret_frame = frames[i]
            i += 1
            return frames[i]
        return None


    return get_cur_frame
