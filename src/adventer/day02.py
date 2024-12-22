import re
import csv
import os
import adventer
import copy


def file_loc(user):
    input_file = os.path.join("share", user, "day02/input.csv")
    test_file = os.path.join("share", user, "day02/test.csv")
    return input_file, test_file



def is_monotonic(s):
    return (all(s[i] <= s[i + 1] for i in range(len(s) - 1))) or (
        all(s[i] >= s[i + 1] for i in range(len(s) - 1))
    )


def is_safe(s):
    return all(abs(s[i] - s[i + 1]) <= 3 for i in range(len(s) - 1)) and all(
        abs(s[i] - s[i + 1]) >= 1 for i in range(len(s) - 1)
    )


def p02():
    user = adventer.parser.parser()
    input_file, test_file = file_loc(user)


    reports = []
    with open(input_file) as file:
        for input_line in file:
            line = [int(val) for val in input_line.split(" ")]
            reports.append(line)

    nsafe_report = 0
    for report in reports:
        for i in range(len(report)):
            report_copy = copy.deepcopy(report)
            report_copy.pop(i)
            if is_monotonic(report_copy) and is_safe(report_copy):
                nsafe_report = nsafe_report + 1
                break

    print(nsafe_report)
