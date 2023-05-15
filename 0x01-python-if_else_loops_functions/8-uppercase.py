#!/usr/bin/python3
def islower(c):
    if (ord(c) >= 97 and ord(c) <= 122):
        return True
    else:
        return False


def uppercase(str):
    for i in str:
        print("{:c}".format((ord(i)-32) if islower(i) else ord(i)), end='')
    print()


uppercase("Mercy")
