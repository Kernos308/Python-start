def iloczyn(a1=1,r=1,ile=10):
    if ile==1:
        return a1
    return a1*iloczyn(a1+r,r,ile-1)
print(iloczyn(1,2,5))
print(iloczyn())