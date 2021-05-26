file = input("Enter a file name: ")
readFile = open(file)
print(readFile)
readFile02 = readFile.read()
print(len(readFile02))
readWhole = readFile02[:94625]
print(readWhole)