#!/usr/bin/env python3
from pwn import cyclic

# Generate a 300-byte cyclic pattern for a 64-bit environment (n=8)
pattern = cyclic(300, n=8)
with open("badfile", "wb") as f:
    f.write(pattern)
print("Cyclic pattern written to badfile")
