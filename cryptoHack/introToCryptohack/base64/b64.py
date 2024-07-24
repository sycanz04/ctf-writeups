#! /usr/bin/python3

import base64

hexString = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"
hexToByte = bytes.fromhex(hexString)
print(f"Hex bytes: {hexToByte}")

encodedBase64 = base64.b64encode(hexToByte).decode()
print(f"Flag: {encodedBase64}")
