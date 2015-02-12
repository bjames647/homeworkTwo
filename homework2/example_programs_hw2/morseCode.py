from os.path import exists
import os
import pickle

def getMorseCode():
	END_OF_MESSAGE_CODE = '.-.-.'

	myFile = open("morseCodeObjects.p","rb")
	charToMorseCodeDict = pickle.load(myFile)
	morseCodeToCharDict = pickle.load(myFile)
	myFile.close()

	print("charToMorseCodeDict: ")
	print (charToMorseCodeDict)

	print("\nmorseCodeToCharDict: ")
	print (morseCodeToCharDict)

def fileExist(fileName):
    directoryList = os.listdir('.')    
    if fileName == '':
        return False
    elif exists(fileName):
        return True
    else:
        return False

def createMorseCodeFile(fileName):
	directoryList = os.listdir('.') 
	newFile = fileName[0:-3]
	newFile = newFile + "zzz"
	if exists(newFile):
		print("WARNING: The file '" + newFile + "' already exists!")
		remakeFile = input("Is it okay to wipe it out (y/n)? ")
		while remakeFile != 'y' and remakeFile != 'n':
			userInput = input("Please enter a correct choice. Is it okay to wipe it out (y/n)? ")
		if remakeFile == 'y':
			openedFile = open(newFile, "w")
		else:
			print("Please pick a different file ending in .zzz ('textfile.zzz') to recieve the encoded or decoded text.")
			newFile = input("Selection: ")
			openedFile = open(newFile, "w")
	else:
		openedFile = openedFile = open(newFile, "w")
	return openedFile

def readFile(fileName):
	if not exists(fileName):
		print("File", fileName, "does NOT exist!")
	else:
        # Open the file for reading 'r'
		myFile = open(fileName, 'r')
		lineNumber = 1
		# loop over the file a line at a time
		for line in myFile:
			line = line.rstrip() # remove new-line character from line
			print('Words on line %d: "%s"' % (lineNumber, line)) 
		    # split line by default of white-space
			wordList = line.split()

		    # loop over list of word and print each word
			for word in wordList:
				print(word)
			lineNumber += 1

def 

def main():
	print("Welcome to the Morse-code Encryption/Decryption Program")

	userInput = input("Would you like (e)ncrypt a file, (d)ecrypt a file, or e(x)it (enter e, d, or x)? ")
	while userInput != 'e' and userInput != 'd' and userInput != 'x':
		userInput = input("Please enter a correct choice. Would you like (e)ncrypt a file, (d)ecrypt a file, or e(x)it (enter e, d, or x)? ")

	if userInput == 'e':
		fileName = input("Enter the text-file name to encrypt: ")
		while fileExist(fileName) == False:
			print("Sorry the file '" + fileName + "' does NOT exist--please try again!")
			fileName = input("Enter the text-file name to encrypt: ")
	elif userInput == 'd':
		fileName = input("Enter the text-file name to decrypt: ")
		while fileExist(fileName) == False:
			if fileExists == True:
				readFile(fileName)
			else:
				print("Sorry the file '" + fileName + "' does NOT exist--please try again!")
	else:
		return

	openedFile = createMorseCodeFile(fileName)
	







	#openedFile.write("FJDLJFKL")
	print("MAde it!")
main()