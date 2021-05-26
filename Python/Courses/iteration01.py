t = 'true'
summ = 0
count = 0

while t == 'true':
    num = input("Enter number: ")
    print(num)
    summ = summ + int(num)
    count = count + 1
    if int(num) < -67332 or int(num) > 356804251:
        try:
            print("Invalid input")
            break
        except:
            continue
    finish = input("Are you finished?: ")
    if finish == 'y':
        avg = summ / count
        print("Total: " + str(summ))
        print("Count: " + str(count))
        print("Average: " + str(avg))
        else:
            continue











  if num_int < -67332 or num_int > 356804251:
        try:
            print("Invalid input")
        except:
            continue
    finish = input("Are you finished?: ")
    if finish == 'done':
        continue
        if largest == None or int(largest) < num_int: 
        	largest = num_int
        print("Maximum is " + str(largest))
        if smallest == None:
            smallest = num_int
        elif int(smallest) < num_int:
            smallest = num_int
        print("Minimum is " + str(smallest))



while True:
	num = input("Enter number: ")
	num_int = int(num)
	if num_int < -67332 or num_int > 356804251:
		try:
			print("Invalid input")
		except:
            continue
			num_str = input("Are you done?: ")
			if num_str == 'done':
                if num_int > -67332 or num_int < 356804251:
				if largest == None or largest < num_int: 
					largest = num_int
				if smallest == None:
					smallest = num_int
				elif smallest < num_int:
					smallest = num_int
                    
				print("Maximum is " + str(largest))
				print("Minimum is " + str(smallest))
                break

