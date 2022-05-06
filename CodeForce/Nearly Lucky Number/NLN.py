#!/bin/bash/env python3

num = input()
count = 0

for digit in num:
    if digit == "4" or digit =="7":
        count = count +1

count2 =0
for digit in str(count):
    if digit == "4" or digit =="7":
        count2 = count2 +1

if count2 == len(str(count)):
    output = "YES"
else:
    output = "NO"

print(output)
