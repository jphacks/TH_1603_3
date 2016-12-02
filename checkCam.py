import cv2,numpy as np

if __name__=="__main__":

    capture = cv2.VideoCapture(0)
    
    if capture.isOpened() is False:
        raise("IO Error")

    cv2.namedWindow("Capture", cv2.WINDOW_AUTOSIZE)
    cascade = cv2.CascadeClassifier('./haarcascade_frontalface_alt.xml')
    while True:

        ret, image = capture.read()

        if ret == False:
            continue
        facerect = cascade.detectMultiScale(image, scaleFactor=1.1,minNeighbors=1,minSize=(1,1))
        if len(facerect) > 0 :
            for face in facerect :
                if face[2] > 150 :
                    x,y,w,h = face[0],face[1],face[2],face[3]
                    #gray_image = cv2.cvtColor(image[y+(h*0.65):y+(h*0.85),x+(w*0.35):x+(w*0.65)],cv2.COLOR_RGB2GRAY);
                    gray_image = cv2.cvtColor(image[y:y+h,x:x+w],cv2.COLOR_RGB2GRAY);
                    arr = np.array(gray_image)
                    ave = np.average(arr)
                    print(ave)
                    bimg = cv2.adaptiveThreshold(gray_image,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,21,2)
                    #cv2.imshow("Capture",gray_image);
                    cv2.imshow("Capture",bimg);
       
        if cv2.waitKey(33) >= 0:
            cv2.imwrite("image.png", image)
            break

    cv2.destroyAllWindows()

