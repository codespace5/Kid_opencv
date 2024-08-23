import cv2
import imutils
import numpy as np
import os

img = cv2.imread('./images/6.png')
img1 = img.copy()
img_origin = img.copy()
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


# delete_path = os.listdir('./output/')
# for delete_file in delete_path:
#     os.remove(delete_path + delete_file)


#////// blue
#  ([230, 180, 120], [250, 220, 230]),
# /////  ground gray
# ([135, 140, 150], [200, 180, 186]),
# //// pink
# ([190, 130, 185], [230, 210, 240]),
# /// green
# ([140 , 190, 150], [172, 255, 213]),
# /////red pink
# ([135 , 150, 230], [180, 200, 255]),
# ////// yellow
# ([110 , 200, 200], [200, 255, 255]),


boundaries = [
#////// blue
 ([230, 180, 120], [250, 220, 230]),
# /////  ground gray
([135, 140, 150], [200, 180, 200]),
# //// pink
([190, 130, 185], [230, 210, 240]),
# /// green
([140 , 190, 150], [172, 255, 213]),
# /////red pink
([135 , 150, 230], [180, 200, 255]),
# ////// yellow
([110 , 200, 200], [200, 255, 255]),
]

position_list = []
i = 0
for (lower, upper) in boundaries:
    img = img_origin.copy()
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

    for cnt in cnts:
        x, y, w, h = cv2.boundingRect(cnt)
        if w < i_w / 20: continue
        if h < i_h / 20: continue
        # output = cv2.rectangle(output, (x, y), (x+w, y+h), (0, 255, 2), 2)
        output = cv2.rectangle(img1, (x, y), (x+w, y+h), (0, 255, 2), 2)
        # cv2.imshow('img', img)
        crop = img1[y:y+h, x:x+w]
        position_list.append([y, y+h, x, x+w])
        cv2.imshow('img', crop)
        cv2.imwrite('./output/' + str(i) +'.jpg', crop)
        i += 1
        cv2.waitKey(0)
    # for c in cnts:
    #     cv2.drawContours(img, [c], -1, (0, 255, 0), 2)
    cv2.imshow("image", output)
    #     cv2.waitKey(300)
    cv2.waitKey(0)

print("output", position_list)




def error(img1, img2):
   diff = cv2.subtract(img1, img2)
   err = np.sum(diff**2)
   mse = err/(float(h*w))
   msre = np.sqrt(mse)
   return mse, diff

img_path = os.listdir('./output/')
path = './output/'
similarity = 1000
object1 = ''
object2 = ''
for img1_path in img_path:
    for img2_path in img_path:
        if img1_path == img2_path:
            continue
        
        img1 = cv2.imread(path + img1_path)
        img2 = cv2.imread(path + img2_path)
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
        if(similarity >= match_error12):
            similarity = match_error12
            object1 = img1_path
            object2 = img2_path
            
print("11111111111111", similarity, object1, object2)

pos1 = int(object1[:-4])
pos2 = int(object2[:-4])

print('22222222222222', position_list[pos1], position_list[pos2])

# result = cv2.rectangle(img_origin, (x, y), (x+w, y+h), (0, 255, 2), 2)

result = cv2.rectangle(img_origin, (position_list[pos1][2], position_list[pos1][0]), (position_list[pos1][3], position_list[pos1][1]), (0, 255, 2), 2)
result = cv2.rectangle(img_origin, (position_list[pos2][2], position_list[pos2][0]), (position_list[pos2][3], position_list[pos2][1]), (0, 255, 2), 2)
cv2.imshow('result', result)

cv2.waitKey(0)
