#!/usr/bin/env python3

def print_fibonacci(length):
    f0 = 0
    f1 = 1
    if length == 0:
        seq = []
    elif length == 1:
        seq = [f0]
    else:
        seq = [f0, f1]
        i = 2
        while i < length:
            seq.append(seq[i-1] + seq[i-2])
            i += 1
    print(seq)