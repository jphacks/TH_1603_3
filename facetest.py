# -*- coding:utf-8 -*-
import numpy
import cv2
cascade_path = './haarcascade_frontalface_alt.xml'
cap = cv2.VideoCapture(0)
for i in xrange(1, 25):
    filename = "%02d.jpg" % i
    ret, frame = cap.read()
    #ファイル読み込み
    image = frame
    #グレースケール変換
    image_gray = cv2.cvtColor(image, cv2.cv.CV_BGR2GRAY)
    #カスケード分類器の特徴量を取得する
    cascade = cv2.CascadeClassifier(cascade_path)
    #物体認識（顔認識）の実行
    facerect = cascade.detectMultiScale(
                    image_gray, scaleFactor=1.1, minNeighbors=1, minSize=(1, 1))
    
    print filename, len(facerect)
    
    if len(facerect) <= 0:
        print 'miss'
        continue
    
    rect = facerect[0]
    for r in facerect:
        if rect[2] < r[2]:
            rect = r
        
    
    x = rect[0]
    y = rect[1]
    w = rect[2]
    h = rect[3]
    
    # img[y: y + h, x: x + w] 
    cv2.imwrite('face_' + filename, image_gray[y:y+h, x:x+w])
    k = cv2.waitKey(200)
    if k == 27: break

cap.release()
