import re
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


    with open(input_file) as f:
        res = 0;
        matches = re.findall('mul\\([0-9]+,[0-9]+\\)', f.read())
        products =  [[int(b),int(c)] for a,b,c,d in [re.split("\\(|,|\\)",match) for match in matches]]

        for values in products:
            res = res + values[0] * values[1]

        print(res)
