class Rectangle():
    def __init__(self,a,b,c):
         self.a=a
         self.b=b
         self.c=c
    def calculate_perimeter(self):
         return self.a+self.b+self.c


class Square():
     def __init__(self,w,l):
         self.w=w
         self.l=l
     def calculate_perimeter(self):
         return self.w*2+self.l*2

r=Rectangle(3,2,1)
s=Square(20,30)

print(r.calculate_perimeter())
print(s.calculate_perimeter())
