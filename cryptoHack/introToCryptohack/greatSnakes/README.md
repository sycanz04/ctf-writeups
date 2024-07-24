# Great Snakes
Modern cryptography involves code, and code involves coding. CryptoHack provides a good opportunity to sharpen your skills.
Of all modern programming languages, Python 3 stands out as ideal for quickly writing cryptographic scripts and attacks. For more information about why we think Python is so great for this, please see the FAQ.
Run the attached Python script and it will output your flag.

## Ord
Ord() in python returns the integer representation of a unicode character. So in this problem we were given a list of ord
```
ords = [81, 64, 75, 66, 70, 93, 73, 72, 1, 92, 109, 2, 84, 109, 66, 75, 70, 90, 2, 92, 79]
```
Then it XORs the ords list with 0x32 before printing out the flag
```
crypto{z3n_0f_pyth0n}
```
