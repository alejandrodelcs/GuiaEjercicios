#!/usr/bin/env python3

data = [[1,2,3],[4,5,6],[7,8,9]]

'''output = []
for i in data:
    for j in i:
        output.append(j)'''

output = [j for i in data for j in i]

print(output)
