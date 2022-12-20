import cv2
import os, glob
import numpy as np
from time import sleep

def saveImg(image, index, name):
    filename = '../images/' + name + '/face{:03d}.jpg'.format(index)
    cv2.imwrite(filename, image)

def signup(name):
    index=1
    total=100
    #name=input('輸入姓名(使用英文): ')
    if os.path.isdir('../images/'+ name):
        print('此姓名已存在！')
    else:
        os.mkdir('../images/'+name)
        face_cascade = cv2.CascadeClassifier("../haarcascade_frontalface_alt2.xml")
        cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
        cv2.namedWindow('video', cv2.WINDOW_NORMAL)
        while index > 0:
            ret, frame = cap.read()
            frame = cv2.flip(frame,1)
            gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, 1.1,3)
            for (x,y,w,h) in faces:
                frame = cv2.rectangle(frame,(x,y),(x+w,y+h), (0,255,0),3)
                image = cv2.resize(gray[y: y+h, x: x+w],(400, 400))
                saveImg(image, index, name)
                sleep(0.3)
                index+=1
                if index > total:
                    print('取樣完成！')
                    index=-1
                    break
            cv2.imshow('video',frame)
            cv2.waitKey(1)
        cap.release()
        cv2.destroyAllWindows()

    images = []
    labels = []
    labelstr = []
    count = 0
    dirs = os.listdir('../images')
    for d in dirs:
        if os.path.isdir('../images/'+d):
            files = glob.glob('../images/'+d+'/*.jpg')
            for filename in files:
                img = cv2.imread(filename, cv2.COLOR_BGR2GRAY)
                images.append(img)
                labels.append(count)
            labelstr.append(d)
            count+=1
            
    f=open('member.txt','w')
    f.write(','.join(labelstr))
    f.close()

    print('開始建立模型...')
    model = cv2.face.LBPHFaceRecognizer_create()
    model.train(np.asarray(images),np.asarray(labels))
    model.save('face_LBPH.yml')
    print('建立模型完成！')