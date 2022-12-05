# dice probability simulation
import random
min = 1
def dice_trial(diceQuantity, diceSides):
    # dice_trials should simulate rolling 3 six sided dice
    sum = 0
    for i in range(int(diceQuantity)):
        sum += random.randint(1, int(diceSides))
    return sum
def simulate():
    diceSides = int(input("How many dice sides? :"))
    diceQuantity = int(input("How many dice? :"))
    trialQuantity = int(input("Trial sample size? :"))
    trials = []
    for i in range(trialQuantity):
        trials.append(dice_trial(diceSides, diceQuantity))
    print(sum(trials)/trialQuantity)
    return(sum(trials)/trialQuantity)
simulate()