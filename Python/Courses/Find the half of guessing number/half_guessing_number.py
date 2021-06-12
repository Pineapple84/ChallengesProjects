# Find the half of guessing number in range 100.
# IN PROGRESS...

half = 50
guess = input("Guess your number: ")

for guess in range(100):
    print("Is your number is higher or lower?")
    case 'higher':
        half_02 = half + (guess / 2)
    case 'lower':
        half_02 = guess / 4
    case 'equal:
        print("Congrats!!!, We got " + guess)
        
    if guess <= -1 or guess > 100:
        break
