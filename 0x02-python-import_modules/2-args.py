#!/usr/bin/env python3

import sys

# Check the number of arguments
if len(sys.argv) == 1:
    print("0 arguments.")
elif len(sys.argv) == 2:
    print("1 argument:")
else:
    print(f"{len(sys.argv) - 1} arguments:")

# Print the arguments
for i, arg in enumerate(sys.argv[1:], start=1):
    print(f"{i}: {arg}")
