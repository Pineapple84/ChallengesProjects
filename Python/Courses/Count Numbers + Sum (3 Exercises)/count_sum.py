# Count numbers from 2 up to 10, 2 skips

i = 2
count = 1

while count <= 10:
    val = i * count
    print(val)
    count += 1
    if val == 10:
        break
print("Goodbye!")


# Count numbers backwards from 10 down to 2, 2 skips

j = 2
count02 = 5

print("Hello!")

while count02 <= 5:
    val02 = j * count02
    count02 -= 1
    print(val02)
    if val02 == 2:
        break
 
 
# Count numbers to 6, them sum all numbers

k = 0
cal = 0

while k <= 6:
    cal += k
    k += 1
print(cal)
