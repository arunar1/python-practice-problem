#reverse a number

num=input("Enter the number :")

length=len(num)

numrev=""

for i in range(0,length):
    numrev=numrev+num[length-1-i]

numrev=int(numrev)


print(f"\nThe reverse of {num} is {numrev}")
    
