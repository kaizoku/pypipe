import sys
import string
import operator
import codecs
from functools import reduce

try: ## Attempt hackercodecs import
    import hackercodecs
except ImportError as e:
    pass

def main():
    stdin = sys.stdin.read()
    stdout = sys.stdout

    code = reduce(operator.concat, sys.argv[1:])
    sys.stdout.write(eval(code))
