#!/usr/bin/python3

def uppercase(str):
    for i in str:
        if ord(i) >= 97 and ord(i) <= 122:
            if i != str[len(str) - 1]:
                print("{}".format(chr(ord(i) + 32)), end="")
            else:
                print("{}".format(chr(ord(i) + 32)))
        else:
            pass
