import sys
import string
import operator
import codecs
from functools import reduce

def main():
    stdin = sys.stdin.read()
    stdout = sys.stdout

    code = reduce(operator.concat, sys.argv[1:])
    sys.stdout.write(eval(code))
