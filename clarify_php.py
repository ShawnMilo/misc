#!/usr/bin/env python

"""
Attempt to un-obfuscate PHP malware. Such malware will often have a
gibberish string which is used as an "alphabet," by referring to indexes
of it throughout the remainder of the code. If you identify this, replace
the gibberish variable name with "$alphabet" before running this for best
results.
"""

import sys
import re

def get_alphabet(mess):
    for line in mess.split('\n'):
        if '$alphabet = ' in line:
            return line.split()[-1][1:]
    return None

chr_pat = re.compile(r'chr\((\d+)\)')
hex_pat = re.compile(r'\\x([a-f0-9]{2})', re.IGNORECASE)
alpha_pat = re.compile(r'\$alphabet\[(\d+)\]')

with open(sys.argv[1], 'r') as raw:
    mess = raw.read()

alphabet = get_alphabet(mess)

while True:
    char_match = chr_pat.search(mess)
    if char_match is None:
        break
    start, end =  char_match.start(), char_match.end()
    code = int(char_match.groups()[0])
    mess = mess[:start] + chr(code) + mess[end:]

while True:
    hex_match = hex_pat.search(mess)
    if hex_match is None:
        break
    start, end =  hex_match.start(), hex_match.end()
    code = int(hex_match.groups()[0], 16)
    mess = mess[:start] + chr(code) + mess[end:]

while True:
    alpha_match = alpha_pat.search(mess)
    if alpha_match is None:
        break
    start, end =  alpha_match.start(), alpha_match.end()
    code = int(alpha_match.groups()[0])
    mess = mess[:start] + alphabet[code] + mess[end:]

print mess
