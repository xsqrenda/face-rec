from img_face_rec import find_face, find_face_cap
# import requests
import cv2, os
import os
p = r'd:\Pictures\beauty\face'
img_path = p.replace('\\', '/')
os.chdir(img_path)


def init_capimg():
    cap = cv2.VideoCapture(0)
    cnt = 0
    # cascPath = 'D:/360Downloads/ide'
    while (cap.isOpened()):
        ret, frame = cap.read()
        cv2.imshow('frame', frame)
        k = cv2.waitKey(1)
        if (k == ord('s')):
            cnt += 1
            cv2.imwrite("screenshoot" + str(cnt) + ".jpg", frame)
        if cv2.waitKey(2) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()