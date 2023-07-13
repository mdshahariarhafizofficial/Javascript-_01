import math

def triangle_area(a,b,c):
    if (a+b)>c and (b+c)>a and (c+a)> b :
        s = (a+b+c)/2
        area = math.sqrt((s*(s-a)*(s-b)*(s-c)))
        return area
    else:
        print("Triangle area is not possible")

result = triangle_area(10,20,15)
print("Triangle area is: ", result)