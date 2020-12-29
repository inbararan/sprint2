import cv2
import copy
import time
import multiprocessing as mp
from sys import argv
import keyboard

class Camera():

    def __init__(self,rtsp_url):
        #load pipe for data transmittion to the process
        self.parent_conn, child_conn = mp.Pipe()
        #load process
        self.p = mp.Process(target=self.update, args=(child_conn,rtsp_url))
        #start process
        self.p.daemon = True
        self.p.start()

    def end(self):
        #send closure request to process

        self.parent_conn.send(2)

    def update(self,conn,rtsp_url):
        #load cam into seperate process

        print("Cam Loading...")
        cap = cv2.VideoCapture(rtsp_url,cv2.CAP_FFMPEG)
        print("Cam Loaded...")
        run = True

        while run:

            #grab frames from the buffer
            cap.grab()

            #recieve input data
            rec_dat = conn.recv()


            if rec_dat == 1:
                #if frame requested
                ret,frame = cap.read()
                conn.send(frame)

            elif rec_dat ==2:
                #if close requested
                cap.release()
                run = False

        print("Camera Connection Closed")
        conn.close()

    def get_frame(self,resize=None):
        ###used to grab frames from the cam connection process

        ##[resize] param : % of size reduction or increase i.e 0.65 for 35% reduction  or 1.5 for a 50% increase

        #send request
        self.parent_conn.send(1)
        frame = self.parent_conn.recv()

        #reset request
        self.parent_conn.send(0)

        #resize if needed
        if resize == None:
            return frame
        else:
            return self.rescale_frame(frame,resize)

    def rescale_frame(self,frame, percent=65):

        return cv2.resize(frame,None,fx=percent,fy=percent)


def main():
    frames = []
    vc = Camera("http://" + argv[1] + ":5000/video_feed")
    # vc = cv2.VideoCapture(0)

    # print("Camera is alive?: " + str(cam.p.is_alive()))

    while(1):

        frame = vc.get_frame()
        # ret, frame = vc.read()
        frames.append(copy.deepcopy(frame))
        cv2.imshow("Feed", frame)

        key = cv2.waitKey(1)

        if key == 13: #13 is the Enter Key
            break

    cv2.destroyAllWindows()

    # cam.end()
    return frames, vc

if __name__ == '__main__':
    frames, vc = main()
    # save the photos
    img_array = frames

    out = cv2.VideoWriter('output.avi', cv2.VideoWriter_fourcc(*'XVID'), 20.0,
                          (int(vc.get(3)), int(vc.get(4))))


    for i in range(len(img_array)):
        out.write(img_array[i])
    out.release()