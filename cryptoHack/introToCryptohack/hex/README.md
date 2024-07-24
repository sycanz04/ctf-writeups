# Hex
When we encrypt something the resulting ciphertext commonly has bytes which are not printable ASCII characters. If we want to share our encrypted data, it's common to encode it into something more user-friendly and portable across different systems.
<br/><br/>
Hexadecimal can be used in such a way to represent ASCII strings. First each letter is converted to an ordinal number according to the ASCII table (as in the previous challenge). Then the decimal numbers are converted to base-16 numbers, otherwise known as hexadecimal. The numbers can be combined together, into one long hex string.
<br/><br/>
So we're given a flag encoded as hex string
```
63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d
```

## Hex
Hex numbers are base-16 (0-9, a-f) are 4 bits each so we can use `bytes.fromhex()` to convert each pair of hex digits into the corresponding bytes since 8 bits makes a byte. Then after that we will decode the returned byte and retrieve our flag.
```python
test = bytes.fromhex("63")
print(test.decode('utf-8')) # Outputs 'c' as hex 63 = c in ASCII table
```
