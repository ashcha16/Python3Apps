import cv2

img = cv2.imread("galaxy.jpg",0)

print(type(img))
print(img)
print(img.shape) #rows and column tuple 

resize_img=cv2.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2))) #this requires width and height or columns and rows
cv2.imwrite("Galaxy_re.jpg",resize_img)
cv2.imshow("Galaxy1",img)
cv2.imshow("Galaxy2",resize_img)
cv2.waitKey(0)
cv2.destroyAllWindows()