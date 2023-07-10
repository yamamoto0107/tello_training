#https://terra-1-g.djicdn.com/2d4dce68897a46b19fc717f3576b7c6a/Tello%20%E7%BC%96%E7%A8%8B%E7%9B%B8%E5%85%B3/For%20Tello/Tello%20SDK%20Documentation%20EN_1.3_1122.pdf
#送信基礎

import socket
import time

add = ('192.168.10.1',8889)
camera = 'udp://@0.0.0.0:11111'

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(('',8889))
def send(com):
    s.sendto(com.encode('utf-8'),add)
send('command')
time.sleep(1)
send('streamon')
time.sleep(1)
import cv2
import sys
import os
sys.stderr=os.devnull
cap = cv2.VideoCapture(camera)#0でPCカメラ。.mp4でビデオ。URLで通信先データ

while True:
    try:
        ret,frame = cap.read()
        cv2.imshow('',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    except:
        pass
cap.release()
cv2.destroyAllWindows()
s.close()
