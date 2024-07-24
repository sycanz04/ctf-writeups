#! /usr/bin/python3

# For example:
# message: HELLO
# ascii bytes: [72, 69, 76, 76, 79]
# hex bytes: [0x48, 0x45, 0x4c, 0x4c, 0x4f]
# base-16: 0x48454c4c4f
# base-10: 310400273487 

from Crypto.Util.number import *

# Method 1
givenInt = 11515195063862318899931685488813747395775516287289682636499965282714637259206269
bytes = long_to_bytes(givenInt).decode()
print(f"Flag: {bytes}")
