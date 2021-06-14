# Find the half of guessing number in range 100.
# IN PROGRESS...

half = 50
part = 4
guess = int(input("Guess your number: "))

for guess in range(100):
    ans = input("Is your number is higher or lower than " + str(half) + " ?")
    
    if ans == "higher":
        value_01 = half + (half / 2)
        print(value_01)
        
    while part <= 200:
        ans_02 = input("Is number is higher or lower than previous number" + " ?")
        if ans_02 == "higher":
            new_val = value_01 + (value_01 / part)
            print(new_val)
            value_01 = new_val
            part *= 2
            continue
        
    if guess <= -1 or guess > 100:
        break
