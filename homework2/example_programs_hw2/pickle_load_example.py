"""
    File:  pickle_load_example.py
    Description:  Simple program to demonstrate how to:
    * restore/read several Python objects from a file using the pickle module method pickle.load
    * two dictionaries are restored/read:
        - charToMorseCodeDict with a character key with a value corresponding to its Morse code string
        - morseCodeToCharDict with a Morse-code string key with a value corresponding to the character
"""
import pickle

END_OF_MESSAGE_CODE = '.-.-.'

myFile = open("morseCodeObjects.p","rb")
charToMorseCodeDict = pickle.load(myFile)
morseCodeToCharDict = pickle.load(myFile)

print("charToMorseCodeDict: ")
print (charToMorseCodeDict)

print("\nmorseCodeToCharDict: ")
print (morseCodeToCharDict)
