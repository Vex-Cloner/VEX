import vex64
import vex32
import os
import sys

is_64bits = sys.maxsize > 2**32
os.system('clear')
if is_32bits:
    os.system("python vex32.py")
elif is_64bits:
    os.system("python vex64.py")
else:
    print("unknown bit please try again later...")
