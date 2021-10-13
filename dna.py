
from sys import argv
from cs50 import get_string

if len(argv) != 3:
    print('Enter the correct form ')
    exit(1)

dataf = open(argv[1], 'r')
STRs = []
name = {}

for i, row in enumerate(dataf):
    if i == 0:
        STRs = [STR for STR in row.strip().split(',')][1:]
        print(STRs)
    else:
        curr_row = row.strip().split(',')
        name[curr_row[0]] = [int(x) for x in curr_row[1:]]
        print(name[curr_row[0]])
seqr = open(argv[2], 'r').read()
final_STR = []

for STR in STRs:
    i = 0 
    max_STR = -1 
    curr_max = 0
    while i < len(seqr):
        curr_wind = seqr[i: i + len(STR)]
        if curr_wind == STR:
            curr_max += 1
            max_STR = max(max_STR, curr_max)
            i += len(STR)
        else:
            curr_max = 0
            i += 1
    final_STR.append(max_STR)

for names, data in name.items():
    if data == final_STR:
        print(names)
        exit(0)
print('No match')    