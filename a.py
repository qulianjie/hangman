
try:
    a=input("请输入： ")
    a=int(a)
    b=input("请输入： ")
    b=str(b)
    new_string="Yesterday I wrote a {}. I sent it to {}".format(a,b)
    print(new_string)
except(ValueError):
    print("This is not int!")

