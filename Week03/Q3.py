# Question 3 : Map - calculate the x&y and distance between differents points
point1 = (3,5)
point2 = (7,2)
print(f"Point 1:{point1}\nPoint 2:{point2}\n")

x1, y1 = point1
x2, y2 = point2
print(f"Point 1 - X1: {x1}, Y1: {y1}\nPonit 2 - X2: {x2}, Y2: {y2}\n")

distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
print("Distance Between 2 Points:",distance)
