import time
import random
villains = ['goblin', 'rhino', 'troll', 'Darth Vader']

weapons = []
visited = set()


def print_pause(prompt):
    print(prompt)
    time.sleep(2)


def intro(villians):
    villain = random.choice(villains)
    print_pause('You find yourself standing in a open field.')
    print_pause('Rumor has that a {} is somewhere around here, \
                   and has been \
                   terryfying the nearby village.'.format(villain))
    print_pause('Infront of you is the house.')
    print_pause('To the right of you is a cave.')
    print_pause('In your hand you hold the trusty \
                (but not very effective) dagger.')
    return villain


def approach():
    print_pause('Enter 1 to knock on the door of the house')
    print_pause('Enter 2 to peer into the cave')
    print_pause('What would you like to do?')


def choice_input(villain):
    # validates user input to choose if they want to go into the house or cave
    choice = input("(Please enter 1 or 2.)\n")

    if choice != '1' and choice != '2' and choice != ' ':
        choice_input(villain)
    else:
        if choice == '2':
            cave(villain)
        else:
            house(villain)


def to_be_or_not(villain):
    # validates user input to  choose to fight or runaway
    choice = input('Would you like to fight(1) or runaway(2)?\n')
    if choice != '1' and choice != '2' and choice != ' ':
        to_be_or_not(villain)
    else:
        if choice == '2' or choice == '1':
            fight(choice, villain)


def house(villain):
    print_pause('You approach the door of the house.')
    print_pause('You are about to knock when  \
            the door opens and out steps a {}.'.format(villain))
    print_pause('Eep! This is the {}"s house!'.format(villain))
    print_pause('The {} attacks you!'.format(villain))
    if 'sword' not in weapons:
        print_pause('You feel a bit under-prepared \
                    for this, what with only having a tiny dagger.')
        to_be_or_not(villain)
    else:
        to_be_or_not(villain)


def fight(choice, villain):
    if choice == '1' and 'sword' not in weapons:
        print_pause('You do your best...')
        print_pause('but your dagger is no match for the {}.'.format(villain))
        print_pause('You have been defeated!')
        choice = input('Would you like to play again? (y/n)\n')

        if choice == 'y':
            print_pause('Awesome sauce...restarting the game!')
            play_game()

    elif choice == '1' and 'sword' in weapons:
        print_pause('There is a struggle...')
        print_pause('but you win and are victorious!')
        choice = input('Would you like to play again? (y/n)\n')

        if choice == 'y':
            print_pause('Awesome sauce...restarting the game!')
            play_game()

    else:
        if choice == '2':
            print_pause('You get the hell out of there \
                        and run back into the field, \
                        you don"t seem to be followed.')
            approach()
            choice_input(villain)


def cave(villain):
    print_pause('You peer cautiously into the cave.')
    if 'cave' not in visited:
        print_pause('It turns out to be only a very small cave.')
        print_pause('Your eye catches a glint of metal behind a rock.')
        print_pause('You have found the magical Sword of Ogoroth!')
        print_pause('You discard your silly old dagger \
                        and take the sword with you.')
        print_pause('You walk back out to the field.')
        visited.add('cave')
        weapons.append('sword')
        approach()
        choice_input(villain)

    else:
        print_pause("You've been here before, \
                    and gotten all the good stuff. \
                    It's just an empty cave now.")
        print_pause("You walk back out to the field.")
        approach()
        choice_input(villain)


def play_game():
    villain = intro(villains)
    approach()
    choice_input(villain)


play_game()
