#!/usr/bin/env python3

from Crypto.Util.number import *

cipher = 11515195063862318899931685488813747395775516287289682636499965282714637259206269

uncipher = cipher.to_bytes(33, "big")
print(uncipher)