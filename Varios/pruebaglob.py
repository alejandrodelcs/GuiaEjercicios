#!/usr/bin/env python3
import glob

read_files = glob.glob("*.csv")
print(read_files)

with open("result.csv", "wb") as outfile:
    for f in read_files:
        with open("prueba.csv", "w") as infile:
            outfile.write(infile.read())