# ASCII
Modern cryptography involves code, and code involves coding. CryptoHack provides a good opportunity to sharpen your skills.
Of all modern programming languages, Python 3 stands out as ideal for quickly writing cryptographic scripts and attacks. For more information about why we think Python is so great for this, please see the FAQ.
Run the attached Python script and it will output your flag.

## chr
chr() in python returns the unicode character from a integer representation of it. So in this problem we were given a list of int
```
[81, 64, 75, 66, 70, 93, 73, 72, 1, 92, 109, 2, 84, 109, 66, 75, 70, 90, 2, 92, 79]
```
So all we have to do is just create a loop that performs chr() on all integer given and return them as a string
```python
ordList = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]
chrList = []

for list in ordList:
    chrList.append(chr(list))

print("".join(chrList))
```
