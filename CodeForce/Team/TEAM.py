#! /usr/bin/env python3

problems = int(input())
count = 0
for i in range(0,problems):
    x = input()
    if x.count("1") >= 2:
        count += 1
print(count)