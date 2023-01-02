import pygame
import speech_recognition as sr
from pygame import mixer
from talk import talk
from time import sleep

        

n=0
def tts111():
    mixer.init()
    pygame.display.init()
    sr_flag=True
    while True:
        try:
            for event in pygame.event.get():
                if event.type == pygame.USEREVENT:
                    sr_flag=True
        except:
            pass
        if sr_flag==True:
            try:
                with sr.Microphone() as source:
                    print("說些話吧： ")
                    r=sr.Recognizer()
                    r.energy_threshold = 4000
                    audio = r.listen(source)
                    listen_text=r.recognize_google(audio, language="zh-TW")
                    print(listen_text)
                    # if "報" in listen_text:
                    #     print(report)
                    #     talk(report, 'zh-tw')
                    #     sr_flag=False
                    if "結束" in listen_text or "停止" in listen_text or "拜" in listen_text:
                        talk("再見",'zh-tw')
                        sleep(1)
                        break
                    elif "天氣" in listen_text or "溫度" in listen_text:
                        talk('今天有點冷，小心確診', 'zh-tw')
                        sleep(3)
                    elif "什麼" in listen_text:
                        sth = '我不知道'
                        talk(sth, 'zh-tw')
                        sleep(1)
                        talk('你自己去google', 'zh-tw')
                    else:
                        tttt = len(listen_text)*0.3
                        talk(listen_text,'zh-tw')
                        sleep(tttt)
            except sr.UnknownValueError:
                print("語音無法辨識")
                sr_flag=True
            except sr.RequestError as e:
                print("沒有語音輸入{0}".format(e))
                sr_flag=True