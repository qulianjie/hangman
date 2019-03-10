class Square():
    square_list=[]

    def __init__(self,s1):
        self.s1=s1
        self.square_list=self.square_list.append(self.s1)
    def print(self):
        print ("""{}by{}by{}by{}""".format(self.s1,self.s1,self.s1,self.s1))

s=Square(20)
s=Square(10)
s=Square(30)
print(s.print())

        
        
    
       
