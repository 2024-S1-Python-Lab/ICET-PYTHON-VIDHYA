class Rect:
    def __init__(self, length, breadth):  
        self.l = length
        self.b = breadth
    
    def area(self):
        ar = (self.l * self.b)
        return ar
    
    def perimeter(self):
        p = 2 * (self.l + self.b)
        return 
x1 = int(input("Enter length of first rectangle: "))
y1 = int(input("Enter breadth of first rectangle: "))
r1 = Rect(x1, y1)
print("Area of rectangle 1:", r1.area())   
print("Perimeter of rectangle 1:", r1.perimeter())
x2 = int(input("Enter length of second rectangle: "))
y2 = int(input("Enter breadth of second rectangle: "))
r2 = Rect(x2, y2)  
print("Area of rectangle 2:", r2.area())
print("Perimeter of rectangle 2:", r2.perimeter())
if r1.area() == r2.area():
    print("\nAreas of both rectangles are equal.")
else:
    print("\nAreas of both rectangles are not equal.")

