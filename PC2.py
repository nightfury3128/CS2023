"""The Game of Hog."""
from dice import four_sided, six_sided, make_test_dice

GOAL_SCORE = 100 # The goal of Hog is to score 100 points.

######################
# Phase 1: Simulator #
######################

def roll_dice(num_rolls, dice=six_sided):
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls > 0, 'Must roll at least once.'
    dice_total = 0  
    for _ in range(num_rolls):
        dice_outcome = dice() 
        if dice_outcome == 1:
            return 1
        dice_total += dice_outcome
    return dice_total

def take_turn(num_rolls, opponent_score, dice=six_sided):
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls >= 0, 'Cannot roll a negative number of dice.'
    assert num_rolls <= 10, 'Cannot roll more than 10 dice.'
    assert opponent_score < 100, 'The game should be over.'
    if num_rolls == 0:
        return max(opponent_score // 10 , opponent_score % 10) + 1
    else:
        return roll_dice(num_rolls, dice)

def select_dice(score, opponent_score):
    if (score + opponent_score) % 7 == 0:
        return four_sided
    else:
        return six_sided

def is_swap(score0, score1):
    return (score0 % 10 == score1 // 10) and (score1 % 10 == score0 // 10)

def other(who):
    return 1 - who

def play(strategy0, strategy1, score0=0, score1=0, goal=GOAL_SCORE):
    who = 0  
    while score0 < goal and score1 < goal:
        if (score0 + score1) % 7 == 0:
            current_dice = four_sided 
        else:
            current_dice = six_sided
        if who == 0:
            num_rolls0 = strategy0(score0, score1)  
            score0 += take_turn(num_rolls0, score1, current_dice)
        else:
            num_rolls1 = strategy1(score1, score0)  
            score1 += take_turn(num_rolls1, score0, current_dice)
        if is_swap(score0, score1):
            score0, score1 = score1, score0
        
        who = other(who)

    return score0, score1

def always_roll(n):
    def strategy(score, opponent_score):
        return n
    return strategy
