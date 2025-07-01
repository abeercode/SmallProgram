num=int(input("enter a number"))

bin=''
while num!=0:
    
    if num%2==0:
        bin=str(0)+bin
    else:
        bin=str(1)+bin

    num=num//2

print(bin)
print(10)
#here again to makesureit well done
#status
