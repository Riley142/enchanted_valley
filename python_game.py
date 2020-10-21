import time

# Game over & play again
def game_over():
    print("GAME OVER")
    time.sleep(2)

    global answer
    answer = input ("Do You want to play again? [Y/N]")
    if answer == "Yes" or answer == "yes" or answer == "Y" or answer== "y":
        start_game()
    elif answer == "No" or answer == "no" or answer == "N" or answer == "n":
        print("Ok, bye!")


#Options for path 1
def option_b():  
    print ("While frantically running, you dropped your spell book and your sachel in the mud. You quickly reach down and grab it,")
    time.sleep(1)
    print("and start reading the Expecto Patronum spell but it does not work. You try to calm your heavy breathing as you hide")
    time.sleep(1)
    print("behind a haunted building, watching out for Bojo as it's past your 10pm curfew.")
    

    answer = input("You notice a purple flower near your foot. Do you pick it up? Y/N")
    if answer == "Y" or "Yes":
        time.sleep(1)
        flower = 1 #adds a flower
    else:
        flower = 0
        time.sleep(1)
        print ("You hear its heavy footsteps and ready yourself for the impending Bojo.")
        time.sleep(1)
    if flower > 0:
        print ("You quickly hold out the purple flower, somehow hoping it will stop Bojo.")
        time.sleep(1)
        print("It does! He was looking for love")
        time.sleep(1)
        print("Things got pretty weird, but you survived!")
        time.sleep(1)
        print("You win!")
    else: #If the user didn't grab the sword
        time.sleep(1)
        print ("Maybe you should have picked up the flower.You died!")
        game_over()
        

#Options for path 2

def frogs():
    print("The sound of nature mesmarized You right?")
    time.sleep(2)
    print("Don't You feel very relaxed and sleepy already?")
    time.sleep(2)
    print("The frogs have hypnotized You. You're not sure which path You've chosen...")
    time.sleep(2)
    choose_your_path()

def giant():
    print("As You come closer, the shining thing is getting bigger and bigger.")
    time.sleep(2)
    print("You realize it's look like man... An iron giant man.")
    time.sleep(2)
    print("Before You can see his face, he crushes You like a fly")
    time.sleep(2)
    game_over()

def bird():
    time.sleep(2)
    print("The sound of birds are getting louder and louder until You realize they're all coming from a giant bird in a magic hat")
    time.sleep(2)
    print("When You're close enough the Bird Wizard turns too You and asks:")
    time.sleep(2)

    global answer
    answer = input ("What is the only way out of my forest: [on a blue [1] or a red [2] carpet? Choose wisely!]")
    time.sleep(1.5)
    if answer == "1":
        print("The carpet flies You to the castle on top of the hill.")
        time.sleep(2)
        print("It looks dark and scary. The Magic bird flies from the inside and says:")
        time.sleep(2)
        print("You can kill me and take this castle and all the gold and treasure You find inside it! Or You can leave the Valley and let me live...")
        time.sleep(2)
        answer = input ("What do You do? I came this far! [1 Kill / 2 Leave]")
        if answer == "1":
            time.sleep(2)
            print("Youu grab a knife and attack the bird! \n 'You choose poorly' {} ! You're Evil, dissapear!".format(character))
            time.sleep(3)
            print("The bird put a spell on You... Everything is getting darker...")
            time.sleep(2)
            game_over()
        
    elif answer == "2":
        time.sleep(2)
        print("The castle start falling apart brick by brick!")
        time.sleep(2.5)
        print("The Magic bird says 'You broke the spell! All the people & animals can now live peacefully in this Enchanted Valley!'")
        time.sleep(2.5)
        print("Congrats {} *YOU WON*!".format(character))
    

#Options for path 3
def one():
    time.sleep(1)
    global answer2
    answer2 = input("Nothing change man, you're back to the entrace of the meadow... if would you like to go back to any other path press [1]...  or may you would try the excited experience through the mushroom ground? press [2]")
    if answer2 == "1":
        choose_your_path()
    elif answer2 == "2":
        print("You've been poisoned ...")
        time.sleep(1) 
        print("You should have taken another path champ...RETRY!!")
        time.sleep(2)
        game_over()

# Options for path 4
def option():
    time.sleep(2)
    answer = input ("You remain unfaltered in your journey, and decide to fight. The Dark Lord begins advances. Will you: [A - Run/ B - Fight back/C - Slash a sword]") 
    time.sleep(2.5)
    if answer == "A":
        print("You are a weakling")
        time.sleep(1)
        print("You're runing a way to the cross road, this time pick a safer path!")
        time.sleep(2)
        choose_your_path()
    elif answer == "B":
        print("Throwing a spell!")
        time.sleep(1.5)
        print("The spell takes You to a Wizard birds forest!")
        time.sleep(1)
        bird()
    elif answer == "C":
        print("Cut a deep wound that causes The Dark Lord to bleed to death")
        time.sleep(2)
        game_over()
   

