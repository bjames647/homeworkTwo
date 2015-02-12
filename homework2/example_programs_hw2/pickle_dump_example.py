"""
    File:  pickle_dump_example.py
    Description:  Simple program to demonstrate how to:
    * save several Python objects to a file using the pickle module method pickle.dump
    * two dictionaries are saved:
        - charToMorseCodeDict with a character key with a value corresponding to its Morse code string
        - morseCodeToCharDict with a Morse-code string key with a value corresponding to the character
"""

import pickle

# charToMorseCodeDict - dictionary with a character key with a value corresponding to its Morse code string
charToMorseCodeDict = {
    '.':'.-.-.-',
    ',':'--..--',
    '?':'..--..',
    ':':'--..--',
    '@':'.--.-.',
    '/':'-..-.',
    '-':'-....-',
    '\'':'.-----.',
    '"':'.-..-.',
    '=':'-...-',
    '(':'-.--.-',
    ')':'-.--.-',
    '\n':'.-.-',
    '0':'-----',
    '1':'.----',
    '2':'..---',
    '3':'...--',
    '4':'....-',
    '5':'.....',
    '6':'-....',
    '7':'--...',
    '8':'---..',
    '9':'----.',
    'A':'.-',
    'B':'-...',
    'C':'-.-.',
    'D':'-..',
    'E':'.',
    'F':'..-.',
    'G':'--.',
    'H':'....',
    'I':'..',
    'J':'.---',
    'K':'-.-',
    'L':'.-..',
    'M':'--',
    'N':'-.',
    'O':'---',
    'P':'.--.',
    'Q':'--.-',
    'R':'.-.',
    'S':'...',
    'T':'-',
    'U':'..-',
    'V':'...-',
    'W':'.--',
    'X':'-..-',
    'Y':'-.--',
    'Z':'--..' }

# morseCodeToCharDict - dictionary with a Morse-code string key with a value corresponding to the character
morseCodeToCharDict = {}
for char in charToMorseCodeDict:
    morseCodeToCharDict[charToMorseCodeDict[char]] =  char

myFile = open("morseCodeObjects.p","wb")
pickle.dump(charToMorseCodeDict, myFile,2)
pickle.dump(morseCodeToCharDict, myFile,2)

myFile.close()
