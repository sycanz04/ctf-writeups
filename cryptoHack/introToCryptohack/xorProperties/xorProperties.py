#! /usr/bin/python3

from binascii import unhexlify

def xorTwoStr(first, second):
    if len(first) != len(second):
        raise Exception("The number of bits don't match, can't XOR them!")

    return "".join(format(int(a, 16) ^ int(b, 16), 'x') for a, b in zip(first, second))


key1 = "a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313"
key21 = "37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e"
key23 = "c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1"
flagKey132= "04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf"

# XOR operations
key2 = xorTwoStr(key1, key21)
print(f"Key 2: {key2}")

key3 = xorTwoStr(key2, key23)
print(f"Key 3: {key3}")

key4 = xorTwoStr(key1, xorTwoStr(key2, key3))

flag = xorTwoStr(flagKey132, key4)
print(f"Flag hex: {flag}")

realFlag = unhexlify(flag)
print(f"Flag: {realFlag.decode()}")
