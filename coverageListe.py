#read ".coverage" files, read inside and make a list
#output must be like this:
# 236912 SGH 116.303
# 212653 SGH 126,3020


import os
import sys
import re

def listeYap():
    # read .coverage files
    for root, dirs, files in os.walk("."):
        for file in files:
            if file.endswith(".coverage"):
                with open(file, 'r') as f:
                    lines = f.readlines()
                    for line in lines:
                        # find the line which contains the word "Total"
                        if re.search("Total", line):
                            # split the line by space
                            line = line.split()
                            # find the first element of the line
                            # and split it by "/"
                            line = line[0].split("/")
                            # print the first element of the line
                            # and the last element of the line
                            print(line[0], line[-1])
                            # if the first element of the line is "SGH"
                            # and the last element of the line is "Total"
                            if line[0] == "SGH" and line[-1] == "Total":
                                # print the first element of the line
                                # and the last element of the line
                                print(line[0], line[-1])
                            # if the first element of the line is "SGH"
                            # and the last element of the line is "Total"
                            if line[0] == "SGH" and line[-1] == "Total":
                                # print the first element of the line
                                # and the last element of the line
                                print(line[0], line[-1])

if __name__ == "__main__":
    listeYap()

    
