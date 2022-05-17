#!/usr/bin/env python3

from base64 import b64encode

data = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"

result = bytes.fromhex(data)

final = b64encode(result)
print(final)
