# Base64
## Question
Another common encoding scheme is Base64, which allows us to represent binary data as an ASCII string using an alphabet of 64 characters. One character of a Base64 string encodes 6 binary digits (bits), and so 4 characters of Base64 encode three 8-bit bytes.
<br/><br/>
Base64 is most commonly used online, so binary data such as images can be easily included into HTML or CSS files.
<br/><br/>
So we're given a hex string:
```
72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf
```

### Solution
Just like in [Hex](https://github.com/sycanz04/ctf-writeups/tree/main/cryptoHack/introToCryptohack/hex), we will have convert the hex into bytes, then encode it into base64 with base64.b64encode()
```python
hexString = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"
hexToByte = bytes.fromhex(hexString)
print(f"Hex bytes: {hexToByte}")

encodedBase64 = base64.b64encode(hexToByte).decode()
print(f"Flag: {encodedBase64}")

```
