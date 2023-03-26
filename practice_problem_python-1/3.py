# question 3

num=input("Enter the numbers 4 integer -ve and +ve values :")

#initializing the values
sumpos=0
countpos=0
countneg=0
sumneg=0
#splitting the numbers
num=num.split(" ")
length=len(num)   

for i in range(0,length):
    #to avoid the space during the input
    if num[i]=='':
        continue;
    num[i]=int(num[i])
    #comparing the number is positive or negative
    if num[i]>0:
        sumpos=sumpos+num[i]
        countpos=countpos+1
    else:
        sumneg=sumneg+num[i]
        countneg=countneg+1

#to avoid division by zero error
if countpos==0:
    countpos=1
    
if countneg==0:
    countneg=1
    
print(f"\nsum of positive numbers   {sumpos}   and average is   {sumpos/countpos}")

print(f"\nsum of negative numbers   {sumneg}   and average is   {sumneg/countneg}")
 
