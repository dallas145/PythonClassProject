import cv2
import os, glob
import numpy as np
from time import sleep
import sqlite3

def saveImg(image, index, name):
    filename = '../images/' + name + '/face{:03d}.jpg'.format(index)
    cv2.imwrite(filename, image)

def getid(name):
    conn = sqlite3.connect('ids.db')
    conn.execute('CREATE TABLE IF NOT EXISTS members ( "id" INTEGER PRIMARY KEY AUTOINCREMENT, "names" TEXT NOT NULL UNIQUE)')
    conn.execute('INSERT INTO members ( names ) VALUES ( {} )'.format('"' + name + '"'))
    coursor = conn.execute('SELECT id FROM members WHERE names={}'.format('"' + name + '"'))
    id0 = coursor.fetchone() 
    print(id0)
    conn.commit()
    conn.close()
    intid = str(id0[0])
    return intid[0]

def signup(name):
    index=1
    total=100
    faces = []
    ids = []
    #name=input('輸入姓名(使用英文): ')
    if os.path.isdir('../images/'+ name):
        print('此姓名已存在！')
    else:
        os.makedirs('../images/'+name)
        id = getid(name)
        face_cascade = cv2.CascadeClassifier("../haarcascade_frontalface_alt2.xml")
        cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
        cv2.namedWindow('video', cv2.WINDOW_NORMAL)
        while index > 0:
            ret, frame = cap.read()
            if ret==True:
                frame = cv2.flip(frame,1)
                print(index)
                gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                face = face_cascade.detectMultiScale(gray)
                for (x,y,w,h) in face:
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
    model.save('faces.yml')
    print('建立模型完成！')