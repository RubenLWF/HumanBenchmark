import os
from aimTrainer import aimTrainer
from chimpTest import chimpTest
from numberMemory import numberMemory
from reactionTime import reactionTime
from sequenceMemory import sequenceMemory
from typingTest import typingTest
from verbalMemory import verbalMemory
from visualMemory import visualMemory

tests = {1 : ". Aim Trainer", 2 : ". Chimp test", 3: ". Number Memory", 4 : ". Reaction Time", 5 : ". Sequence Memory", 6 : ". Typing Test", 7 : ". Verbal Memory", 8 : ". Visual Memory"}

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def prompt():
    cls()
    for test in tests:
        print(str(test) + tests[test])
    return int(input('Insert number of wanted test (Or "9" to stop): '))

def run(test):
    match test:
        case 1: aimTrainer()
        case 2: chimpTest()
        case 3: numberMemory()
        case 4: reactionTime()
        case 5: sequenceMemory()
        case 6: typingTest()
        case 7: verbalMemory()
        case 8: visualMemory()
        case 9: exit()

    start()

def start():
    test = prompt()
    run(test)

start()