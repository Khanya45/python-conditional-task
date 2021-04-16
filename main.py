# dog_name = ('choc', 'patrick', 'bobbie' )
# print("Hi there" +" "+dog_name[2])

# initialising variables
_pi = 3.14 # constant variable
iradius = int(input("insert a radius "))

# calculations
area = round(_pi*iradius**2 , 2)  # calculating area of a circle using user's input
diameter = iradius*2 # calculating diameter of a circle
cmf = round(2*_pi*iradius , 2) # calculating circumference of a circle

# converting an int to str (print can only display str data type)
print("Area of a circle: " + str(area) + "cm^2")
print("Diameter of a circle: " + str(diameter) + "cm")
print("Circumference of a circle: " + str(cmf) + "cm")
