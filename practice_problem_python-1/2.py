#python program sum of cubes of all postive numbers


import math
num=int(input("Enter the limit :"))

sum=0

for i in range(2,num+1,2):
    sum=sum+pow(i,3)

print(f"The cubes of the even number upto the limit :{sum}")

      
