import cv2
import numpy as np
import time
import matplotlib.pyplot as plt
import os
from cv2 import THRESH_BINARY
from colorthief import ColorThief
import colorsys

cap = cv2.VideoCapture(1)
white_palette = []
black_palette = []
green_palette = []

while True: 


    _, frame = cap.read()
    cv2.rectangle(frame, (140, 110), (460, 450), (255, 0, 255), 2) #show the middle area
    cv2.imshow("frame", frame)
    frame = cv2.medianBlur(frame,15)
    
    global white
    global black
    global green

    key = cv2.waitKey(1)
    if key == ord('w'): #Left Arrow
        white_cal = cap.read()[1]
        cropcal_white = white_cal[140:600, 110:440]
        cv2.imwrite(r"C:\Users\20211487\Desktop\Year1\Quarter4\DBL\Python DBL\images\white_cal.jpg", cropcal_white)
        color_thief = ColorThief(r"C:\Users\20211487\Desktop\Year1\Quarter4\DBL\Python DBL\images\white_cal.jpg")
        white_palette = color_thief.get_palette(quality=1)
        print(white_palette)
        i = -1
        for r, g, b in white_palette:
            i+=1
            if r > 200 and g > 200 and b > 200:
                white = white_palette[i]
                white = list(white)
                print("Final white")
                print(white)
                break
    
        
    if key == ord('b'): #Down Arrow
        black_cal = cap.read()[1]
        cropcal_black = black_cal[140:600, 110:440]
        cv2.imwrite(r"C:\Users\20211487\Desktop\Year1\Quarter4\DBL\Python DBL\images\black_cal.jpg", cropcal_black)
        color_thief = ColorThief(r"C:\Users\20211487\Desktop\Year1\Quarter4\DBL\Python DBL\images\black_cal.jpg")
        black_palette = color_thief.get_palette(quality=1)
        print(black_palette)
        i = -1
        for r, g, b in black_palette:
            i+=1
            if r < 70 and g < 70 and b < 70:
                black = black_palette[i]
                black = list(black)
                print("final black")
                print(black)
                break


    if key == ord('g'): #Right Arrow
        green_cal = cap.read()[1]
        cropcal_green = green_cal[140:600, 110:440]
        cv2.imwrite(r"C:\Users\20211487\Desktop\Year1\Quarter4\DBL\Python DBL\images\green_cal.jpg", cropcal_green)
        color_thief = ColorThief(r"C:\Users\20211487\Desktop\Year1\Quarter4\DBL\Python DBL\images\green_cal.jpg")
        green_palette = color_thief.get_palette(quality=1)
        print(green_palette)
        i = -1
        for r, g, b in green_palette:
            i+=1
            if r < 150 and g > 125 and b < 150:
                green = green_palette[i]
                green = list(green)
                print("final green")
                print(green)
                calibrated = True
                break    

        white_r = (white[0]) / 255
        white_g = (white[1]) / 255 
        white_b = (white[2]) / 255
        (wh, ws, wv) = colorsys.rgb_to_hsv(white_r, white_g, white_b)
        (wh, ws, wv) = (int(wh * 179), int(ws * 255), int(wv * 255))
        print(wh, ',', ws, ',', wv)

        # high_white_r = (white[0] + 30) / 255
        # high_white_g = (white[1] + 30) / 255
        # high_white_b = (white[2] + 30) / 255
        # (high_wh, high_ws, high_wv) = colorsys.rgb_to_hsv(high_white_r, high_white_g, high_white_b)
        # (high_wh, high_ws, high_wv) = (int(high_wh * 179), int(high_ws * 255), int(high_wv * 255))
        # print(high_wh, ',', high_ws,',', high_wv)

        black_r = (black[0]) / 255
        black_g = (black[1]) / 255
        black_b = (black[2]) / 255
        (bh, bs, bv) = colorsys.rgb_to_hsv(black_r, black_g, black_b)
        (bh, bs, bv) = (int(bh * 179), int(bs * 255), int(bv * 255))
        print(bh, ',' ,bs ,',' , bv)

        # high_black_r = (black[0] + 30) / 255
        # high_black_g = (black[1] + 30) / 255
        # high_black_b = (black[2] + 30) / 255
        # (high_bh, high_bs, high_bv) = colorsys.rgb_to_hsv(high_black_r, high_black_g, high_black_b)
        # (high_bh, high_bs, high_bv) = (int(high_bh * 179), int(high_bs * 255), int(high_bv * 255))
        # print(high_bh, ',', high_bs,',', high_bv)

        green_r = (green[0]) / 255
        green_g = (green[1]) / 255
        green_b = (green[2]) / 255
        (gh, gs, gv) = colorsys.rgb_to_hsv(green_r, green_g, green_b)
        (gh, gs, gv) = (int(gh * 179), int(gs * 255), int(gv * 255))
        print(gh, ',' ,gs ,',' , gv)

        # high_green_r = (green[0] + 30) / 255
        # high_green_g = (green[1] + 30) / 255
        # high_green_b = (green[2] + 30) / 255
        # (high_gh, high_gs, high_gv) = colorsys.rgb_to_hsv(high_green_r, high_green_g, high_green_b)
        # (high_gh, high_gs, high_gv) = (int(high_gh * 179), int(high_gs * 255), int(high_gv * 255))
        # print(high_gh, ',', high_gs,',', high_gv)

        # lower_white = np.array([low_white_g, low_white_r, low_white_b])
        # upper_white= np.array([high_white_g, high_white_r, high_white_b])

        # lower_green = np.array([low_green_g, low_green_r, low_green_b])
        # upper_green = np.array([high_green_g, high_green_r, high_green_b])

        # lower_black = np.array([low_black_g, low_black_r, low_black_b])
        # upper_black = np.array([high_black_g, high_black_r, high_black_b])

        # mask = cv2.inRange(frame, lower_black, upper_black)
        # green_mask = cv2.inRange(frame, lower_green, upper_green)
        # white_mask = cv2.inRange(frame, lower_white, upper_white)

        # kernel = np.ones((5, 5), np.float32)/25
        # mask = cv2.erode(mask, kernel, iterations = 1)
        # green_mask = cv2.erode(green_mask, kernel, iterations = 1)
        # white_mask = cv2.erode(white_mask, kernel, iterations = 1)

        # contour_black, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        # contour_green, _ = cv2.findContours(green_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        # contour_white, _ = cv2.findContours(white_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        # for cnt_white in contour_white:
        #     area_white = cv2.contourArea(cnt_white)
        #     approx_white = cv2.approxPolyDP(cnt_white, 0.01*cv2.arcLength(cnt_white, True), True)

        #     if area_white > 1000:
        #         # print(area_white)
        #         # print("White")
        #         cv2.drawContours(frame, [approx_white], 0, (94, 73, 233), 3)


        # for cnt_black in contour_black:
        #     area_black = cv2.contourArea(cnt_black)
        #     approx_black = cv2.approxPolyDP(cnt_black, 0.01*cv2.arcLength(cnt_black, True), True)

        #     if area_black > 1000:
        #         # print(area_black)
        #         # print("Black")
        #         cv2.drawContours(frame, [approx_black], 0, (56, 201, 186), 3)
                


        # for cnt_green in contour_green:
        #     area_green = cv2.contourArea(cnt_green)
        #     approx_green = cv2.approxPolyDP(cnt_green, 0.01*cv2.arcLength(cnt_green, True), True)

        #     if area_green > 1000:
        #         cv2.drawContours(frame, [approx_green], 0, (113, 250, 152), 3)


        # cv2.imshow("Frame", frame)
        # cv2.imshow("Mask", mask)
        # cv2.imshow("Green Mask", green_mask)
        # cv2.imshow("White Mask", white_mask)

    if key == 27:
        
        break
