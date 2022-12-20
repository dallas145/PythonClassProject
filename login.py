import cv2
import time
from talk import talk

model = cv2.face.LBPHFaceRecognizer_create()
model.read('face_LBPH.yml')
f=open('member.txt','r')
names = f.readline().split(',')

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_frontalface_alt2.xml")
cap=cv2.VideoCapture(0)
cv2.namedWindow('frame',cv2.WINDOW_NORMAL)

timenow = time.time()
while(cap.isOpened()):
    count = 5 - int(time.time() - timenow)
    ret, img = cap.read()
    if ret==True:
        imgcopy = img.copy()
        cv2.putText(imgcopy,str(count),(200,400),cv2.FONT_HERSHEY_SIMPLEX,15,(0,0,255),35)
        cv2.imshow("frame",imgcopy)
        k=cv2.waitKey(100)
        if k == ord("z") or k == ord("Z") or count == 0:
            cv2.imwrite("media/tem.jpg",img)
            break
cap.release()
cv2.destroyAllWindows()

img = cv2.imread("media/tem.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray,1.1,3)
for (x,y,w,h) in faces:
    img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
    face_img = cv2.resize(gray[y: y+h, x: x+w],(400,400))
    try:
        val = model.predict(face_img)
        if val[1]<50:
            print("歡迎 "+ names[val[0]]+' 登入！',val[1])
            talk("歡迎"+ names[val[0]]+' 登入！', "zh-tw")
            time.sleep(2)
        else:
            print("抱歉！你不是會員，無法登入！")
            talk("抱歉！你不是會員，無法登入！", "zh-tw")
            time.sleep(2)
    except:
        print("辨識時產生錯誤！")
        talk("辨識時產生錯誤！", "zh-tw")
        time.sleep(2)