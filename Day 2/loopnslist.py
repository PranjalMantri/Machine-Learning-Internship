# For Loops

for i in range(1, 101):
    print(i)

for i in range(1, 101, 2):
    print(i)

for i in range(30, 10, -2):
    print(i)

num = int(input("Enter a number: "))

# FOR ELSE LOOP

for i in range(0, 100):
    if num == i:
        print("Number Found")
        break
else:
    print("Number not found")
