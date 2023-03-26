#count even and odd numbers

num=int(input("Enter the number of element :"))

counteven=0
countodd=0

while num>0:
    num1=int(input())
    if num1%2==0:
        counteven=counteven+1
    elif num1%2==1:
        countodd+=1

    num=num-1
        

print(f"number of even numbers :{counteven}\nNumber of odd numbers :{countodd}")

    
