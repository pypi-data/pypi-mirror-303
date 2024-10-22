#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on 23.2.2012

@author: David
'''


def bytes2bin(rawBytes, sz=8):
    """Accepts a string of bytes (chars) and returns an array of bits representing
    the bytes in big endian byte (Most significant byte/bit first) order.  Each byte
    can have it's higher bits ignored by passing a sz."""
    if sz < 1 or sz > 8:
        raise ValueError("Invalid sz value: " + str(sz))
    retVal = []
    for b in rawBytes:
        bits = []
        b = ord(b)
        while b > 0:
            bits.append(b & 1)
            b >>= 1

        if len(bits) < sz:
            bits.extend([0] * (sz - len(bits)))
        elif len(bits) > sz:
            bits = bits[:sz]

        bits.reverse()  # Big endian byte order.
        retVal.extend(bits)

    if len(retVal) == 0:
        retVal = [0]
    return retVal


def bin2bytes(x):
    """Convert an array of bits (MSB first) into a string of characters."""
    bits = []
    bits.extend(x)
    bits.reverse()

    i = 0
    out = ''
    multi = 1
    ttl = 0
    for b in bits:
        i += 1
        ttl += b * multi
        multi *= 2
        if i == 8:
            i = 0
            out += chr(ttl)
            multi = 1
            ttl = 0

    if multi > 1:
        out += chr(ttl)

    out = list(out)
    out.reverse()
    out = ''.join(out)
    return out


def bin2dec(x):
    """Convert an array of "bits" (MSB first) to it's decimal value."""
    bits = []
    bits.extend(x)
    bits.reverse()

    multi = 1
    value = 0
    for b in bits:
        value += b * multi
        multi *= 2
    return value


def bytes2dec(rawBytes, sz=8):
    return bin2dec(bytes2bin(rawBytes, sz))


def dec2bin(n, p=0):
    """Convert a decimal value to an array of bits (MSB first), optionally padding
    the overall size to p bits. """
    assert (n >= 0)
    retVal = []

    while n > 0:
        retVal.append(n & 1)
        n >>= 1

    if p > 0:
        retVal.extend([0] * (p - len(retVal)))
        retVal.reverse()

    return retVal


def dec2bytes(n, p=0):
    return bin2bytes(dec2bin(n, p))


def bin2synchsafe(x):
    """Convert a list of bits (MSB first) to a synch safe list of bits."""

    if len(x) > 32 or bin2dec(x) > 268435456:  # 2^28
        raise ValueError("Invalid value")
    elif len(x) < 8:
        return x

    n = bin2dec(x)
    bites = ""
    bites += chr((n >> 21) & 0x7f)
    bites += chr((n >> 14) & 0x7f)
    bites += chr((n >> 7) & 0x7f)
    bites += chr((n >> 0) & 0x7f)
    bits = bytes2bin(bites)
    if len(bits) < 32:
        bits = ([0] * (32 - len(x))) + bits

    return bits


def bytes2str(rawBytes):
    s = ""
    for b in rawBytes:
        s += ("\\x%02x" % ord(b))
    return s
