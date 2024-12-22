import csv
import os
import adventer

def file_loc(user):
    input_file = os.path.join("share", user, "day01/input.csv")
    test_file = os.path.join("share", user, "day01/test.csv")
    return input_file, test_file


def p01():
    user = adventer.parser.parser()
    input_file, test_file = file_loc(user)

    with open(input_file, "r") as f:
        reader = csv.reader(f, delimiter=" ")
        data = []
        for row in reader:
            data.append(row)

    a = [int(row[0]) for row in data]
    b = [int(row[3]) for row in data]
    a.sort()
    b.sort()

    c = [abs(aval - bval) for aval, bval in zip(a, b)]
    print(sum(c))


def p02():
    user = adventer.parser.parser()
    input_file, test_file = file_loc(user)

    with open(input_file, "r") as f:
        reader = csv.reader(f, delimiter=" ")
        data = []
        for row in reader:
            data.append(row)

    a = [int(row[0]) for row in data]
    a = [int(row[0]) for row in data]
    b = [int(row[3]) for row in data]

    val_array = [val * b.count(val) for val in a]
