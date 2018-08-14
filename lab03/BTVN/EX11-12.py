def is_inside(point,rectangle):
    max_x = rectangle[0] + rectangle[2]
    max_y = rectangle[1] + rectangle[3]

    if rectangle[0] <= point[0] <= max_x and rectangle[1] <= point[1] <= max_y:
        return True
    else:
        return False 




a = is_inside([100, 120], [140, 60, 100, 200])
if a == False:
    print("Your funtion is correct")
else:
    print("Bug detected")

b = is_inside([200, 120], [140, 60, 100, 200])
if b:
    print("Your funtion is correct")
else:
    print("Bug detected")