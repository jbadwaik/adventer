import os
import adventer
import adventer.parser
import math

def file_loc(user):
    input_file = os.path.join("share", user, "day04/input.csv")
    test_file = os.path.join("share", user, "day04/test.csv")
    return input_file, test_file

def p01():
    print("Day 4 - Part 1")
    
    user = adventer.parser.parser()
    input_file, test_file = file_loc(user)
    
    with open(input_file, "r") as f:
        values = []
        for line in f:
            values.append(line.split(" "))
        print(values)

    xlen = 101
    ylen = 103
    
    uniq_vals = dict()

    for val in values:
        x = int(val[0].split("=")[1].split(",")[0])
        y = int(val[0].split("=")[1].split(",")[1])
        
        vx = int(val[1].split("=")[1].split(",")[0])
        vy = int(val[1].split("=")[1].split(",")[1])

        print (x,y,vx,vy)

        nx = (x + 100 * vx) % xlen
        ny = (y + 100 * vy) % ylen

        if ((nx,ny) in uniq_vals):
            uniq_vals[(nx,ny)] = uniq_vals[(nx,ny)] + 1
        else:
            uniq_vals[(nx,ny)] = 1
    
    print(len(uniq_vals))
    
    first = 0
    second = 0
    third = 0
    fourth = 0
    
    for i in range(0, math.floor(xlen/2)):
        for j in range(0, math.floor(ylen/2)):
            if ((i,j) in uniq_vals):
                print((i,j))
                first = first + uniq_vals[(i,j)]

    for i in range(math.ceil(xlen/2),xlen):
        for j in range(0, math.floor(ylen/2)):
            if ((i,j) in uniq_vals):
                print((i,j))
                second = second + uniq_vals[(i,j)]

    for i in range(0, math.floor(xlen/2)):
        for j in range(math.ceil(ylen/2), ylen):
            if ((i,j) in uniq_vals):
                print((i,j))
                third = third + uniq_vals[(i,j)]

    for i in range(math.ceil(xlen/2),xlen):
        for j in range(math.ceil(ylen/2), ylen):
            if ((i,j) in uniq_vals):
                print((i,j))
                fourth = fourth + uniq_vals[(i,j)]

    print(first)
    print(second)
    print(third)
    print(fourth)
    print (first * second * third * fourth)    

def p02():
    print("Day 4 - Part 2")

    user = adventer.parser.parser()
    input_file, test_file = file_loc(user)
    
    with open(input_file, "r") as f:
        values = []
        for line in f:
            values.append(line.split(" "))
        print(values)

    xlen = 101
    ylen = 103
    
    uniq_vals = dict()

    for i in range(0,10001):

        print(i)
        print(" ")

        uniq_vals = set()
        uniq_vals.clear()
        for val in values:
            x = int(val[0].split("=")[1].split(",")[0])
            y = int(val[0].split("=")[1].split(",")[1])

            vx = int(val[1].split("=")[1].split(",")[0])
            vy = int(val[1].split("=")[1].split(",")[1])

            a = (x + i * vx) % xlen
            b = (y + i * vy) % ylen

            uniq_vals.add((a,b))

        if (i - 166) % ylen == 0 or (i - 183) % xlen == 0:
            for q in range(0,ylen):
                print("")
                for p in range(0,xlen):
                    if ((p,q) in uniq_vals):
                        print("*", end="")
                    else:
                        print(" ", end="")
            x = input()