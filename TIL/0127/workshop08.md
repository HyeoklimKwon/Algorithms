## Q.1

```python
class Point :
    def __init__(self, x , y) :
        self.x = x
        self.y = y
        
class Rectangle :
    def __init__(self,point1,point2):
        self.point1_x = point1.x
        self.point1_y = point1.y
        self.point2_x = point2.x
        self.point2_y = point2.y
        
    
    def get_area(self) :
        return abs(self.point1_x - self.point2_x)*abs(self.point1_y - self.point2_y)
    
    def get_perimeter(self):
        return 2*(abs(self.point1_x - self.point2_x)+abs(self.point1_y - self.point2_y))
    def is_square(self):
        if abs(self.point1_x - self.point2_x) == abs(self.point1_y - self.point2_y):
            return True
        else :
            return False
        
        
p1 = Point(1,3)
p2 = Point(3,1)
r1 = Rectangle(p1,p2)

p3 = Point(3,7)
p4 = Point(6,4)
r2 = Rectangle(p3,p4)

print(r1.get_area())
print(r1.get_perimeter())
print(r1.is_square())

print(r2.get_area())
print(r2.get_perimeter())
print(r2.is_square())

#4
#8
#True
#9
#12
#True
```

