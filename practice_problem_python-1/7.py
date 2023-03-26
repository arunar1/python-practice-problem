
num = int(input("Enter a number: "))

sum = 0

num_str = str(num)

for digit in num_str:
    sum += int(digit)**len(num_str)

if sum == num:
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")
