import csv

test01_file = "share/day01/test01.csv"
input_file = "share/day01/input.csv"

def main():
    with open(input_file, 'r') as f:
        reader = csv.reader(f, delimiter=' ')
        data = []
        for row in reader:
            data.append(row)

    a = [ int(row[0]) for row in data]
    b = [ int(row[3]) for row in data]
    a.sort()
    b.sort()


    c = [abs(aval - bval) for aval, bval in zip(a, b)]
    print(sum(c))


