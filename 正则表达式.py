import re
text = """
       Giraffes have aroused the curiosity of __PLURAL_NOUN__ since earliest times. The giraffe is the
       tallest of all living __PLURAL_NOUN__, but scientists are unable to explain how it got its long
       __PART_OF_THE_BODY__. The giraffe's tremendous height, which might reach __NUMBER__ __PLURAL_NOUN__,
       comes from its legs and __BODYPART__.
       """
def game(msl):
    hit=re.findall("__.*?__",msl)
    if hit is not None:
        for word in hit:
            new_word=input("enter a {}".format(word))
            msl=msl.replace(word,new_word,1)
        print("\n")
        print(msl)
    else:
        print("无效字符")
            

game(text)
