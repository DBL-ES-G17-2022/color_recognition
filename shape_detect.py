import cv2
import numpy as np
import time
import matplotlib.pyplot as plt
import os
from cv2 import THRESH_BINARY
import socket
from pipes import Pipes

from simulation_camera import SimulationCamera

IS_SIMULATION = os.getenv("RIOL_SIMULATION", False)    

if not IS_SIMULATION:
    cap = cv2.VideoCapture(0)
else:
    simulation_camera = SimulationCamera()


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip = '192.168.47.1'# '192.168.47.1'
port = 11334

#s.connect((ip, port))

outputs = []

black_detected = False
white_detected = False
green_detected = False


def get_frame():
    if not IS_SIMULATION:
        _, frame = cap.read()
        return frame[100:400, 140: 420]
    return simulation_camera.get_frame()
    


while True:


    frame = get_frame()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    

    #Filters
    hsv = cv2.medianBlur(hsv,15)

    # if white_count > 0:
    #     white_count -= 0.1
    # if black_count > 0:
    #     black_count -= 0.1
    # if green_count >0:
    #     green_count -= 0.1
    

    #define range for black HSV values (requires calibration)
    lower_black = np.array([0 , 0 , 0])
    upper_black = np.array([100 , 80 , 90])

    lower_green = np.array([40 , 40 , 40])
    upper_green = np.array([90 , 255 , 255])

    lower_white = np.array([20 , 0 , 230])
    upper_white = np.array([255 , 255 , 255])


    #create mask for black objects using the bounds
    mask = cv2.inRange(hsv, lower_black, upper_black)
    green_mask = cv2.inRange(hsv, lower_green, upper_green)
    white_mask = cv2.inRange(hsv, lower_white, upper_white)
    # res_white = cv2.bitwise_and(frame, frame, mask = white_mask)
    # res_green = cv2.bitwise_and(frame, frame, mask = green_mask)
    # res = cv2.bitwise_and(frame, frame, mask = mask)

    
    #erode the mask as a rectangle for better visualization
    kernel = np.ones((15, 15), np.float32)/225
    mask = cv2.erode(mask, kernel, iterations = 1)
    green_mask = cv2.erode(green_mask, kernel, iterations = 1)
    white_mask = cv2.erode(white_mask, kernel, iterations = 1)

    #contour detection
    contour_black, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contour_green, _ = cv2.findContours(green_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contour_white, _ = cv2.findContours(white_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    #Draw contours 

    new_white_detected = False
    for cnt_white in contour_white:  
        area_white = cv2.contourArea(cnt_white)
        approx_white = cv2.approxPolyDP(cnt_white, 0.01*cv2.arcLength(cnt_white, True), True)

        x,y,w,h = cv2.boundingRect(cnt_white)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)

        if area_white > 7000:
            cv2.drawContours(frame, [approx_white], 0, (255, 105, 180), 3)
            outputs.append("1")
            # print("White")
            # (print(area_white))
            # white_count+=1
            # print("white: ", white_count)
            # if white_count > 5:
            #     new_white_detected = True

            #     if not white_detected: 
            #         print("found")
            #         print(" 1")
            #         white_detected = True
            #         white_count = 0
            #         break
        else:
            print("0")
    
    if not new_white_detected:
        white_detected = False

    for cnt_black in contour_black:
        area_black = cv2.contourArea(cnt_black)
        approx_black = cv2.approxPolyDP(cnt_black, 0.01*cv2.arcLength(cnt_black, True), True)

        x,y,w,h = cv2.boundingRect(cnt_black)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)

        if area_black > 7000:
            cv2.drawContours(frame, [approx_black], 0, (255, 105, 180), 3)
            outputs.append("2")
            # print("Black")
            # (print(area_black))        
            # black_count +=1
            # print("black", black_count)
            # if black_count > 5:
            #     print("found")
            #     print("2")
            #     break
            #     # s.sendall(b"1")
        else:
            print("0")


    for cnt_green in contour_green:
        area_green = cv2.contourArea(cnt_green)
        approx_green = cv2.approxPolyDP(cnt_green, 0.01*cv2.arcLength(cnt_green, True), True)

        x,y,w,h = cv2.boundingRect(cnt_green)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        
        if area_green > 5000:
            cv2.drawContours(frame, [approx_green], 0, (255, 105, 180), 3)
            outputs.append("3")
            # print("Green")
            # (print(area_green))
            # green_count +=1
            # print("green :", green_count)
            # if green_count > 5:
            #     print("found")
            #     print("3")
            #     if green_count > 10:
            #         break
        else:
            print("0")



            
    #show all needed windows
    cv2.imshow("Frame", frame)
    cv2.imshow("Mask", mask)
    cv2.imshow("Green Mask", green_mask)
    cv2.imshow("White Mask", white_mask)
    # ultra_res = res_green + res_white + res 
    # cv2.imshow("Result", ultra_res)
    #ultra_mask = mask + green_mask + white_mask
    #cv2.imshow("All Mask", ultra_mask)

    
    #esc to close windows
    key = cv2.waitKey(1)
    if key == 27:
        
        break
if not IS_SIMULATION:
    cap.release()
cv2.destroyAllWindows()