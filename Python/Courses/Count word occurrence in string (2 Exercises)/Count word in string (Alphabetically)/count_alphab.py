# Count the longest string alphabetically -> 'beggh'

alphabet = 'abcdefgkijlmnopqrstuvwxyz'
s = 'azcbobobegghakl'
string = ""
count = 0

while count <= len(alphabet):
    count += 1
    find_b = s.find('b')
    if s[find_b] <= s[find_b+1]:
        string = s[find_b+4:s.find('h')+1]    
    else:
        string = s[find_b]
print(string)
