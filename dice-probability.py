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
    diceSides = int(input("How many sides should the dice have? :"))
    diceQuantity = int(input("How many die to roll? :"))
    trialQuantity = int(input("Trial sample size? (1000 is a good base) :"))
    trials = []
    for i in range(trialQuantity):
        trials.append(dice_trial(diceSides, diceQuantity))
    print(sum(trials)/trialQuantity)
    return(sum(trials)/trialQuantity)
simulate()