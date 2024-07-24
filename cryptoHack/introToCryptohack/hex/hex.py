#! /usr/bin/python3

sampleBytes = bytes.fromhex("63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d")
print(sampleBytes.decode('utf-8')) # Outputs the flag

test = bytes.fromhex("63")
print(test.decode('utf-8')) # Outputs the first character of the flag
