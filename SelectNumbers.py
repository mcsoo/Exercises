#__author__ = "ClaytonBat"

import random

def Num( ):
    l = ""
    pots =list(range(46))
    x = 0 
    while x < 7:
        pick = random.randrange(1,46)
        for i in pots:
            if pick == i:
                break
            else:
                continue
            
        l += str(pick) + ","
        x +=1
            
    return l

print (Num())
