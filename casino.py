from blackjack import *

money = 100.00


def menu():
    global money
    print(f"\n\nYou have joined the casino. \nCurrently you have {money}$. \nYou may join a game of your choosing from our selection.")
    game = input('Our game selection is blackjack. \nWhich one would you like to choose ? ')
    if game == 'blackjack':
        bet = input('Choose your amount to bet: ')
        money -= float(bet)
        if money < 0:
            print('You are not alowed to bet more money than you have.')
            money += float(bet)
            menu()
        score = blackjack()
        print(score)
        if score == 0:
            bet = 0
            print('You lost your bet!')
        elif score == 1:
            print('You neither lost nor won any money!')
        elif score == 2:
            bet = int(bet)
            bet *= 2
            print('You doubled your bet!')
        elif score == 3:
            bet = int(bet)
            bet = float(float(bet) + float(bet*1.5))
        elif score == 4:
            bet = int(bet)
            bet -= 2*int(bet)
            print('You lost double your bet!')
        elif score == 5:
            bet = int(bet)
            bet *= 4
            print('You quadrupled your bet!')
        elif score == 6:
            bet = int(bet)
            bet = 2*(float(float(bet) + float(bet*1.5)))
        money += float(bet)
        print(f"You now have {money}$ left")
        if money < 1:
            print('You are out of money!')
            exit('exit code: poor')
        menu()
    elif game == 'stop':
        exit(0)
    else:
        print('invalid prompt')
        menu()

menu()

'''
blackjack score:
0 => lost
1 => tied
2 => won
3 => won with a blackjack
4 => lost with a double
5 => won with a double
6 => won with a double and a blackjack
'''