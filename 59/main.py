#!/usr/bin/env python3

import sys
from aux import *

# CHARS = range(97, 123, 1)

def increment_cipher(ciph, slot):
    ciph[slot] += 1
    if ciph[slot] > 122:
        if slot == 2:
            print("last cipher reached. exiting")
            return ""
        ciph[slot] = 97
        return increment_cipher(ciph, slot + 1)
    return ciph

def decrypt(ciph, text):
    text = text[:]
    l = len(text)
    cur = 0 
    for i in range(l):
        # decypher one char

        text[i] = chr(text[i] ^ ciph[cur])

        cur += 1
        cur %= 3
    return "".join(text)

with open("p059_cipher.txt", "r") as f:
    chr_array = [int(l) for l in f.readlines()[0].split(",")]


# only decrypt with known cipher, then exit
d_text = decrypt([101, 120, 112], chr_array)
sum = 0
for c in d_text:
    sum += ord(c)
print(sum)
sys.exit(0)

current_cipher = [97, 97, 97]
hits = 0

while True:
    # do sth with cipher
    d_text = decrypt(current_cipher, chr_array).lower()

    # check if keywords are in decrypted text
    if d_text.find("that") != -1:
        hits += 1
        print(d_text)
        print(current_cipher)

    # increment cipher
    current_cipher = increment_cipher(current_cipher, 0)
    if current_cipher == "":
        print(hits)
        sys.exit(0)

# working cipher:
# [101, 120, 112]