# XOR Starter

## Problem
Given the string `label`, XOR each character with the integer `13`. Convert these integers back to a string and submit the flag as `crypto{new_string}`.

## Solution
So first we'll have to separate the string `label` into a list of char.
```
charVar = [*givenString]
```
Then you can do a for loop to get the integer representation of each char and XOR it with 13
```
ordChar = ord(char)^13
```
Finally just convert the integers back into unicode characters
```
print(chr(ordChar))
```
