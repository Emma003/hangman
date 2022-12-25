import random

class Game:
    words = []

    def __init__(self, wordList, letters):

        self.livesLeft = 6
        self.wordString = ""

        #randomly pick a word from the list and add each of its letters to a set for fast lookup
        self.generateWord(wordList)
        self.letterSet = set(self.wordString)

        #add 1-3 start letters at the beginning depending on the size of the word
        self.wordArray = ['_' for i in range(len(self.wordString))]
        self.getStartFormat()

        #remove letters from start letter list if they were included in the start format
        self.setLetterList(letters)

        #keep track of number of blank letters (user won when == 0)
        self.emptyCellCount = 0
        self.setEmptyCellCount()

    def generateWord(self, wordList):
        randomIndex = random.randint(1, 981)
        self.wordString = wordList[randomIndex]
        self.wordString = self.wordString[:-1]

    def getStartFormat(self):
        numOfReveals = 0
        wordLen = len(self.wordString)

        if wordLen <= 7:
            numOfReveals = 1
        elif wordLen <= 10:
            numOfReveals = 2
        else:
            numOfReveals = 3

        while numOfReveals > 0:
            randomIndex = random.randint(1, wordLen - 1)
            self.wordArray[randomIndex] = self.wordString[randomIndex]
            numOfReveals -= 1

    def setLetterList(self, letters):
        for c in self.wordArray:
            if c != '_':
                charCount = 0

                for char in self.wordString:
                    if c == char:
                        charCount += 1

                if charCount == 1:
                    del letters[c]


    def setEmptyCellCount(self):
        for char in self.wordArray:
            if char == '_':
                self.emptyCellCount += 1


    def word_size(self):
        return len(self.wordString)


    def play(self, char):

        if char not in self.letterSet:
            print("CHARACTER NOT IN WORD")
            self.livesLeft -= 1
            print("YOU HAVE " + str(self.livesLeft) + " LIVES LEFT!!!")
            return False

        else:
            print("CHARACTER FOUND IN WORD")
            print("")
            for i, chr in enumerate(self.wordString):
                if chr == char:
                    self.wordArray[i] = char

            empty_cells = 0
            for c in self.wordArray:
                if c == '_':
                    empty_cells += 1
            self.emptyCellCount = empty_cells

            return True
