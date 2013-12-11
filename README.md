PyPipe
======

Want to add some python code in a shell pipeline?
This script makes it easy!


Notes
-----
Standard input is read into the variable 'stdin'.

`stdin = sys.stdin.read()`

Return values are printed to the console.

Usage
-----

> % echo BLAARHH | pypipe 'stdin.capitalize()'
> Blaarhh


