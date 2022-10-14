
from operator import neg


a=[1,-1,-2,2]

def negative(s):
    if s<0:
        return True
    else:
        return False
negativeNum=filter(negative,a)
print(list(negativeNum))
    