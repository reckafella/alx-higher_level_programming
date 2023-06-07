#!/usr/bin/python3

sum_ = 0
count = 1
def counter(count, sum_):
    for i in range(-5, 256):
        sum_ += i
        count += 1
    print(sum_)
    print(count)

counter(count, sum_)
