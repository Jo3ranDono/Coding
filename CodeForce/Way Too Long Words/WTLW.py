#!/usr/bin/env python3

num = int(input())

for i in range(0,num):
    word = str(input())
    length = len(word)
    if length > 10:
        print(word[0], end='')
        print(length-2, end='')
        print(word[length-1])
    else:
        print(word)

