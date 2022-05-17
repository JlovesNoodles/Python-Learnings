from random import shuffle

def shuffle_cup():
    cups = [' ' , '0', ' ']
    shuffle(cups)
    return cups

V_shuffle_cup = shuffle_cup()

def user_guess():
    
    guess = ''
    while guess not in ['0', '1', '2']:
        
        guess = input("Choose A number between 0, 1, 2 -> ")
    return guess

guess = user_guess()


def the_game(V_shuffle_cup,guess):
    if V_shuffle_cup[int(guess)] == '0':
        print ("You got it right!")
        print (V_shuffle_cup)
    else:
        print("Try again")
        print(V_shuffle_cup)
        
        
        
the_game(V_shuffle_cup,guess)
