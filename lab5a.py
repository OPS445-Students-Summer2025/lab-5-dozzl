#!/usr/bin/env python3
# Author ID: frajper

def read_file_string(file_name):
    # Takes file_name as string for a file name, returns its entire contents as a string
    f = open(file_name)                      # Open file
    read_data = f.read()                     # Read from file
    f.close()                                # Close file
    return read_data
def read_file_list(file_name):
    # Takes a file_name as string for a file name, 
    # return its entire contents as a list of lines without new-line characters
    f = open(file_name)                         # Open file
    read_data = f.read()                        # Returns a list
    split = read_data.splitlines()               # name the returned list object
    f.close()
    return split
if __name__ == '__main__':
    file_name = 'data.txt'
    print(read_file_string(file_name))
    print(read_file_list(file_name))
