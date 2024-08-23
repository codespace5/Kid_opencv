import cv2
import numpy as np
import os

def error(img1, img2):
   diff = cv2.subtract(img1, img2)
   err = np.sum(diff**2)
   mse = err/(float(h*w))
   msre = np.sqrt(mse)
   return mse, diff

img = cv2.imread('./output/img0.jpg')
cv2.imshow('11', img)
cv2.waitKey(0)

img_path = os.listdir('./output/')
print(img_path)
for img1_path in img_path:
    for img2_path in img_path:
        if img1_path == img2_path:
            continue
        
        img1 = cv2.imread(img1_path)
        img2 = cv2.imread(img2_path)
        h = img2.shape[0]
        w = img2.shape[1]

        print(w, h)
        img1 = cv2.resize(img1, (w, h))

        img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
        img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)


        cv2.imshow('img', img1)
        cv2.imshow('img1', img2)
        cv2.waitKey(500 )



        match_error12, diff12 = error(img1, img2)

        print("Image matching Error between" + img1_path+ "and" +img2_path+ ":",match_error12)
