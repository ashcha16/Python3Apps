import cv2

face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

img=cv2.imread("photo.jpg")
img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)#convert the color image to gray scale
faces=face_cascade.detectMultiScale(img_gray, # passing gray scale image improves speed and detection
scaleFactor=1.05, # this value helps in accuracy and should be low for better results
minNeighbors=5) # to tell python how many neighbors to search in image

for x,y,w,h in faces:
    rec_img=cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3) # this will create the rectangle by taking 5 arguments image, x and y coordinates,
                                               #diagnal values by adding width and height,RGB,thickness of rectangle

cv2.imshow("A",rec_img)
print(faces)
cv2.waitKey(0)# 0 means window will not close until pressed any key
cv2.destroyAllWindows()