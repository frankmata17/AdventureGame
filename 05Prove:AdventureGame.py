def main():
    print()
    first_choice = input('You are walking through a dark forest and find two items: a MATCH and a FLASHLIGHT. Which one do you want to pick up?: ')

    if first_choice.lower() == 'match':
        handle_match_choice()
    elif first_choice.lower() == 'flashlight':
        handle_flashlight_choice()
    else:
        print('Invalid choice, you lost!')

def handle_match_choice():
    print()
    print('You pick up the match and strike it, and for an instant, the forest around you is illuminated.')
    print('You see a large grizzly bear, and then the match burns out.')
    print()
    second_choice = input('Do you CLIMB a tree or HIDE in the shadows?: ')

    if second_choice.lower() == 'climb':
        print('You climb a large tree, but you step on a broken branch and fall. You lost!')
    elif second_choice.lower() == 'hide':
        handle_hide_choice()
    else:
        print('Invalid choice. Game over.')

def handle_hide_choice():
    print()
    hide_choice = input('You hide in the shadows and avoid being seen by the grizzly bear. You continue walking when you reach a crossroads. Do you go LEFT or RIGHT?: ')

    if hide_choice.lower() == 'left':
        print('You walk a few feet when suddenly you fall into a giant pit. You lose.')
    elif hide_choice.lower() == 'right':  
        print('You choose the right and walk for a few miles until you make it safely out of the forest back to your car. You win.')
    else:
        print('Invalid choice. Game over.')

def handle_flashlight_choice():
    print()
    print('You pick up the flashlight and turn it on. You see the pathway lit up in front of you, but you thought you also heard something off to the side.')
    print()
    run_or_hide = input('Do you want to RUN, or HIDE behind a tree?: ')

    if run_or_hide.lower() == 'run':
        handle_run_choice()
    elif run_or_hide.lower() == 'hide':
        handle_hide_choice_after_flashlight()
    else:
        print('Invalid choice. Game over.')

def handle_run_choice():
    print()
    print('You run toward the lit up pathway in front of you and you come onto a bonfire surrounded by mysterious hooded figures.')
    print()
    talk_or_sneak = input('Do you TALK to them or SNEAK away?: ')

    if talk_or_sneak.lower() == 'talk':
        print('The mysterious figures rush towards you and attack you. You lose!')
    elif talk_or_sneak.lower() == 'sneak':
        print('You avoid them and make your way out of the forest. You win.')
        print()
    else:
        print('Invalid choice. Game over.')

def handle_hide_choice_after_flashlight():
    print('You hide behind a bush and suddenly you see a pack of wolves who have caught a scent.. your scent!')
    print()
    howl_or_throw = input('Do you HOWL like a wolf or THROW a rock to create a distraction?: ')

    if howl_or_throw.lower() == 'howl':
        print()
        print('You howl like a wolf and scare off the wolves, giving you a chance to escape. You win!')
    elif howl_or_throw.lower() == 'throw':
        print('You throw a rock in another direction, but the wolves see you and attack. Game over.')
    else:
        print('Invalid choice. Game over.')

if __name__ == "__main__":
    main()
