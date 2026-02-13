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
        return "you won, no traits will be destroyed"
    elif playerTraitValue < botTraitValue:
        playerTraits.remove(random.choice(playerTraits))
        playerTraits.remove(random.choice(playerTraits))
        return "You lost, 2 traits have been taken"
    else:
        return "tie, no traits removed"
    

while 1:
    startGame = input("Do you want to start the game(to win you must win three battles), (y/n): ")
    if startGame.lower() in 'yes':
        print(f"Name: {name}\nAge: {age}\nTraits: {playerTraits}\nPoints: {playerTraitValue},\n\n\nVS")
        print(f"\n\n\nBotName: {random.choice(BotNames)}\nBotAge: {random.randint(1,110)}\nTraits: {botTraits}\nPoints: {botTraitValue}")
        print(battle())
        print("-----------------------------------------------------")
        print("If you lost you can reroll your traits(reroll) :")
        if len(playerTraits) < 2:
            print("you lost")
            break
    elif startGame.lower() in 'reroll':
        
    else:
        break    
    
    
print("\n\nfinished the game")