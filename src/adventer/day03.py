import re

input_file = "share/day03/input.txt"

def p01():
    with open(input_file) as f:
        res = 0; 
        matches = re.findall('mul\\([0-9]+,[0-9]+\\)', f.read())
        products =  [[int(b),int(c)] for a,b,c,d in [re.split("\\(|,|\\)",match) for match in matches]]

        for values in products:
            res = res + values[0] * values[1]

        print(res)
