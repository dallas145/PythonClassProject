import speech_recognition as sr

r = sr.Recognizer()
r.energy_threshold = 4000
while True:
    try:
        with sr.Microphone() as source:
            print("請開始說話:")
            audio = r.listen(source)
            listen_text=r.recognize_google(audio, language="zh-TW")
            print(listen_text+"\n")
            if listen_text=="結束":
                break
    except sr.UnknownValueError:
        print("語音無法辨識\n")
    except sr.RequestError as e:
        print("語音無法辨識{0}\n".format(e))