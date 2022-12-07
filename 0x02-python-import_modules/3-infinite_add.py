#!/usr/bin/env python3

import sys

# Initialize the result variable
result = 0

# Iterate over the arguments and add them to the result
for arg in sys.argv[1:]:
    result += int(arg)

# Print the result
print(result)
