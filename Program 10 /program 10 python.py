# binary to decimal
a = input("Enter the binary number : ")
from_base = 2
answer = int(a,from_base)
print(answer)
# decimal to binary
a = int(input("enter the decimal number : "))
answer = bin(a)
print(answer[2:])
