#prime number less than 1000

for i in range(2,1000):
    flag=1
    if i==2:
        continue
    for j in range(2,i):
        if i%j==0:
            flag=0
            break
    if(flag==1):
        print(i,end=" ")
            
    
