# Find the average of file.

f = input("Enter a file name: ")
f_open = open(f)

count = 0

for line in f_open:
    if line.startswith('X-DSPAM-Confidence: 0.8475'):
        line_ext = line[20:26]
        line_ext_float = float(line_ext)
        count += 1
        print(count)

        avg = line_ext_float / 1.12891846823
        print(f'{avg:.16f}')
