import cv2
import imutils
import numpy as np

img2 = cv2.imread('./images/4.png')
img = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
img1 = img.copy()
# grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# cv2.imshow("iamge",grey)
# cnts = cv2.findContours(grey, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
# cnts = imutils.grab_contours(cnts)
# for c in cnts:
#     cv2.drawContours(img, [c], -1, (0, 255, 0), 2)
#     cv2.imshow("images", img)
#     cv2.waitKey(300)
# cv2.waitKey(0)


(i_h, i_w, c) = img.shape


# boundaries = [
# 	([17, 15, 100], [50, 56, 200]),
# 	([86, 31, 4], [220, 88, 50]),
# 	([25, 146, 190], [62, 174, 250]),
# 	([103, 86, 65], [145, 133, 128])
# ]
boundaries = [
	# ([180, 180, 180], [255, 255, 255]),
 ([90, 180, 200], [180, 250, 255]),

]

for (lower, upper) in boundaries:
    lower = np.array(lower, dtype='uint8')
    upper = np.array(upper, dtype='uint8')

    mask = cv2.inRange(img, lower, upper)
    output = cv2.bitwise_and(img, img, mask=mask)
    cv2.imshow('dee', output)
    # cv2.imshow('image', np.hstack([image, output]))



    gray = cv2.cvtColor(output, cv2.COLOR_RGB2GRAY)
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY)[1]
    cv2.imshow('three', thresh)
    cnts, _ = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # cnts = imutils.grab_contours(cnts)
    print(cnts)
    img = cv2.drawContours(output, cnts, -1, (0,255,0), 1)
    for cnt in cnts:
        
        x, y, w, h = cv2.boundingRect(cnt)
        if w < i_w / 20: continue
        if h < i_h / 20: continue
        output = cv2.rectangle(output, (x, y), (x+w, y+h), (0, 255, 2), 2)
        output = cv2.rectangle(img1, (x, y), (x+w, y+h), (0, 255, 2), 2)
        cv2.imshow('img', img1)
    # for c in cnts:
    #     cv2.drawContours(img, [c], -1, (0, 255, 0), 2)
    cv2.imshow("image", output)
    #     cv2.waitKey(300)
    cv2.waitKey(0)
    
    
    
    
    
    
    
    