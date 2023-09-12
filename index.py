import random

options = ['Rock', 'Paper', 'Scissors']

def printOptions():
    print("Rock Paper Scissor Game!")
    print("1) Rock")
    print("2) Paper")
    print("3) Scissor")

def get_option():
    user_action = input("Enter a Choice : ")

    if user_action == '1':
        user_chose = options[0]
    elif user_action == '2':
        user_chose = options[1]
    elif user_action == '3':
        user_chose = options[2]
    else:
        print('Unknown Input, Try Again!\n')
        start()

    return user_chose


def start():
    printOptions()
    user_chose = get_option()
    computer_chose = random.choice(options)

    if user_chose == computer_chose:
        print(f'{user_chose} VS {computer_chose} | Result: Tied')
    # Rock
    elif user_chose == options[0]: 
        if computer_chose == options[1]:
            print(f'{user_chose} VS {computer_chose} | Result: Computer Win')
        elif computer_chose == options[2]:
            print(f'{user_chose} VS {computer_chose} | Result: You Win')
    # Paper
    elif user_chose == options[1]:
        if computer_chose == options[0]:
            print(f'{user_chose} VS {computer_chose} | Result: You Win')
        elif computer_chose == options[2]:
            print(f'{user_chose} VS {computer_chose} | Result: Computer Win')
    # Scissor 
    elif user_chose == options[2]:
        if computer_chose == options[0]:
            print(f'{user_chose} VS {computer_chose} | Result: Computer Win')
        elif computer_chose == options[1]:
            print(f'{user_chose} VS {computer_chose} | Result: You Win')

    print(f'')
    start()

start()