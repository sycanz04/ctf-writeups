#! /usr/bin/python3

givenString = "label"
givenINt = 13

charVar = [*givenString]

for char in charVar:
    ordChar = ord(char)^13
    print(chr(ordChar))
# ordString = ord(givenString)
# print(ordString)