cap.release()
cv2.destroyAllWindows()





















# '''


# # reading the picture in coloured mode
# image = cv2.imread(, cv2.IMREAD_COLOR)

# # first, count all occurrences of unique colours in your picture
# unique, counts = np.unique(image.reshape(-1, image.shape[2]), axis=0, return_counts=True)

# # then, return the colour that appears the most
# print(max(zip(unique, counts), key=lambda x: x[1]))



# #COLORTHIEF
# from colorthief import ColorThief
# color_thief = ColorThief(cap)
# # get the dominant color
# dominant_color = color_thief.get_color(quality=1)
# print(dominant_color)
# '''


# import cv2
# import numpy as np
# from colorthief import ColorThief

# #Cropping video
# cap = cv2.VideoCapture(1)
# ret, image = cap.read()
# while True :
#     photo = cap.read()[1]           # Storing the frame in a variable photo
#     photo = cv2.flip(photo,1)       # Fliping the photo for mirror view
#     cropu1 = photo[80:400,100:540]      # Top left part of the photo
#     cv2.imshow("cropu1",cropu1)     # It will show cropu1 part in a window     
#     cv2.imshow("Live",photo)        # It will show complete video in a window
#     if cv2.waitKey(50) == 13 :      # Specifying (Enter) button to break the loop
#         break
#     color_thief = ColorThief(photo)
#     # get the dominant color
#     dominant_color = color_thief.get_color(quality=1)
#     print(dominant_color)
# cv2.destroyAllWindows()            # To destroy all windows 




# # Read Frames when color instances > a certain number of pixels
# # Take frame and return 2, 3, 4 based on color
# # If object is not close enough to the color, return 5 
# # If most common color is the background or common color pixel count < it should be, return 1
# # 640x480 camera, box in middle of screen


# if len(cnts) > 0:
 
#     #find the largest contour according to their enclosed area
#     c = max(cnts, key=cv2.contourArea)
 
#     #get the center and radius values of the circle enclosing the contour
#     (x, y), radius = cv2.minEnclosingCircle(c)




#     hi = cap.read()[1]
# cv2.imshow("Window", hi)
# cv2.imwrite(r"C:\Users\20211487\Desktop\Year1\Quarter4\DBL\Python DBL\images\img1.jpg", hi)
# from colorthief import ColorThief
# color_thief = ColorThief(r"C:\Users\20211487\Desktop\Year1\Quarter4\DBL\Python DBL\images\img1.jpg")
# # get the dominant color
# dominant_color = color_thief.get_color(quality=1)
# print(dominant_color)
# crop_center = hi[80:400,100:540]     
# cv2.imshow("cropu1",crop_center)
# palette = color_thief.get_palette(color_count=6)
# print(palette)