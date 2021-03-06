import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records?
Print a message:
"There are <count> different telephone numbers in the records."
"""

phoneNumbers = set()

for index in range(0, len(texts) - 1):
    phoneNumbers.add(texts[index][0])
    phoneNumbers.add(texts[index][1])

for index in range(0, len(calls) - 1):
    phoneNumbers.add(calls[index][0])
    phoneNumbers.add(calls[index][1])

print('There are {} different telephone numbers in the records.'.format(len(phoneNumbers)))
