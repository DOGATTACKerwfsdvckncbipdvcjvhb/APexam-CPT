import random

name = input("Enter a character name: ")
age = input("Enter an age: ")
SuperGoodTraits = ["Speed II","Strength II", "Skill II", "Power II", "Sneak II", "Intelligence II"]
goodTraits = ["Speed I","Strength I", "Skill I", "Power I", "Sneak I", "Intelligence I", "Sharp sight"]
NeutralTraits = ["Kindness", "Loyalty", "Greed", "Honor", "Knitter", "Grace", "Generosity"]
badTraits = ["Blindness I", "Slowness I", "Cursed I", "Brittle I", "Dullness I", "Deafness I", "Heavy Bleeding"]
SuperBadTraits = ["Blindness II", "Slowness II", "Cursed II", "Dullness II", "Deafness II", "Hemorrhage"]
allTraits = ["Speed II","Strength II", "Skill II", "Power II", "Sneak II", "Intelligence II", "Speed I","Strength I", "Skill I", "Power I", "Sneak I", "Intelligence I", "Sharp sight", "Kindness", "Loyalty", "Greed", "Honor", "Knitter", "Grace", "Generosity", "Blindness I", "Slowness I", "Cursed I", "Brittle I", "Dullness I", "Deafness I", "Heavy Bleeding", "Blindness II", "Slowness II", "Cursed II", "Dullness II", "Deafness II", "Hemorrhage"]
BotNames = ["Eeeethan", "Luker", "Snoopers", "AAsush", "JaIden", "shooodow"]


def trait_chooser(traitNum):
    charTraits = []
    num = 0
    while num < traitNum:
        randomtrait = random.choice(allTraits)
        if randomtrait not in charTraits:
            charTraits.append(randomtrait)
            num+=1
        
    return charTraits
playerTraits = trait_chooser(5)
botTraits = trait_chooser(5)
def traitValueFinder(TraitList):
    charTotalValue = 0
    for trait in TraitList:
        if trait in SuperGoodTraits:
            charTotalValue += 2
        elif trait in goodTraits:
            charTotalValue += 1
        elif trait in badTraits:
            charTotalValue -= 1
        elif trait in SuperBadTraits:
            charTotalValue -= 2
    return charTotalValue


playerTraitValue = traitValueFinder(playerTraits)
botTraitValue = traitValueFinder(botTraits)

def battle():
    
    if playerTraitValue > botTraitValue:
        return 1
    elif playerTraitValue < botTraitValue:
        playerTraits.remove(random.choice(playerTraits))
        playerTraits.remove(random.choice(playerTraits))
        return -1
    else:
        return 0
    
Wins = 0
while 1:
    print("Your traits:", playerTraits, "\n your total trait value: ", playerTraitValue,"\n\n")
    startGame = input("Do you want to start the game(to win you must win 4 battles), (y/n): ")
    if startGame.lower() in 'yes' and Wins < 5:
        print(f"Name: {name}\nAge: {age}\nTraits: {playerTraits}\nPoints: {playerTraitValue},\n\n\nVS")
        print(f"\n\n\nBotName: {random.choice(BotNames)}\nBotAge: {random.randint(1,110)}\nTraits: {botTraits}\nPoints: {botTraitValue}")

        battleResult = battle()

        if battleResult == 1:
            Wins+=1
            print("you won, no traits will be destroyed")
        elif battleResult == -1:
            print("You lost, 2 traits have been taken")
        else:
            print("tie, no traits removed")
        
            

        playerTraitValue = traitValueFinder(playerTraits)
        botTraits = trait_chooser
        print("\n\n-----------------------------------------------------")
        print("If you lost you can reroll your traits(reroll) :")
        if len(playerTraits) < 2:
            print("you lost")
            break
    elif startGame.lower() in 'reroll':
        playerTraits = trait_chooser(5)
        playerTraitValue = traitValueFinder(playerTraits)
    else:
        break

    
    
print("\n\nfinished the game")