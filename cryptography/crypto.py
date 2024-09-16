#!/usr/bin/env python3

"""
Cryptography Project
"""

import sys

# provided ALPHABET constant - list of the regular alphabet
# in lowercase. Refer to this simply as ALPHABET in your code.
# This list should not be modified.
ALPHABET = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def compute_slug(key):
    """
    Given a key string, compute and return the len-26 slug list for it.
    >>> compute_slug('z')
    ['z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y']
    >>> compute_slug('Bananas!')
    ['b', 'a', 'n', 's', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'o', 'p', 'q', 'r', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    >>> compute_slug('Life, Liberty, and')
    ['l', 'i', 'f', 'e', 'b', 'r', 't', 'y', 'a', 'n', 'd', 'c', 'g', 'h', 'j', 'k', 'm', 'o', 'p', 'q', 's', 'u', 'v', 'w', 'x', 'z']
    >>> compute_slug('Zounds!')
    ['z', 'o', 'u', 'n', 'd', 's', 'a', 'b', 'c', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'p', 'q', 'r', 't', 'v', 'w', 'x', 'y']
    """
    unique_chars = []
    for i in key:
        if i not in unique_chars:
            unique_chars.append(i)
    for char in ALPHABET:
        if char not in unique_chars:
            unique_chars.append(char)
    return unique_chars



def encrypt_char(source, slug, ch):
    """
    Given source and slug lists,
    if the char ch is in source, return
    its encrypted form. Otherwise return ch unchanged.
    >>> encrypt_char(['a', 'b', 'c', 'd'], ['d', 'c', 'b', 'a'], 'a')
    'd'
    >>> encrypt_char(['a', 'b', 'c', 'd'], ['d', 'c', 'b', 'a'], 'c')
    'b'
    >>> encrypt_char(['a', 'b', 'c', 'd'], ['d', 'c', 'b', 'a'], 'C')
    'B'
    >>> encrypt_char(['a', 'b', 'c', 'd'], ['d', 'c', 'b', 'a'], ',')
    ','
    >>> # Compute 'z' slug, store it in a var named z_slug
    >>> # and pass that in as the slug for the tests.
    >>> z_slug = compute_slug('z')
    >>> encrypt_char(ALPHABET, z_slug, 'A')
    'Z'
    >>> encrypt_char(ALPHABET, z_slug, 'n')
    'm'
    >>> encrypt_char(ALPHABET, z_slug, ' ')
    ' '
    """
    if isinstance(ch , str):
        chars = [c.strip() for c in ch.split(',')]
    else:
        chars = list(ch)
    encrypted_chars = []
    for c in chars:
        lower_c = c.lower()
        if lower_c in source:
            index = source.index(lower_c)
            encrypted_char = slug[index]
            if c.isupper():
                encrypted_chars.append(encrypted_char.upper())
            else:
                encrypted_chars.append(encrypted_char)
        else:
            encrypted_chars.append(c)
    return  ',' .join(encrypted_chars)

def encrypt_str(source, slug, s):
    """
    Given source and slug lists and string s,
    return a version of s where every char
    has been encrypted by source/slug.
    >>> z_slug = compute_slug('z')
    >>> encrypt_str(ALPHABET, z_slug, 'And like a thunderbolt he falls.')
    'Zmc khjd z sgtmcdqanks gd ezkkr.'
    """
    encrypted_chars = []
    for c in s:
        lower_c = c.lower()
        if lower_c in source:
            index = source.index(lower_c)
            encrypted_char = slug[index]
            if c.isupper():
                encrypted_chars.append(encrypted_char.upper())
            else:
                encrypted_chars.append(encrypted_char)
        else:
            encrypted_chars.append(c)
    return ''.join(encrypted_chars)

def decrypt_str(source, slug, s):
    """
    Given source and slug lists and encrypted string s,
    return the decrypted form of s.
    >>> z_slug = compute_slug('z')
    >>> decrypt_str(ALPHABET, z_slug, 'Zmc khjd z sgtmcdqanks gd ezkkr.')
    'And like a thunderbolt he falls.'
    """
    return encrypt_str(slug , source , s)


def encrypt_file(filename, key):
    """
    Given filename and key, compute and
    print the encrypted form of its lines.
    >>> encrypt_file('test-plain.txt', 'z')
    zab
    wxy
    """
    slug = compute_slug(key)
    source = ALPHABET
    with open(filename , 'r') as f:
        for line in f:
            line = line.strip()
            encrypted_line = encrypt_str(source , slug , line)
            print(encrypted_line)


def decrypt_file(filename, key):
    """
    Given filename and key, compute and
    print the decrypted form of its lines.
    >>> decrypt_file('test-crypt.txt', 'z')
    abc
    xyz
    """
    slug = compute_slug(key)
    source = ALPHABET
    with open (filename , 'r') as f:
        for line in f:
            line = line.strip()
            decrypted_line = decrypt_str(source , slug , line)
            print(decrypted_line)


def main():
    args = sys.argv[1:]
    # 2 command line argument patterns:
    # -encrypt key filename
    # -decrypt key filename
    # Call encrypt_file() or decrypt_file() based on the args.
    mode = args[0]
    key = args[1]
    filename = args[2]
    if mode == '-encrypt':
        encrypt_file(filename , key)
    elif mode == '-decrypt':
        decrypt_file(filename , key)
    else:
        print("Invalid mode! Use -encrypt or -decrypt.")


# Python boilerplate.
if __name__ == '__main__':
    main()
