import csv
from datetime import datetime
from collections import defaultdict

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during
September 2016.".
"""
durations = defaultdict(int)

for i in range(0, len(calls) -1):
    curDate = datetime.strptime(calls[i][2], '%d-%m-%Y %H:%M:%S')
    if curDate.month == 9 and curDate.year == 2016:
        durations[calls[i][0]] += int(calls[i][3])
        durations[calls[i][1]] += int(calls[i][3])

numWithLongestDuration = max(durations, key=durations.get)

print('{} spent the longest time, {} seconds, on the phone during September 2016.'.format(numWithLongestDuration, durations[numWithLongestDuration]))