#Tangarine's Lake
def path1():
    time.sleep(1)
    print ("A. Search your backpack for a weapon and fight Bojo / B. Lie down, think how to negotiate for your life / C. Run so You do not get mauled")
    answer = input("\nUse A , B, or C")
    if answer == "A":
        print("Ah rats, you did not bring your mace with you!\nYou died!")
        game_over()
    elif answer == "B":
        print("Really? You're wait in silence until Bojo passesas he can see very well in the dark after 10pm")
        option_b()
    elif answer == "C":
        print("You run as quickly as possible, but Bojo's speed is too fast. You perish!!")
        game_over()
     
#Thorny Path
def path2():
    time.sleep(1.5)
    print("You find Yourself on a Thorny Path,the further You go the darker it gets...")
    time.sleep(2)
    print("In front of You three roads unravel:")
    time.sleep(2)
    print("First One is a boggy and mossy road, You can hear the sounds of nature coming of that side.")
    time.sleep(2)
    print("Second one is dark & erie but You can see something shining in the distance.")
    time.sleep(2)
    print("Third one looks like normal forest road with tiny twigs and bird feathers twirling on the ground, You can hear the birds chirping in the distance.")
    time.sleep(3)
    
    answer = input ("Which one is calling Your name ? [1 - 2 - 3]")
    if answer == "1":
        frogs()
    elif answer == "2":
        giant()
    elif answer == "3":
        bird()

#Blue Meadow
def path3():
    print("Cool ! You choose to walk through the Blue Meadow...") 
    time.sleep(1)
    print ("But there's a cross roads...")
    
    global answer
    answer = input ("[1] Muddy path , [2] Mushroom ground")
    if answer == "1": 
        print(".....")
        print("Walking...Walking...")
        time.sleep(1.5)
        one()
    elif answer == "2":
        print("DAMN...You've been poisoned :/" ) #GAME OVER
        time.sleep (2)
        game_over()


#Epping Valley
def path4():
    time.sleep(1.5)
    print("You proceed and come across The Dark Lord of Epping Valley. He stands before you 9 feet tall and covered pitch black armour.")
    time.sleep(3)
    print("Noble {}! You've made a grave mistake coming here:".format(character))
    time.sleep(2)
    print("Upon this land you have trespassed, and you shall pay the price")
    time.sleep(2)
    option()

def choose_your_path():
    time.sleep(2)
    print("A slobbering Bojo is running towards you. Will You:")
    # Ask Jay why don't we need a global 
    answer = input("Which way do You choose? [1 for Tangarine's Lake / 2 for Thorny Path /  3 for Blue Meadow / 4 for Epping Valley]")
    
    if answer == "1":
       time.sleep(1.5)
       path1()
    elif answer == "2":
        time.sleep(1.5)
        path2()
    elif answer == "3":
        time.sleep(1.5)
        path3()
    elif answer == "4":
        time.sleep(1.5)
        path4()
   

def dialogue():
    time.sleep(1)
    print("Once upon a time in a land called Far Far Away ")
    time.sleep(2)
    print("You wake up the next morning in a thick, spooky part of forest in the enchanted Epping Valley. ")
    time.sleep(3)
    print("You stand and awe at the new, unfamiliar setting.") 
    time.sleep(2)
    print("The peace quickly fades when you encounter a horrifing sound emitting behind you.")
    choose_your_path()

def level_one():
    time.sleep(1)
    global character
    character = input("To prove you're not a complete muggle. Remind me again, what character did you select?")
    time.sleep(1)
    print("Okay noble {}! I hope you're ready, here we go:".format(character))
    dialogue()

def character_choice():
    character = input("Wizard, Nymph, Vampire, Scooby Doo, Dragon, Hydra, or Loch Ness Monster ?")
    if character == "wizard" or character == "Wizard":
        print("You have selected the Wizard!")
        level_one()
    elif character == "nymph" or character == "Nymph":
        print("You have selected the Nymph")
        level_one()
    elif character == "vampire" or character == "Vampire":
        print("You have selected the Vampire!")
        level_one()
    elif character == "scooby doo" or character == "Scooby Doo":
        print("You have selected the Scooby Doo!")
        level_one()
    elif character == "dragon" or character == "Dragon":
        print("You have selected the Dragon!")
        level_one()
    elif character == "hydra" or character == "Hydra":
        print("You have selected the Hydra!")
        level_one()
    elif character == "loch ness monster" or character == "Loch Ness Monster":
        print("You have selected the Loch Ness Monster!")
        level_one()
    else:
        print("Come on now, you've been given a list of characters, why choose on that isn't even there!?")
        time.sleep(1)
        print("YOU MUGGLE! Try again!")
        character_choice()

def start_game():
    answer = input("Do you dare to select a character and commence the game? Yes or No\n")
    if answer == "Yes" or answer == "yes" or answer == "Y" or answer== "y":
        character_choice()
    elif answer == "No" or answer == "no" or answer == "N" or answer == "n":
        print("How are you going to proceed in the game without selection a character? You lemon!")
        time.sleep(1)
        print("Please. Select a character and don't be a fool this time.")
        start_game()

start_game()