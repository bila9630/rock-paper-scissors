#!/usr/bin/env python3

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""
import random
import time
moves = ['rock', 'paper', 'scissors']  # all possible moves

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    wins = 0  # a variable "wins" to count how many wins
    my_move = ""  # empty variable to contain the own move
    their_move = ""  # empty variable to contain the opponent move

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):  # this method is to tell
        self.my_move = my_move  # the player what the other player's move was
        self.their_move = their_move


class RandomPlayer(Player):  # Random player who just pick a random move
    def move(self):
        return random.choice(moves)


class HumanPlayer(Player):
    def move(self):
        # ask for user input
        the_player_input = input("Please insert either paper,"
                                 "rock or scissors: ")
        if the_player_input in moves:
            # check if the input is valid
            return the_player_input
        else:
            print("The choice you make is invalid,"
                  " please enter something again")
            time.sleep(1)
            self.move()
            # if there is something else, the user will be asked again.


class ReflectPlayer(Player):
    def move(self):
        if self.their_move in moves:  # check if there is something to reflect
            return self.their_move
        else:
            return random.choice(moves)


class CyclePlayer(Player):
    def move(self):  # return the move
        # that you didnt use before
        if self.my_move == "rock":
            return "paper"
        elif self.my_move == "paper":
            return "scissors"
        elif self.my_move == "scissors":
            return "rock"
        else:  # If there is nothing to cycle , just play some random move
            return random.choice(moves)


# Player input will be placed. It will return true or false
def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2):  # set the player
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        move1 = self.p1.move()  # giving each player move a variable
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        self.p1.learn(move1, move2)  # assign move of the player to "learn".
        # It is only to remember which move the player/opponent make
        self.p2.learn(move2, move1)
        if beats(move1, move2):  # using the beats method to see who wins.
            self.p1.wins += 1
            time.sleep(1)
            print(f"PLAYER 1 WINS WITH THE SCORE OF {self.p1.wins}"
                  f" to {self.p2.wins}")
        elif beats(move2, move1):
            self.p2.wins += 1
            time.sleep(1)
            print(f"PLAYER 2 WINS WITH THE SCORE OF {self.p2.wins}"
                  f" to {self.p1.wins}")
        else:
            time.sleep(1)
            print(f"IT'S A TIE! THE SCORE IS {self.p1.wins}"
                  f" to {self.p2.wins}")

    def play_game(self):
        print("Game start!")
        for round in range(3):
            print(f"Round {round}:")
            self.play_round()
        print("Game over!")
        time.sleep(1)
        if self.p1.wins > self.p2.wins:  # announce the winner
            print(f"Player 1 wins the game with a score of {self.p1.wins}"
                  f" to {self.p2.wins}")
        elif self.p2.wins > self.p1.wins:
            print(f"Player 2 wins the game with a score of {self.p2.wins}"
                  f" to {self.p1.wins}")
        else:
            print(f"Nobody wins. Both players "
                  f"have the score of {self.p1.wins}")


if __name__ == '__main__':
    game = Game(HumanPlayer(), ReflectPlayer())
    game.play_game()
