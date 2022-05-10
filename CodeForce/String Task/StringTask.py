#!/usr/bin/env python3

letter = input()

letter =  letter.lower()

dot =""

vowels = [ "A", "O", "Y", "E", "U", "I", "a" , "e" , "i" , "o" , "u" , "y"]

for i in range(0, len(letter)):
    if letter[i] not in vowels:
        dot += "."
        dot += letter[i]

print(dot)
