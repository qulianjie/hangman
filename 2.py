class Hexagon():
    def  __init__(self,a,b,c,d,e,f):
        self.a=a
        self.b=b
        self.c=c
        self.d=d
        self.e=e
        self.f=f
    

    
    def cacculate_perimeter(self):
        return self.a+self.b+self.c+self.d+self.e+self.f

        
hexagon=Hexagon(1,2,3,1,4,3)
print(hexagon.cacculate_perimeter())
