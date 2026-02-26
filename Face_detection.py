import cv2
image=cv2.imread("C:/Users/suchi/Downloads/Suchi .jpg")
image =cv2.resize(image,(200,300))
classifier = cv2.CascadeClassifier("C:/Users/suchi/Desktop/CV/haarcascade_frontalface_default.xml")
gray_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
coordinates = classifier.detectMultiScale(gray_image)
for (x,y,w,h) in coordinates:
    cv2.rectangle(image,(x,y),(x+w,y+h),(0,0,255),3)
cv2.imshow("img",image)
while True:
    key =cv2. waitKey(1)
    print(key)
    if key==27:
        cv2.destroyAllWindows()
        break