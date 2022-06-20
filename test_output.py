outputs = []
i = 0
counter_white = 0
counter_black = 0
counter_green = 0
for index, vals in enumerate(outputs):
    if vals == "1" and outputs[index + 1] == "1":
        counter_white+=1
    if vals == "2" and outputs[index + 1] == "2":
        counter_black+=1
    if vals == "3" and outputs[index + 1] == "3":
        counter_green+=1
for index, two in enumerate(outputs):
    
for index, three in enumerate(outputs):



if counter_white > 5 and counter_black < 5 and counter_green < 5:
    print("white found")
    counter_white = 0
elif counter_black > 5 and counter_white < 5 and counter_green < 5:
    print("black found")
    counter_black = 0
elif counter_green > 5 and counter_black < 5 and counter_green < 5:
    print("green found")
    counter_green = 0


i = 0

for i, vals in enumerate(outputs):
    if vals == outputs[index + 1]:
        if vals == "1":
            white+=1
        elif vals == "2":
        elif vals == "3":

#call method after appending value to outputs to analyze and check for puck change