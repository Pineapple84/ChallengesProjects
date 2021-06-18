# IN PROGRESS....

half = 50
part = 4
guess = int(input("Guess your number: "))

for guess in range(100):
    ans = input("Is your number is higher or lower than " + str(half) + " ?")
    
    if ans == "higher":
        value = half + (half / 2)
        print(value)
    if ans == "lower":
        value = half / 2
        print(value)
        
    while part <= 200:
        ans_02 = input("Is number is higher or lower than previous number" + " ?")
        if ans_02 == "higher":
            new_val = value + (value / part)
            print(new_val)
            value = new_val
            part *= 2
            continue
        if ans_02 == "lower":
            new_val = value / part
            print(new_val)
            value = new_val
            part *= 2
            continue
        
    if guess <= -1 or guess > 100:
        break
