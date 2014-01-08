import sys
import string
import operator
import argparse
import codecs
from functools import reduce

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", action="append", dest="imports", help="module to import")
    parser.add_argument("code", action="append", help="code to execute")
    args = parser.parse_args()
    if not args.code:
        parser.error("Must include code to execute.")

    ## load modules in imports
    globals().update({i: __import__(i) for i in args.imports})

    ## set some helpful variables
    stdin = sys.stdin.read()
    stdout = sys.stdout

    code = reduce(operator.concat, args.code)
    sys.stdout.write(eval(code))
