sides = []
for i in range(3):
    sides.append(float(input(f"Enter the length of side {i+1}: ")))

sides.sort() 
if sides[0]**2 + sides[1]**2 == sides[2]**2:
    print("The triangle is a right triangle.")
else:
    print("The triangle is not a right triangle.")
