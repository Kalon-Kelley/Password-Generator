from colorama import init
init()
print("""\033[92m
    ╔═╗╔══╗╔══╗╔══╗╔╦═╦╗╔═╗╔══╗╔══╗     ╔══╗╔══╗╔═╦╗╔══╗╔══╗╔══╗╔══╗╔══╗╔═╗╔══╗            ╔══╗ ╔═══╗
    ║□║║╔╗║║══╣║══╣║║║║║║║║║□ ║╚╗╗║     ║╔═╣║║═╣║║║║║║═╣║□ ║║□ ║║╔╗║╚╗╔╝║║║║□ ║     ╔═╦═╗  ╚╗ ║ ║ ║ ║
    ║╔╝║╠╣║╠══║╠══║║║║║║║║║║╗ ╣╔╩╝║     ║╚╗║║║═╣║║║║║║═╣║╗ ╣║╗ ╣║╠╣║ ║║ ║║║║╗ ╣     ╚╗║╔╝   ║ ║ ║ ║ ║
    ╚╝ ╚╝╚╝╚══╝╚══╝╚═╩═╝╚═╝╚╩═╝╚══╝     ╚══╝╚══╝╚╩═╝╚══╝╚╩═╝╚╩═╝╚╝╚╝ ╚╝ ╚═╝╚╩═╝      ╚═╝    ╚═╝■╚═══╝\033[00m
""")

from random import *
from os.path import join

passFile = input("What file do you want to store your passwords in?\n")+".txt"
path = input("What is the path for your file [Enter] for default\n") # "C:\\Users\\optim\\Desktop"

if path == "":
    path = "C:\\Users\\optim\\Desktop"

outfile = open(join(path, passFile), 'a+')

PASS_LIST = []
numCHARACTERS = []

CHAR = 0
try:
    CHAR = int(input("""How many characters long would you like the password to be,
not including specified words or characters?\n"""))

except ValueError:
    print("Error, not a valid number")
    quit()

SPEC_CHAR = input("Would you like special characters in the password? \n[Y] for yes \n[N] for no\n").upper()

if SPEC_CHAR != "Y" and SPEC_CHAR != "N":
    print("Unacceptable Value")
    quit()

NUM_CHAR = input("Would you like numbers in the password? \n[Y] for yes \n[N] for no\n").upper()

if NUM_CHAR != "Y" and NUM_CHAR != "N":
    print("Unacceptable Value")
    quit()

SPACES = input("Would you like to include spaces in the password? \n[Y] for yes \n[N] for no\n").upper()

if SPACES != "Y" and SPACES != "N":
    print("Unacceptable Value")
    quit()

SPEC_CHAR_WORD = input("""Would you like any specified characters and/or words to be included in the password
[Y] for yes
[N] for no
""").upper()

specificCharactersList = []

LEN_SPEC_CHAR = 0

if SPEC_CHAR_WORD == "Y":
    CHARACTER = str(input("What specific characters or words would you like to include use [,] as separation \n"))
    if "," in CHARACTER:
        specificCharactersList = CHARACTER.split(',')
        LEN_SPEC_CHAR = len(CHARACTER) - (len(specificCharactersList)-1)
    else:
        specificCharactersList.append(CHARACTER)
        LEN_SPEC_CHAR = len(CHARACTER)

NUM_SPEC = len(specificCharactersList)

remChar = CHAR - LEN_SPEC_CHAR

if remChar < 0:
    print("Specified characters or words are longer than password length")
    quit()

for i in range(remChar + 1):
    RND = randint(0, 3)
    if RND == 0:
        if SPEC_CHAR == "Y":
            SPEC_RND = 0
            if SPACES == "Y":
                SPEC_RND = randint(32, 47)
            else:
                SPEC_RND = randint(33, 47)
            PASS_LIST.append(str(chr(SPEC_RND)))
        else:
            CAPS_RND = randint(0, 1)
            if CAPS_RND == 0:
                ALPHA_RND = randint(97, 122)
                PASS_LIST.append(str(chr(ALPHA_RND)))
            else:
                ALPHA_RND = randint(65, 90)
                PASS_LIST.append(str(chr(ALPHA_RND)))
    elif RND == 1:
        if NUM_CHAR == "Y":
            NUM_RND = randint(0, 9)
            PASS_LIST.append(str(NUM_RND))
        else:
            CAPS_RND = randint(0, 1)
            if CAPS_RND == 0:
                ALPHA_RND = randint(97, 122)
                PASS_LIST.append(str(chr(ALPHA_RND)))
            else:
                ALPHA_RND = randint(65, 90)
                PASS_LIST.append(str(chr(ALPHA_RND)))
    elif RND == 2:
        if SPEC_CHAR_WORD == "Y":
            if NUM_SPEC > 1:
                RND_CHAR = randint(0, NUM_SPEC-1)
                PASS_LIST.append(str(specificCharactersList[RND_CHAR]))
                specificCharactersList.pop(RND_CHAR)
                NUM_SPEC = len(specificCharactersList)
            elif NUM_SPEC == 1:
                PASS_LIST.append(str(specificCharactersList[0]))
                specificCharactersList.pop(0)
                NUM_SPEC = len(specificCharactersList)
            else:
                CAPS_RND = randint(0, 1)
                if CAPS_RND == 0:
                    ALPHA_RND = randint(97, 122)
                    PASS_LIST.append(str(chr(ALPHA_RND)))
                else:
                    ALPHA_RND = randint(65, 90)
                    PASS_LIST.append(str(chr(ALPHA_RND)))
        else:
            ALPHA_RND = randint(65, 90)
            PASS_LIST.append(str(chr(ALPHA_RND)))
    else:
        CAPS_RND = randint(0, 1)
        if CAPS_RND == 0:
            ALPHA_RND = randint(97, 122)
            PASS_LIST.append(str(chr(ALPHA_RND)))
        else:
            ALPHA_RND = randint(65, 90)
            PASS_LIST.append(str(chr(ALPHA_RND)))

for i in range(NUM_SPEC):
    if NUM_SPEC > 1:
        RND_CHAR = randint(0, NUM_SPEC-1)
        PASS_LIST.append(str(specificCharactersList[RND_CHAR]))
        specificCharactersList.pop(RND_CHAR)
        NUM_SPEC = len(specificCharactersList)
        for n in range(len(PASS_LIST)):
            tempChr = str(PASS_LIST[n])
            if len(tempChr) == 1:
                if tempChr not in specificCharactersList:
                    numCHARACTERS.append(tempChr)
        RAND = randint(0, len(numCHARACTERS) - 1)
        PASS_LIST.remove(numCHARACTERS[RAND])
    elif NUM_SPEC == 1:
        PASS_LIST.append(str(specificCharactersList[0]))
        specificCharactersList.pop(0)
        NUM_SPEC = len(specificCharactersList)
        for n in range(len(PASS_LIST)):
            tempChr = str(PASS_LIST[n])
            if len(tempChr) == 1:
                if tempChr not in specificCharactersList:
                    numCHARACTERS.append(tempChr)
        RAND = randint(0, len(numCHARACTERS) - 1)
        PASS_LIST.remove(numCHARACTERS[RAND])

print(*PASS_LIST, sep="")

passTitle = input("What is this password for?")

strPass = ""
for i in PASS_LIST:
    strPass += i

outfile.write("%s : %s\n" % (passTitle, strPass))
outfile.close()

close = input("Press any key to close")
