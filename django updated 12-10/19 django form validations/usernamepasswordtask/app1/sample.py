'''def valid(st):
    l,u,d,s=0,0,0,0
    for i in st:
        if i.isupper():
            u+=1
        if i.islower():
            l+=1
        if i.isdigit():
            d+=1
        if i in '[()[\]{}|\\`~!@#$%^&*_\-+=;:\'",<>./?]':
            s+=1
        
        
    if (l>=1 and s>=1 and d>=1 and u>=1):
        return("valid password")
    else:
        return("invalid password")

st=input("enter the password--->")

print(valid(st))
'''
print(any([]))