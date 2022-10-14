num=[1,2,3,4,5]
odd=[]
def oddFind(x):
    if(x%2!=0):
        return True
    else:
        return False
odd=filter(oddFind,num)
print(list(odd))