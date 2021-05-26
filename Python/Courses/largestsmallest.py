# Find the maximun number and minimum number.

t = 'True'
largest = None
smallest = None

while t == 'True':
    num = input("Enter number: ")
    num_int = int(num)
    finish = input("Are you finished?: ")
    if finish == 'n':
        if num_int > -67332 or num_int < 356804251:
            if largest == None or largest < num_int: 
        	    largest = num_int
            if smallest == None or smallest > num_int:
                smallest = num_int
        if num_int < -67332 or num_int > 356804251:
            print("Invalid input")
            break
    if finish == 'done':
        print("Maximum is " + str(largest))
        print("Minimum is " + str(smallest))
