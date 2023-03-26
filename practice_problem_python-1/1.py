#python program to find the sum of even numbers from N given integer

num=int(input("Enter the number of element :"))
sum=0
for i in range(0,num):
    c=int(input())
    if c%2==0:
        sum=sum+c

print(f"sum of even number upto given limit :{sum}")
