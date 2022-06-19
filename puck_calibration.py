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
