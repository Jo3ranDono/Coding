#!/usr/bin/env python3

# In Python, the bytes.fromhex() function can be used to convert hex to bytes.
# The .hex() instance method can be called on byte strings to get the hex representation.

data = "63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d"

result = bytes.fromhex(data)

print(result)
