a=[2,-10,-20,-30,45,55]
positiveNum=list(filter(lambda x: True if x>0 else False, map(lambda x: x*-1, a)))
print(positiveNum)
