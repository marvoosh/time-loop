# Story by: Tim Statler
# Copyright: Comp Sci Central @ compscicentral.com

import sys
import time

a = 2
b = 0.2
c = 0.08

def openingCresits():
    print()
    print()
    print("     ####################")
    print("     #                  #")
    print("     #  Welcome to the  #")
    print("     #    TIME LOOP     #")
    print("     #                  #")
    print("     ####################")
    print()
    print()
    time.sleep(a)
    print("Wha... What happened? How did I get here??")
    time.sleep(a)
    print("I can't see anything.. What is this place????")
    time.sleep(a)
    print()

def startGame():
    start = input("Would you like to start the game?  [Y/N]: ").lower()
    if start == 'n':
        print("Maybe next time.. :( ")
    else:
        intro()

def char_print_slow(s):
    for char in s:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(b)
    time.sleep(1)
    print()

def char_print_fast(s):
    for char in s:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(c)
    time.sleep(1)
    print()

def intro():
    print()
    print("(Everything is dark)")
    time.sleep(a)
    print("You feel around, using your hands to see.")
    time.sleep(a)
    print("The ground is cold, damp, and covered in thick vines.")
    time.sleep(a)
    print("You feel a round rock that sinks into the floor when you press it.")
    time.sleep(a)
    print("The ground starts rumbling.")
    time.sleep(a)
    print("Light begins flooding in.")
    time.sleep(a)
    print()
    s = '"I\'m in a cave...?"'
    char_print_slow(s)
    print()
    print("The rock released a boulder that was blocking the cave entrance.")
    time.sleep(a)
    print("Three paths are revealed:")
    time.sleep(a)
    print()
    print("Path #1: Exit forward through the caves entrance, into the light.")
    time.sleep(a)
    print("Path #2: Explore the depths of the rear of the cave, into the darkness.")
    time.sleep(a)
    print("Path #3: Climb down the vines into a bottomless hole in the ground.")
    time.sleep(a)
    print()
    firstPath = input("Which path will you choose? (1/2/3): ")
    if firstPath == "1":
        print()
        path1()
    elif firstPath == "2":
        print()
        path2()
    else:
        print()
        path3()


def path1():
    print("You exit forward through the cave's entrance, into the light.")
    time.sleep(a)
    print("It's incredibly bright but your vision adjusts as you continue.")
    time.sleep(a)
    print("The cave exit closes, there's no going back now.")
    time.sleep(a)
    print("You look out and see that you're about halfway down an incredible mountain.")
    time.sleep(a)
    print("A man calls out to you")
    time.sleep(a)
    print()
    s = '"Hello there!...'
    char_print_slow(s)
    s = "...My name is APOLLO. I thought you were my sister, ARTEMIS..."
    char_print_fast(s)
    s = "...Ah, now I remember you! Yes, you're looking for CHRONOS..."
    char_print_fast(s)
    s = "...He's the one who trapped you in this time loop..."
    char_print_fast(s)
    s = "...Yet, I cannot bring you to him..."
    char_print_fast(s)
    s = "...Only HERMES can do that..."
    char_print_fast(s)
    s = "...However, I have heard that CHRONOS dwells at the base of this mountain.\""
    char_print_fast(s)
    time.sleep(1)
    print()
    print()
    print("There are two paths to take to the bottom of the mountain:")
    time.sleep(a)
    print("Path #1: Take the set path down the mountain.")
    time.sleep(a)
    print("Path #2: Scale down the side of the mountain.")
    time.sleep(a)
    print()
    secondPath = input("Which path will you choose? (1/2): ")
    if secondPath == '1':
        path1_1()
    elif secondPath == '2':
        path1_2()

