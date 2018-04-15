import cv2,os,numpy
from img_face_rec import find_face_cap
from PIL import Image, ImageDraw, ImageFont

# import numpy as np
# import pickle
# import matplotlib.pyplot as plt

cap = cv2.VideoCapture(0)

cascPath = 'D:/360Downloads/ide'

while True:
    os.chdir(cascPath)
    faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    ret, frame = cap.read()
    name = find_face_cap(frame)
    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=5,
        minSize=(30, 30)
    )  # flags = cv2.CV_HAAR_SCALE_IMAGE

    cv2_im = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # cv2和PIL中颜色的hex码的储存顺序不同
    pil_im = Image.fromarray(cv2_im)
    draw = ImageDraw.Draw(pil_im)  # 括号中为需要打印的canvas，这里就是在图片上直接打印
    font = ImageFont.truetype("C:/Windows/Fonts/simhei.ttf", 20, encoding='utf-8')  # 第一个参数为字体文件路径，第二个为字体大小
    draw.text((0, 0), name, (0, 0, 255), font=font)  # 第一个参数为打印的坐标，第二个为打印的文本，第三个为字体颜色，第四个为字体
    cv2_text_im = cv2.cvtColor(numpy.array(pil_im), cv2.COLOR_RGB2BGR)

    # font = cv2.FONT_HERSHEY_SIMPLEX
    for (x, y, w, h) in faces:
        nh = h * 1.2
        # print("宽:%d 高:%d"%(w,nh))
        #  cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.ellipse(cv2_text_im, (int(x + w / 2), int(y + h / 2)), (int(w / 2), int(nh / 2)), 0, 0, 360, (0, 255, 0), 2)
        # cv2.putText(cv2_text_im,
        #             name, (int(x + w / 2), int(y + h)), font, 0.6, (0, 0, 255), 2)
    # Display the resulting frame
    cv2.imshow('frame', cv2_text_im)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
