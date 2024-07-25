import vex64
import vex32
import os
import sys

is_64bits = sys.maxsize > 2**32
os.system('clear')
if is_64bits:
    vex64.menu()
elif is_32bits:
    vex32.menu()
else:
    print("unknown bit please try again later...")
