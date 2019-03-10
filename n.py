def hangman(word): 
     wrong = 0 
     stages = ["", 
              "________        ", 
              "|               ", 
              "|        |      ", 
              "|        0  I  ", 
              "|       /|\LOVE  ", 
              "|       / \ YOU   ", 
              "|               " 
               ] 
     rletters = list(word) 
     board = ["__"] * len(word) 
     win = False 
     print("欢迎来到为你而死游戏来") 
     while wrong < len(stages) - 1: 
         print("\n") 
         msg = "猜一个字母: " 
         char = input(msg) 
         if char in rletters: 
             cind = rletters.index(char) 
             board[cind] = char 
             rletters[cind] = '$' 
         else: 
             wrong += 1 
         print((" ".join(board))) 
         e = wrong + 1 
         print("\n" 
               .join(stages[0: e])) 
         if "__" not in board: 
             print("You win!") 
             print(" ".join(board)) 
             win = True 
             break 
     if not win: 
         print("\n" 
               .join(stages[0:wrong])) 
         print("You lose! It was {}." 
               .format(word)) 
 
import random
list1=["cat","dog","pig","tiger"]
word=random.choice(list1)
hangman(word)

