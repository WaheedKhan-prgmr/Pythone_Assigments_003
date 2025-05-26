# If-Else Statement
x = 10
if x > 0:
    print("Positive number")
elif x == 0:
    print("Zero")
else:
    print("Negative number")

# For Loop
print("For loop example:")
for i in range(5):
    print("i =", i)

# While Loop
print("While loop example:")
count = 0
while count < 3:
    print("count =", count)
    count += 1

# Break and Continue
print("Break and continue example:")
for i in range(5):
    if i == 3:
        break
    if i == 1:
        continue
    print("Loop index:", i)
