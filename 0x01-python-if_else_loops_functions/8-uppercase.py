#!/usr/bin/python3

def uppercase(str):
    for i in str:
        if ord(i) >= 97 and ord(i) <= 122:
            print("{}".format(chr(ord(i) - 32)))
        else:
            if ord(i) >= 65 and ord(i) <= 90:
                print("{}".format(chr(ord(i))))
            else:
                pass
