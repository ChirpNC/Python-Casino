from random import *

suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
values = ['2','3','4','5','6','7','8','9','10','Jack','Queen','King','Ace']



def blackjack():
    global pcard1, pcard2, dcard1, dcard2, agaran, dgaran, dvalue, value, score, doublee
    score = 0
    agaran = 0
    dgaran = 0
    dvalue = 0
    doublee = False
    """
    agaran (ace garanty) is added 1 for every ace in the player's hand.
    It will subtract 10 of the total value if the total value goes above 21 and will be subtracted 1.
    This also means that an ace's value will be 11.
    dgaran is the same but for the dealer
    """
    pcard1 = choice(values)
    pcard2 = choice(values)
    dcard1 = choice(values)
    dcard2 = choice(values)

    print('\n\nYou have chosen to play blackjack \n\n')

    if pcard1=='Ace':
        agaran += 1
        value_pcard1 = 11
    elif pcard1 == 'Jack' or pcard1 == 'Queen' or pcard1 == 'King':
        value_pcard1 = 10
    else:
        value_pcard1 = int(pcard1)
    
    if pcard2=='Ace':
        agaran += 1
        value_pcard2 = 11
    elif pcard2 == 'Jack' or pcard2 == 'Queen' or pcard2 == 'King':
        value_pcard2 = 10
    else:
        value_pcard2 = int(pcard2)
    value = value_pcard1 + value_pcard2
    
    
    if value > 21:
        if agaran > 0:
            value -= 10
            agaran -= 1
        else:
            print('you lose :(')
            return
            
    print(f"You have a {pcard1} of {choice(suits)} and a {pcard2} of {choice(suits)} adding to a total value of {value} \nThe dealer has a {dcard1} of {choice(suits)}")
    
    
    if value_pcard1==value_pcard2:
        achoice()
    else:
        achoice()
    return(score)
        
        
def achoice():
    global pcard1, pcard2, dcard1, dcard2, agaran, dgaran, dvalue, value, score
    choice = input("You may either 'hit', 'stay' or 'double'. Which one do you chose? ")
    if choice=="hit":
        hit()
    elif choice=="stay":
        stay()
    elif choice=="double":
        double()
    else:
        print('invalid prompt')
        achoice()

def hitchoice():
    global pcard1, pcard2, dcard1, dcard2, agaran, dgaran, dvalue, value, score
    choice = input("You may either 'hit' or 'stay'. Which one do you chose? ")
    if choice=="hit":
        hit()
    elif choice=="stay":
        stay()
    else:
        print('invalid prompt')
        hitchoice()

def hit():
    global pcard1, pcard2, dcard1, dcard2, agaran, dgaran, dvalue, value, score
    p=choice(values)
    print(f"You pick up a {p} of {choice(suits)}")
    

    if p=='Ace':
        agaran += 1
        value_p = 11
    elif p == 'Jack' or p == 'Queen' or p == 'King':
        value_p = 10
    else:
        value_p = int(p)
    value += value_p
    
    if value > 21:
        if agaran > 0:
            value -= 10
            agaran -= 1
        else:
            print('You lose.')
            return
    print(f"You now have a total value of {value}")
    hitchoice()

def stay():
    global pcard1, pcard2, dcard1, dcard2, agaran, dgaran, dvalue, value, score, doublee
    dealervalue()
    print(f"The dealer reveals a {dcard2} of {choice(suits)}")
    print(f"The dealer has a total card value of {dvalue}")
    while dvalue < 17:
        dealercards()
        print(f"The dealer now has a total card value of {dvalue}")
        
    
    if 21 >= dvalue > value and doublee == False:
        print('The dealer has a greater card value than you.')
        print('You lose.')       
    elif 21 > value > dvalue and doublee == False:
        print('You win.')
        score = 2
    elif value == dvalue and doublee == False:
        print('Tie.')
        score = 1
    elif dvalue > 21 and value < 21 and doublee == False:
        print('You win.')
        score = 2
    elif 21 == value > dvalue and doublee == False:
        print('You win.')
        score = 3
    elif dvalue > 21 and value == 21 and doublee == False:
        print('You win.')
        score = 3
    elif 21 >= dvalue > value and doublee == True:
        print('The dealer has a greater card value than you.')
        print('You lose.')    
        score = 4  
    elif 21 > value > dvalue and doublee == True:
        print('You win.')
        score = 5
    elif dvalue > 21 and value < 21 and doublee == True:
        print('You win.')
        score = 5
    elif 21 == value > dvalue and doublee == True:
        print('You win.')
        score = 6
    elif dvalue > 21 and value == 21 and doublee == True:
        print('You win.')
        score = 6
    return

def double():
    global pcard1, pcard2, dcard1, dcard2, agaran, dgaran, dvalue, value, score, doublee
 
    print('You have doubled down.')
    doublee = True
    p=choice(values)
    print(f"You pick up a {p} of {choice(suits)}")
    

    if p=='Ace':
        agaran += 1
        value_p = 11
    elif p == 'Jack' or p == 'Queen' or p == 'King':
        value_p = 10
    else:
        value_p = int(p)
    value += value_p

    
    
    if value > 21:
        if agaran > 0:
            value -= 10
            agaran -= 1
        else:
            print('You lose.')
            return
    print(f"You now have a total value of {value}")
    stay()



def dealervalue():
    global pcard1, pcard2, dcard1, dcard2, agaran, dgaran, dvalue, value, score
        
    if dcard1=='Ace':
        dgaran += 1
        value_dcard1 = 11
    elif dcard1 == 'Jack' or dcard1 == 'Queen' or dcard1 == 'King':
        value_dcard1 = 10
    else:
        value_dcard1 = int(dcard1)
    
    if dcard2=='Ace':
        dgaran += 1
        value_dcard2 = 11
    elif dcard2 == 'Jack' or dcard2 == 'Queen' or dcard2 == 'King':
        value_dcard2 = 10
    else:
        value_dcard2 = int(dcard2)
    dvalue = value_dcard1 + value_dcard2
    
    
    if dvalue > 21:
        if dgaran > 0:
            dvalue -= 10
            dgaran -= 1
        else:
            print('The dealer bust.')
            return

def dealercards():
    global pcard1, pcard2, dcard1, dcard2, agaran, dgaran, dvalue, value, score
    d=choice(values)
    print(f"The dealer picks up a {d} of {choice(suits)}")

    if d=='Ace':
        dgaran += 1
        value_d = 11
    elif d == 'Jack' or d == 'Queen' or d == 'King':
        value_d = 10
    else:
        value_d = int(d)
    dvalue += value_d
    
    
    if dvalue > 21:
        if dgaran > 0:
            dvalue -= 10
            dgaran -= 1
        else:
            print('The dealer bust.')
            return