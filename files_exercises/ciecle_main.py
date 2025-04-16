
#from problem3_1 import area  # Import the area function from problem3_1.py

# Step 1: Calculate the area of a circle with radius 5


from circle_utils import calculate_area



radius = 5
area = calculate_area(radius)

file = open("circle_area.txt", "w")
file.write(f"The area of a circle with radius {radius} is {area:.2f}\n")
file.close()

file = open("circle_area.txt", "r")
for line in file:
    print(line, end="") 
file.close()  
