import vex64
import vex32
import os
import sys

# Check if the platform is 64-bit
is_64bits = sys.maxsize > 2**32
import os, platform, time, sys
os.system('clear')
if is_64bits:
    vex64.menu()
    # Perform 64-bit specific operations or imports here
else:
    vex32.menu()
