import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(message)s')

class HangMan(object):

    def __init__(self, word):
        self.word = word
        self.STATES = ['', 'Head', 'Neck', 'Chest', 'Left Arm', 'Right Arm', 'Left Leg', 'Right Leg']
        self.currentState = 0
        self.wrongGuesses = []
        self.rightGuesses = []

    def guess(self, letter):
        if letter in self.word:
            self.rightGuesses.append(letter)
            return True
        else:
            self.wrongGuesses.append(letter)
            if self.currentState < len(self.STATES):
                self.currentState += 1
            return False

    def hung(self):
        return self.currentState == self.STATES[-1]

    def guessed(self):
        return self.currentState < len(self.STATES) and len(self.rightGuesses) == len(self.word)

    def gameStatus(self):
        logging.debug(self.getCurrentState())
        print 'Wrong guesses: %s' % self.wrongGuesses
        print 'Correct guesses: %s' % self.rightGuesses
        if self.hung():
            return 'hung'
        elif self.guessed():
            return 'guessed'
        else:
            return 'guessmore'

    def getCurrentState(self):
        return self.STATES[self.currentState]

if __name__ == '__main__':
    logging.debug('starting')
    i = None
    hangman = HangMan('game')
    while i != 'q':
        print "%s" % hangman.getCurrentState()
        i = raw_input('Guess a letter, or type q to quit: ')
        guessed = hangman.guess(i)
        if guessed:
            print "That's right!"
        else:
            print "WRONG..."
        gameStatus = hangman.gameStatus()
        done = (gameStatus == 'hung') or (gameStatus == 'guessed')
        if gameStatus == 'hung':
            print "\n=== GAME OVER ===\n"
        elif gameStatus == 'guessed':
            print "You guessed it!"
        else:
            print "Keep guessing..."
        if done:
            i = raw_input("Play again? (y/n): ")
            if i == 'y':
                hangman = HangMan('food')
            else:
                break
    print "Bye..."



