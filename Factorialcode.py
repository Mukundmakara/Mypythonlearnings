factoNum = input("Enter the factorial Number: ")
factoNum = int(factoNum)
x = 1
for i in range(1, factoNum + 1):
    x *= i
print(x)
