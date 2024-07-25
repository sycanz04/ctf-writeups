# XOR Properties

## Question
In the last challenge, you saw how XOR worked at the level of bits. In this one, we're going to cover the properties of the XOR operation and then use them to undo a chain of operations that have encrypted a flag. Gaining an intuition for how this works will help greatly when you come to attacking real cryptosystems later, especially in the block ciphers category.
<br/><br/>
There are four main properties we should consider when we solve challenges using the XOR operator
```
Commutative: A ⊕ B = B ⊕ A
Associative: A ⊕ (B ⊕ C) = (A ⊕ B) ⊕ C
Identity: A ⊕ 0 = A
Self-Inverse: A ⊕ A = 0
```
Let's break this down. Commutative means that the order of the XOR operations is not important. Associative means that a chain of operations can be carried out without order (we do not need to worry about brackets). The identity is 0, so XOR with 0 "does nothing", and lastly something XOR'd with itself returns zero.
<br/><br/>
Let's put this into practice! Below is a series of outputs where three random keys have been XOR'd together and with the flag. Use the above properties to undo the encryption in the final line to obtain the flag.
```
KEY1 = a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313
KEY2 ^ KEY1 = 37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e
KEY2 ^ KEY3 = c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1
FLAG ^ KEY1 ^ KEY3 ^ KEY2 = 04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf
**Hint**: <em>Before you XOR these objects, be sure to decode from hex to bytes.</em>
```

## Solution
```python
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
```
<br/>
According to **Associative law** of XOR properties, `A ^ (B ^ C)` == `(A ^ B) ^ C`. So now if we do `KEY1 ^ (KEY2 ^ KEY1)` we will get `KEY2` because `KEY1 ^ KEY1 == 0` and `KEY2 ^ 0 = KEY2` according to the **Self-Inverse** and **Identity** properties. Then after getting `KEY2` we can do the same thing to `KEY2 ^ KEY3` which returns `KEY3`
<br/>
Now since we already have `KEY1, KEY2 AND KEY3`, we have to XOR `KEY1 ^ KEY2 ^ KEY3` with `FLAG ^ KEY1 ^ KEY3 ^ KEY2` to retrieve the flag's hex since any value XOR-ing itself will return 0 according to the **Self Inverse properties**
<br/>
Once we retrieve the flag's hex. We'll use unhexlify from binascii to convert the hexadecimal string representation to its corresponding bytes and decode it. Below are the output.

```
❯ ./xorProperties.py
Key 2: 911404e13f94884eabbec925851240a52fa381ddb79700dd6d0d
Key 3: 504053b757eafd3d709d6339b140e03d98b9fe62b84add0332cc
Flag hex: 63727970746f7b7830725f69355f61737330633161743176337d
Flag: crypto{x0r_i5_ass0c1at1v3}
```
