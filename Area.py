class Circle:     # class is delcared
    def __init__(self,r):   #constructor is declared
        self.r=r
    def detail(self):
        Area=3.14*self.r*self.r
        print(f"Area of circle is {Area}")
class Rectangle:
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def info(self):
        formula=self.l*self.b
        print(f"Area of Rectangle is {formula}")
class Triangle:
    def __init__(self,bs,h):
        self.bs=bs
        self.h=h
    def Details(self):
        f=1/2*self.bs*self.h
        print(f'Area of triangle is {f}')
r=int(input("Enter a radius :"))
l=int(input("Enter a length:"))
b=int(input("Enter an breath:"))
bs=int(input("Enter an base:"))

h=int(input("Enter an height:"))
obj=Circle(r)              # we create object 
obj1=Rectangle(l,bs)
obj2=Triangle(b,h)
obj.detail()
obj1.info()
obj2.Details()