def path1_1():
    print()
    print("You begin walking down the mountain toward the bottom.")
    time.sleep(a)
    print("The path is long and winding but the walk is not difficult.")
    time.sleep(a)
    print("The sky is bright and blue and a warm breeze hits your face.")
    time.sleep(a)
    s = '  "I could get used to this..."'
    for character in s:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(b)
    time.sleep(.25)
    print('  --You think to yourself.')
    time.sleep(a)
    print("A boy calls out to you.")
    time.sleep(a)
    print()
    s = '"Hey! Wait up!...'
    char_print_slow(s)
    s = "...My name is ARES. I was just coming down the mountain for some fresh air..."
    char_print_fast(s)
    s = "...Mount OLYMPUS is the highest reaching mountain on Earth and the air is specially crisp..."
    char_print_fast(s)
    s = "...Anyhow, I see you're searching for the correct path, as we all are..."
    char_print_fast(s)
    s = "...It's not my place to tell you which path is correct..."
    char_print_fast(s)
    s = "...However, I will tell you this..."
    char_print_fast(s)
    print()
    s = '..."ONLY THROUGH DARKNESS WILL FREEDOM BE ATTAINED"'
    char_print_slow(s)
    print()
    time.sleep(a)
    intro()


def path1_2():
    print()
    print("You begin scaling down the side of the mountain toward the bottom.")
    time.sleep(a)
    print("It's a long way down but you soon grow strong enough to appreciate the view.")
    time.sleep(a)
    print("Although you're still about halfway up the mountain, clouds surround you and the world seems small.")
    time.sleep(a)
    s = '  "I don\'t believe my eyes..."'
    for character in s:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(b)
    time.sleep(.25)
    print('  --You think to yourself')
    time.sleep(a)
    print()
    print("You continue down the mountain for days until you reach the bottom.")
    time.sleep(a)
    s2 = '  "Finally! I can face you, CHRONOS!"'
    for character in s2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(b)
    time.sleep(.25)
    print('--You yell, entering the base of Mount OLYMPUS through the largest red and black doors you\'ve ever seen')
    time.sleep(a)
    print("The darkness consumes you as you enter, unable to see a thing.")
    time.sleep(a)
    print("A thunderous voice calls out to you...")
    time.sleep(a)
    print()
    s = "Ah... I've been expecting you. But you're far too early..."
    char_print_fast(s)
    s = "...It appears you've taken a fairly easy route..."
    char_print_fast(s)
    s = "...You can see through the light, but not the DARKNESS..."
    char_print_fast(s)
    s = "...You've developed some STRENGTH, but not enough..."
    char_print_fast(s)
    s = "...There is more you need to grow..."
    char_print_fast(s)
    s = "...More you need to LEARN"
    char_print_fast(s)
    s = "...And learn you will"
    char_print_fast(s)
    s = "...In time..."
    char_print_slow(s)
    intro()


def path2():
    print("You explore the depths of the rear of the cave, into the darkness.")
    time.sleep(a)
    print("It's incredibly dark but your vision adjusts as you continue forward.")
    time.sleep(a)
    print("A huge boulder slides into place behind you, blocking your path back.")
    time.sleep(a)
    print("You notice that the cave floor is declining to the left, like a spiral.")
    time.sleep(a)
    print("A woman calls out to you.")
    time.sleep(a)
    print()
    s = '"Hello there!...'
    char_print_slow(s)
    s = "...My name is ARTEMIS... I thought you were my brother, APOLLO..."
    char_print_fast
    s = "...Ah, now I remember you! Yes, you're looking for CHRONOS..."
    char_print_fast(s)
    s = "...He's the one who trapped you in this time loop..."
    char_print_fast(s)
    s = "...However, I cannot bring you to him..."
    char_print_fast(s)
    s = "...Only HERMES can do that..."
    char_print_fast(s)
    s = "...However, I have heard that CHRONOS dwells at the base of this cave..."
    char_print_fast(s)
    print()
    print("There are two paths to continue through the cave:")
    time.sleep(a)
    print("Path #1: Go to the left.")
    time.sleep(a)
    print("Path #2: Go to the right.")
    time.sleep(a)
    print()
    secondPath = input("Which path will you choose? (1/2): ")
    if secondPath == '1':
        path2_1()
    elif secondPath == '2':
        path2_2()

