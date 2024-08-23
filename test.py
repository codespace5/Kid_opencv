import cv2
import imutils
import numpy as np

img = cv2.imread('./images/4.png')
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
#  ([220, 120, 110], [250, 220, 230]),
#  ([120, 140, 225], [225, 229, 255]),
 ([100, 180, 40], [190, 255, 220]),
]

position_list = []

for (lower, upper) in boundaries:
    lower = np.array(lower, dtype='uint8')
    upper = np.array(upper, dtype='uint8')

    mask = cv2.inRange(img, lower, upper)
    output = cv2.bitwise_and(img, img, mask=mask)
    cv2.imshow('dee', output)
    # cv2.imshow('image', np.hstack([image, output]))



    gray = cv2.cvtColor(output, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY)[1]
    cv2.imshow('three', thresh)
    cnts, _ = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # cnts = imutils.grab_contours(cnts)
    print(cnts)
    img = cv2.drawContours(output, cnts, -1, (0,255,0), 1)
    i = 0
    for cnt in cnts:
        i+= 1
        x, y, w, h = cv2.boundingRect(cnt)
        if w < i_w / 20: continue
        if h < i_h / 20: continue
        # output = cv2.rectangle(output, (x, y), (x+w, y+h), (0, 255, 2), 2)
        output = cv2.rectangle(img1, (x, y), (x+w, y+h), (0, 255, 2), 2)
        cv2.imshow('img', img1)
        crop = img1[y:y+h, x:x+w]
        position_list.append([y, y+h, x, x+w])
        cv2.imshow('img', crop)
        cv2.imwrite('./img' + str(x+y) +'.jpg', crop)
        cv2.waitKey(0)
    # for c in cnts:
    #     cv2.drawContours(img, [c], -1, (0, 255, 0), 2)
    cv2.imshow("image", output)
    #     cv2.waitKey(300)
    cv2.waitKey(0)

print("output", position_list)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # blurred = cv2.GaussianBlur(img, (5,5), 0)
    # gray = cv2.cvtColor(blurred, cv2.COLOR_BGR2GRAY)
    # thresh = cv2.threshold(gray, 228, 255, cv2.THRESH_BINARY_INV)[1]
    # thresh = cv2.threshold(output.copy(), 228, 255, cv2.THRESH_BINARY_INV)[1]
    # thresh = cv2.Canny(gray, 12, 200)


    # cnts, _ = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # cnts, _ = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # # cnts = imutils.grab_contours(cnts)
    # # print(cnts)

    # for cnt in cnts:
    #     img = cv2.drawContours(img, cnts, -1, (0,255,0), 1)
    #     x, y, w, h = cv2.boundingRect(cnt)
    #     img = cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 2), 2)
    #     cv2.imshow("img", img)
    # # for c in cnts:
    # #     cv2.drawContours(img, [c], -1, (0, 255, 0), 2)
    # cv2.imshow("image", img)
    # #     cv2.waitKey(300)
    # cv2.waitKey(0)