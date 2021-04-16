current_speed = float(input("What is your current speed: "))
speed_allowed = float(input("What was the avg speed allowed on the road: "))
diff = current_speed - speed_allowed
points = diff // 5
if current_speed <= speed_allowed:
    print("Ok")
elif points <= 12 :
    print("Points: " + str(points))
else :
    print("You are going to jail")
