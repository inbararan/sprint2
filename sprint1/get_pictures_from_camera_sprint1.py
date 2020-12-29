import cv2
import keyboard
import matplotlib
import os

def create_list_of_frames():
    '''
    activate camera and return the list of frames that the camera films
    press "e" to stop filming
    :return: a list of frames that the camera films
    '''
    videoCaptureObject = cv2.VideoCapture(1)
    frames_list = []
    for i in range(1, 1000):
        ret,frame = videoCaptureObject.read()
        frames_list.append(frame)
        cv2.imshow('Capturing Video',frame)
        #if(cv2.waitKey(1) & 0xFF == ord('e')):
            #videoCaptureObject.release()
            #cv2.destroyAllWindows()
        break
    return frames_list

def show_system():
    '''
    shows the system until we press e so we can set up ths system
    :return: no return value
    '''
    videoCaptureObject = cv2.VideoCapture(1)
    while("True"):
        ret, frame = videoCaptureObject.read()
        cv2.imshow('Capturing Video', frame)
        if (cv2.waitKey(1) & 0xFF == ord('e')):
            videoCaptureObject.release()
            cv2.destroyAllWindows()
            break
