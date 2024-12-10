test01_file = "share/day02/test01.csv"
input_file = "share/day02/input.csv"

import copy


def is_monotonic(s):
    return (all(s[i] <= s[i + 1] for i in range(len(s) - 1))) or (
        all(s[i] >= s[i + 1] for i in range(len(s) - 1))
    )


def is_safe(s):
    return all(abs(s[i] - s[i + 1]) <= 3 for i in range(len(s) - 1)) and all(
        abs(s[i] - s[i + 1]) >= 1 for i in range(len(s) - 1)
    )


def p02():
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
