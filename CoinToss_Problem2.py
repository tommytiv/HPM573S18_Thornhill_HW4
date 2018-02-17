from enum import Enum
import numpy as np

class CoinToss(Enum): # State of each coin toss
    HEADS = 1
    TAILS = 0

class Game: #create cointoss game
    def __init__(self):
        self._rnd = np.random # generate random number for coin flip
        self._headProb = head_prob # probability of getting Heads
        self._CoinToss = [] # outcome of toss
        self._results = [] #outcome of all tosses in a Game

    def simulate(self, n_tosses):
        t = 0 # first toss
        while t < n_tosses: #while number of tosses has not been reached
            if self._rnd.sample() < self._headProb: #odds of getting heads
                self._CoinToss = CoinToss.HEADS
            else:
                self._CoinToss = CoinToss.TAILS #if not heads, then tails
            self._results.append(self._CoinToss.name) #create list of results
            t += 1 # repeat toss
            #print (t) #to check number of tosses

    def tally(self):
        countable = " ".join(map(str,self._results))
        wins = countable.count(winning_sequence)
        total = -(entry_fee)+(wins * reward)
        #print (countable) # TO CHECK for number of tosses
        #print (wins) # TO CHECK number of tosses
        #print (total) # TO CHECK total
        return total


class Rounds:
    def __init__(self, rounds):
        self.initialRounds = rounds
        self.games = []
        self.total_tally = []

        for i in range(rounds): # to iterate through rounds
            game = Game() # game is an instance of Game
            self.games.append(game) #create a list of games to append the talliies

    def play(self):
        for game in self.games:
            game.simulate(n_tosses) #initiate cointoss
            outcome = game.tally()
            self.total_tally.append(outcome)

    def get_avg_tally(self):
        return sum(self.total_tally)/len(self.total_tally)


# Values of constants
head_prob = 0.4
n_tosses = 10
num_rounds = 1000
entry_fee = 250
reward = 100
winning_sequence = "TAILS TAILS HEADS"


myRounds = Rounds(num_rounds) # Create rounds
myRounds.play() # Play rounds
print("Expected value:", myRounds.get_avg_tally())
print("\n")
print ("Based on a coin toss game with the following parameters:")
print ("Probability of getting Heads:",head_prob)
print ("Number of coin tosses per game:", n_tosses)
print ("Number of rounds of games:", num_rounds)
print ("Entry fee to play each game:", entry_fee)
print ("Reward for each winning sequence:", reward)
print ("Winning sequence:", winning_sequence)
