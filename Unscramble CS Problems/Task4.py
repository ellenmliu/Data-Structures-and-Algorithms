import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""
callers = set()
receivers = set()
texters = set()

for call in calls:
    callers.add(call[0])
    receivers.add(call[1])

for text in texts:
    texters.add(text[0])
    receivers.add(text[1])

telemarketers = sorted((callers - receivers) - texters)

print('These numbers could be telemarketers: ')
for number in telemarketers:
    print(number)
