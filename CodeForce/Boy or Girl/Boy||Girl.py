#! /usr/bin/env python3

def find_duplicate(string):
    s = set()
    list = []
    for char in string:
        if char not in s:
            s.add(char)
            list.append(char)
    st =''.join(list)
    if int(len(st)) % 2 == 1:
        print("IGNORE HIM!")
    else:
        print("CHAT WITH HER!")


string = input()
find_duplicate(string)