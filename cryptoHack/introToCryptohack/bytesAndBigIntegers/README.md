# Bytes and Big Integers

## Question
Cryptosystems like RSA works on numbers, but messages are made up of characters. How should we convert our messages into numbers so that mathematical operations can be applied?
<br/><br/>
The most common way is to take the ordinal bytes of the message, convert them into hexadecimal, and concatenate. This can be interpreted as a base-16/hexadecimal number, and also represented in base-10/decimal.
<br/><br/>
To illustrate:
```
message: HELLO
ascii bytes: [72, 69, 76, 76, 79]
hex bytes: [0x48, 0x45, 0x4c, 0x4c, 0x4f]
base-16: 0x48454c4c4f
base-10: 310400273487 
```

Given the below integer:
```
11515195063862318899931685488813747395775516287289682636499965282714637259206269
```

## Solution
To do that. We can use a function from PyCryptodome module to help convert the long int type into bytes, then finally decoding them to retrieve the flag.
```python
from Crypto.Util.number import *

# Method 1
givenInt = 11515195063862318899931685488813747395775516287289682636499965282714637259206269
bytes = long_to_bytes(givenInt).decode()
print(f"Flag: {bytes}")
```
