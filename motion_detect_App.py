import cv2
from datetime import datetime
import pandas

first_frame = None # A static background and will store first frame in this
status_list = [None,None]
times_list = []

df = pandas.DataFrame(columns=["Start","End"])
video = cv2.VideoCapture(0)


while True:

    check, frame = video.read()
    status = 0
    gray= cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray=cv2.GaussianBlur(gray,(21,21),0)# For blurring the image for better calculation using the best values in parameters

    if first_frame is None:
        first_frame=gray
        continue
    
    delta_frame=cv2.absdiff(first_frame,gray)
    thresh_frame=cv2.threshold(delta_frame,30,255,cv2.THRESH_BINARY)[1] 
    # Above code will create the BW image based on diff if it is greater the 30 and returns tuple so we are taking only second value of tuple
    #now smoothen the image 
    thresh_frame=cv2.dilate(thresh_frame,None,iterations=2)#more the iterations more the smoothness
    #now find the contours in the image, any changes in the image
    (cnts,_)=cv2.findContours(thresh_frame.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

    for cntr in cnts:
        if cv2.contourArea(cntr) < 10000:
            continue
        status = 1

        (x,y,w,h)=cv2.boundingRect(cntr)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)

    status_list.append(status)

    # taking only last two values from the list for identifying the change and to avoid memory issue
    status_list = status_list[-2:] 

    if status_list[-1]==1 and status_list[-2]==0: # to check object entered
        times_list.append(datetime.now())
    if status_list[-1]==0 and status_list[-2]==1: # to check object left
        times_list.append(datetime.now())

    cv2.imshow("Color Image",frame)
    #cv2.imshow("Thresh",thresh_frame)
    #cv2.imshow("Gray",gray)

    key = cv2.waitKey(1)
    
    if key == ord("q"):
        if status==1:
            times_list.append(datetime.now()) 
        break

for i in range(0,len(times_list),2):
    df=df.append({"Start":times_list[i],"End":times_list[i+1]},ignore_index=True)
#print(df)
df.to_csv("CaptureData.csv")

video.release()
cv2.destroyAllWindows()