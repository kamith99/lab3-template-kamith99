#!/usr/bin/env python3
'''Lab 3 Part 3 script - free disk space'''
# Author ID: bkamith@myseneca.ca

import subprocess

def free_space():
    # Run the system command to get free disk space
    p = subprocess.Popen(
        ["df -h | grep '/$' | awk '{print $4}'"],
        stdout=subprocess.PIPE, 
        stderr=subprocess.PIPE,
        shell=True
    )
    output, _ = p.communicate()
    # Decode the output to a UTF-8 string and strip any newline characters
    return output.decode('utf-8').strip()

if __name__ == '__main__':
    print(free_space())
