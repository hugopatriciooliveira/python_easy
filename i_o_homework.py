#### Homework Assignment #8: Input and Output (I/O)
"""
Details:
Create a note-taking program. When a user starts it up, it should prompt them for a filename.
If they enter a file name that doesn't exist, it should prompt them to enter the text they want 
to write to the file. After they enter the text, it should save the file and exit.
If they enter a file name that already exists, it should ask the user if they want:
A) Read the file
B) Delete the file and start over
C) Append the file
If the user wants to read the file it should simply show the contents of the file on the screen. 
If the user wants to start over then the file should be deleted and another empty one made in its 
place. If a user elects to append the file, then they should be able to enter more text, and that 
text should be added to the existing text in the file. 
"""
import os.path

for i in range(1):
    currentFileName = str(input("Please enter the file name:\n"))
    print(currentFileName)
    if os.path.isfile(currentFileName+".txt") == False:
        outputFile = open(currentFileName+".txt", "w")
        inputText = str(input("Type the text to write to the file:\n"))
        outputFile.write(inputText)
        print(inputText)
        outputFile.close()
    else:
        inputTextExists = str(input("This file already exists. Type 'r' to read the file, 'a' to append to the file or 'd' to delete the file and start over:\n"))
        if inputTextExists == "d":
            os.remove(currentFileName+".txt")
            open(currentFileName+".txt", "w+")
        if inputTextExists == "r":
            outputFileRead = open(currentFileName+".txt", "r")
            content = outputFileRead.read()
            print(content)
        if inputTextExists == "a":
            outputFileAppend = open(currentFileName+".txt", "a+")
            inputTextAppend = str(input("Please append the text to the file:\n"))
            outputFileAppend.write("\n"+inputTextAppend)
            outputFileAppend.close()
 
"""
Extra Credit:
Allow the user to select a 4th option:
D) Replace a single line
If the user wants to replace a single line in the file, they will then need to be 
prompted for 2 bits of information:
1) The line number they want to update.
2) The text that should replace that line.
"""
import os.path

for i in range(1):
    currentFileName = str(input("Please enter the file name:\n"))
    print(currentFileName)
    if os.path.isfile(currentFileName+".txt") == False:
        outputFile = open(currentFileName+".txt", "w")
        inputText = str(input("Type the text to write to the file:\n"))
        outputFile.write(inputText)
        print(inputText)
        outputFile.close()
    else:
        inputTextExists = str(input("This file already exists. Type 'r' to read the file, 'a' to append to the file, 'd' to delete the file and start over or 'p' to replace a single line:\n"))
        if inputTextExists == "d":
            os.remove(currentFileName+".txt")
            open(currentFileName+".txt", "w+")
        if inputTextExists == "r":
            outputFileRead = open(currentFileName+".txt", "r")
            content = outputFileRead.read()
            print(content)
        if inputTextExists == "a":
            outputFileAppend = open(currentFileName+".txt", "a+")
            inputTextAppend = str(input("Please append the text to the file:\n"))
            outputFileAppend.write(inputTextAppend+"\n")
            outputFileAppend.close()
        if inputTextExists == "p":
            inputLine = int(input("Wich line do you want to update?\n"))
            textUpdate = str(input("Type the text to update the file line:\n"))
            outputFileUpdate = open(currentFileName+".txt", "r")
            lines = outputFileUpdate.readlines()
            lines[inputLine] = textUpdate+"\n"
            outputFileUpdate = open(currentFileName+".txt", "w")
            outputFileUpdate.writelines(lines)[inputLine]
            outputFileUpdate.close
