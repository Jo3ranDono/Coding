#!/usr/bin/env python3

data = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]

# chr() take only an integer value

for i in data:
    # Convert ASCII-based number to character.
    letter = chr(i)
    print(letter)
