#!/usr/bin/env python3
# Author ID: frajper

def add(number1, number2):
    # Add two numbers together, return the result, if error return string
    try:
        result = float(number1) + float(number2)
        return result
    except:
        return 'error: could not add numbers'

def read_file(filename):
    # Read a file, return a list of all lines, if error return string
    try:
        f = open(filename, 'r')
        lines = f.readlines()
        f.close()
        return lines
    except:
        return 'error: could not read file'

if __name__ == '__main__':
    print(add(10,5))
    print(add('10',5))
    print(add('abc',5))
    print(read_file('seneca2.txt'))
    print(read_file('file10000.txt'))