def path2_1():
    print()
    print("You take the fork in the cave to the left and continue walking.")
    time.sleep(a)
    print("The cave floor is still declining but is becoming much steeper than before.")
    time.sleep(a)
    print("It's so dark and the winding cave seems to go on forever.")
    time.sleep(a)
    s = "I have no choice, I must keep going..."
    for character in s:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(b)
    time.sleep(.25)
    print('  --You think to yourself')
    time.sleep(a)
    print("Still going, fortifying your will, until finally, you reach the largest red and black door in existence.")
    time.sleep(a)
    print()
    s = '  "Finally! I can face you, CHRONOS!"'
    for character in s:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(b)
    time.sleep(.25)
    print('  --You erupt as you enter the doors at the base of the cave inside Mount OLYMPUS')
    time.sleep(a)
    print()
    print("Standing now in the largest room, in front of the largest man you've ever seen.")
    time.sleep(a)
    print("The room is dark, but you can see the source of the thunderous voice which calls out to you...")
    time.sleep(a)
    print()
    s = "Ah... I've been expecting you. But you're still too early..."
    char_print_fast(s)
    s = "...It appears you've taken a fairly easy route..."
    char_print_fast(s)
    s = "...Your vision is keen. You see through the darkness and the light..."
    char_print_fast(s)
    s = "...However, you haven’t developed quite enough strength..."
    char_print_fast(s)
    s = "...There is more you need to grow..."
    char_print_fast(s)
    s = "...More you need to learn..."
    char_print_fast(s)
    s = "...And learn you will..."
    char_print_fast(s)
    s = "...In time."
    char_print_slow(s)
    time.sleep(a)
    intro()

def path2_2():
    print()
    print("You take the fork in the cave to the right and continue walking.")
    time.sleep(a)
    print("The cave floor is now inclining and is becoming quite steep.")
    time.sleep(a)
    print("It's so dark but after what seems like days of walking, you see a glow in the distance.")
    time.sleep(a)
    s = '  "What in the world can that be...?"'
    for character in s:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(b)
    time.sleep(.25)
    print('  --You think to yourself')
    time.sleep(a)
    print("Approaching the brilliant light, you reach the end of this path and see an old book perched atop a pedestal")
    time.sleep(a)
    print()
    s = '  "THE SECRETS OF TIME"'
    for character in s:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(b)
    time.sleep(.25)
    print('  --You read the large inscription on the cover before opening the book.')
    print()
    time.sleep(a)
    s = '"If you stumble upon this tomb...'
    char_print_fast(s)
    s = "...It may save you from your doom..."
    char_print_fast(s)
    s = "...Your vision is keen, that much is clear..."
    char_print_fast(s)
    s = "...But you have yet to face your fear..."
    char_print_fast(s)
    s = '...The truest path is one of toil..."'
    char_print_fast(s)
    s = "...Climb down vines beneath the soil..."
    char_print_fast(s)
    s = "...Speak with MOIRAE, help her first..."
    char_print_fast(s)
    s = "...Then you will complete your search..."
    char_print_fast(s)
    time.sleep(a)
    intro()


