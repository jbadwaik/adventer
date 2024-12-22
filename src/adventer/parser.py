
import argparse

def parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("--user",required=True)
    args = parser.parse_args()
    return args.user

