import cv2
import numpy as np
import time
import matplotlib.pyplot as plt
import os
from cv2 import THRESH_BINARY

cap = cv2.VideoCapture(1)

while True:
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    

    #Filters
    hsv = cv2.medianBlur(hsv,15)
    

    #define range for black HSV values (requires calibration)
    lower_black = np.array([0, 0, 0])
    upper_black = np.array([255,255,50])

    lower_green = np.array([50,100,50])
    upper_green = np.array([90, 255, 255])

    lower_white = np.array([0, 0, 230])
    upper_white = np.array([255, 230, 255])


    #create mask for black objects using the bounds
    mask = cv2.inRange(hsv, lower_black, upper_black)
    green_mask = cv2.inRange(hsv, lower_green, upper_green)
    white_mask = cv2.inRange(hsv, lower_white, upper_white)
    res_white = cv2.bitwise_and(frame, frame, mask = white_mask)
    res_green = cv2.bitwise_and(frame, frame, mask = green_mask)
    res = cv2.bitwise_and(frame, frame, mask = mask)
    
    #erode the mask as a rectangle for better visualization
    kernel = np.ones((15, 15), np.float32)/225
    gray = cv2.dilate(mask,kernel,iterations = 1)
    mask = cv2.erode(mask, kernel, iterations = 1)
    green_mask = cv2.erode(green_mask, kernel, iterations = 1)
    white_mask = cv2.erode(white_mask, kernel, iterations = 1)

    #contour detection
    contour_black, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contour_green, _ = cv2.findContours(green_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contour_white, _ = cv2.findContours(white_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    #Draw contours 
    for cnt_black in contour_black:
        area_black = cv2.contourArea(cnt_black)
        #approx for sharper and more accurate contours
        approx_black = cv2.approxPolyDP(cnt_black, 0.01*cv2.arcLength(cnt_black, True), True)

        if area_black > 150:
            cv2.drawContours(frame, [approx_black], 0, (255, 105, 180), 3)
            hi = cap.read()[1]
            crop_center = hi[80:400,100:540]  
            cv2.imshow("crop", crop_center)
            cv2.imwrite(r"C:\Users\20211487\Desktop\Year1\Quarter4\DBL\Python DBL\images\img1.jpg", hi)


    for cnt_green in contour_green:
        area_green = cv2.contourArea(cnt_green)

        approx_green = cv2.approxPolyDP(cnt_green, 0.01*cv2.arcLength(cnt_green, True), True)

        if area_green > 50:
            cv2.drawContours(frame, [approx_green], 0, (255, 105, 180), 3)


    for cnt_white in contour_white:
        white_detected = False
        
        area_white = cv2.contourArea(cnt_white)

        approx_white = cv2.approxPolyDP(cnt_white, 0.01*cv2.arcLength(cnt_white, True), True)

        if area_white > 150:
                cv2.drawContours(frame, [approx_white], 0, (255, 105, 180), 3)

    #show all needed windows
    cv2.imshow("Frame", frame)
    #cv2.imshow("Mask", mask)
    cv2.imshow("Green Mask", green_mask)
    #cv2.imshow("White Mask", white_mask)
    ultra_res = res_green + res_white + res 
    cv2.imshow("Result", ultra_res)
    #ultra_mask = mask + green_mask + white_mask
    #cv2.imshow("All Mask", ultra_mask)

    
    #esc to close windows
    key = cv2.waitKey(1)
    if key == 27:
        
        break
cap.release()
cv2.destroyAllWindows()




#Implement later
'''
    black_detected = False
    white_detected = False
    green_detected = False

    if black_detected:
        print("1")
    
    if white_detected:
        print("2")

    if green_detected:
        print("3")
'''