def path3():
    print("You climb down the vines into a bottomless hole in the ground")
    time.sleep(a)
    print("A huge boulder slides into place above you, blocking your escape.")
    time.sleep(a)
    print("You continue climbing down the vines until you hear something whirring up at you.")
    time.sleep(a)
    print("Someone calls out to you.")
    time.sleep(a)
    print()
    s ='"Hey, hey there!...'
    char_print_slow(s)
    s = "...My name is HERMES... I'll be your guide to freedom..."
    char_print_fast(s)
    s = "...Yes, I know all about you! You're looking for CHRONOS..."
    char_print_fast(s)
    s = "...He's the one who trapped you in this time loop..."
    char_print_fast(s)
    s = "...I'm on my way to deliver a message, so I can't escort you personally..."
    char_print_fast(s)
    s = "...However, I can transport you there, or anywhere else on Mount OLYMPUS..."
    char_print_fast(s)
    s = "...CHRONOS is just below and he'll certainly TEST YOU when you meet him."
    char_print_fast(s)
    print()
    print("HERMES will transport you anywhere on Mount OLYMPUS:")
    time.sleep(a)
    print("Path #1: Continue below to face CHRONOS.")
    time.sleep(a)
    print("Path #2: Read: THE SECRETS OF TIME.")
    time.sleep(a)
    print("Path #3: Speak with ARES.")
    time.sleep(a)
    print("Path #4: Speak with ARTEMIS.")
    time.sleep(a)
    print("Path #5: Speak with APOLLO.")
    time.sleep(a)
    print()
    secondPath = input("Which path will you choose? (1/2/3/4/5): ")
    if secondPath == "2":
        path2_2()
    elif secondPath == "3":
        path1_1()
    elif secondPath == "4":
        path1()
    elif secondPath == "5":
        path2()
    else:
        print()
    print("You continue down the vines until you reach the bottom.")
    time.sleep(a)
    print("You see a small old woman next to the largest red and black iron-wrought double-doors you've ever seen.")
    time.sleep(a)
    print('The old woman calls out to you')
    time.sleep(a)
    print()
    s = '"Hello there, young traveler...'
    char_print_fast(s)
    s = '...My name is MOIRAE, I\'m in great need of help...'
    char_print_fast(s)
    s = '...I know who you seek... CHRONOS is just beyond this door...'
    char_print_fast(s)
    s = '...If you enter, you may speak with him and restore your freedom...'
    char_print_fast(s)
    s = '...But before you do so, would you take me HOME?...'
    char_print_fast(s)
    s = '...The choice is yours."'
    char_print_fast(s)
    print()
    print("Path #1: Forget the old woman. Enter the doors and speak with CHRONOS.")
    time.sleep(a)
    print("Path #2: Honor the woman's request. Help MOIRAE return home safely.")
    time.sleep(a)
    thirdPath = input("Which path would you like to take? (1/2): ")
    if thirdPath == "1":
        path3_1()
    elif thirdPath == "2":
        path3_2()

def path3_1():
    print()
    print('You begin walking toward the doors, ignoring MOIRAE\'s request')
    time.sleep(a)
    print('"I would help you but I\'m in a bit of a hurry, you understand"')
    time.sleep(a)
    print("You pull open the massive doors with all of your might and enter")
    time.sleep(a)
    print("Standing now in the largest room, in front of the largest man you've ever seen.")
    time.sleep(a)
    print("The room is dark, but you can see the source of the thunderous voice which calls out to you...")
    time.sleep(a)
    print()
    s = "Ah... I've been expecting you. But you're somewhat early..."
    char_print_fast(s)
    s = "...It appears you've taken a fairly hard route..."
    char_print_fast(s)
    s = "...Your vision is keen. You see through the darkness and the light..."
    char_print_fast(s)
    s = "...And your strength has grown from your travels..."
    char_print_fast(s)
    s = "...However, there is still just one..."
    char_print_fast(s)
    s = "...One more thing you need to learn..."
    char_print_fast(s)
    s = "...And learn you will..."
    char_print_fast(s)
    s = "...In time."
    char_print_slow(s)
    intro()

def path3_2():
    print()
    print('You begin walking toward MOIRAE, honoring her request')
    time.sleep(a)
    print('  "I understand. I know what it\'s like to miss home... That\'s why I need to get out of here..."')
    time.sleep(a)
    print('  "But before I walk through those doors, I promise that I\'ll get you home safely."')
    time.sleep(a)
    print()
    print("You kneel down in front of MOIRAE, allowing her to climb easily onto your back.")
    time.sleep(a)
    print("Standing up, you make your way back to vine wall to make your ascent.")
    time.sleep(a)
    print("Just as you grab the vines, the enormous red and black iron doors thrust open, slamming to a halt.")
    time.sleep(a)
    print("The largest man you've ever seen steps out and his thunderous voice which calls out to you...")
    time.sleep(a)
    print()
    s = "Ah... I've been expecting you. And you're right on time!..."
    char_print_fast(s)
    s = "...It appears you've taken a very difficult route..."
    char_print_fast(s)
    s = "...Your vision is keen. You see through the darkness and the light..."
    char_print_fast(s)
    s = "...And your strength has grown from your travels..."
    char_print_fast(s)
    s =  "...You have learned everything I have to teach you..."
    char_print_fast(s)
    s = "...So you may finally be free..."
    char_print_fast(s)
    s = "...It's time to return."
    char_print_slow(s)
    print()
    time.sleep(a)
    print("Thanks for playing!  ʕ•ᴥ•ʔ")


openingCresits()
startGame()
