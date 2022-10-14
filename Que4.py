a=["Raj","243","89"]
def positive(num):
    if(num.isalpha()):
        return False
    else:
        return True
positiveNum=list(filter(positive,a))
print(positiveNum)