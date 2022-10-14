alpha=['a','e','i','o','u','r','j','s']
def vow(a):
    if(a=='a' or a=='i' or a=='o' or a=='u' or a=='e'):
        return True
    else:
        return False
vowels=list(filter(vow,alpha))
print(vowels)
    