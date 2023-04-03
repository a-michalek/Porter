#! python3

# Script to manage employees´s IDs 

kennitalas = {
    'a1': '123',
    'b1': '456',
}

import sys, pyperclip, time

# Checking if the command has correct number of args.
if len(sys.argv) < 2:
    print("Usage: l.py abbreviation")
    sys.exit()

# Validating if dictionary contains that abbreviation
if sys.argv[1] in kennitalas:
    pyperclip.copy(kennitalas[sys.argv[1]])
    print("Kennitala of " + sys.argv[1] + " was copied, use ctrl + v")
else:
    print("Are you sure " + sys.argv[1] + " is working here?")
    time.sleep(1)

# To do_1: Reading and writing data to CSV file

# To do_2: Accepting names together with abbreviations 

# To do_3: Split it to classes 