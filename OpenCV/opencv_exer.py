import cv2
import glob

images = glob.glob("*.jpg")

for i in images:
    img = cv2.imread(i,0)
    resize_img= cv2.resize(img,(100,100))
    cv2.imshow("Hey",resize_img)
    cv2.waitKey(2000)
    cv2.destroyAllWindows()
    cv2.imwrite("resize"+i,resize_img)
