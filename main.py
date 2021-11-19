from display_stats import display_stats
from inn import inn
from progress_forward import progress_forward
from art import art_list
"""
LIST OF KEYWORDS TO SEARCH FOR LATER:
!COMBAT - main combat code
!STATIC - variables i set that should be dynamic later. Static for testing
!DATA - Lists for character, item, enemy etc
!CREATE need a function to do something
"""

"""
Our main loop should be a series of choices based on local or situation
Inn: 
1 - Rest
2 - Shop
3 - View inventory/Stats
3.5 - Level up?
4 - Leave Inn

The main "Map"
I imagine it looking something like:

Inn         Encounter                                                                                    "Boss" and End!
[] ____________*______________*_______________*______________*______________*_____________*__________*________#

and encounters can be monsters with a chance for something else. Maybe a trap, a treasure, or a place to rest
Input Menu:
1 - Move forward
2 - Back to town (encounters need to be reset when you go back)
3 - view inventory/stats
4 - Use Consumable

"""
#!DATA
enemy = {
    'wolf' : {
        'solo' : 'a wolf',
        'many' : 'a pack of wolves',
        'health' : 15, # basic health for one enemy
        'base_lvl' : 1, # base level, which i can manipulate later, or use to increase difficulty down the road. level 1's wont show up at the end, for instance
        'exp_gain' : 4, # experience gained from victory against. exp used to increase character level
        'gold_drop' : 5, # max amount they drop... maybe random between 1 and 5 isn't very generous, but im sure ill come up with some maths to make it random without being between 1 to this stat
        'enc_mult' : 25, # a 50% chance to encounter more than 1. May not use until way later
        'damage' : 2, # basic damage amount for combat
        'dice' : 2 # dice for randomness
    },
    'goblin' : {
        'solo' : 'a goblin',
        'many' : 'a group of goblins',
        'health' : 20, 
        'base_lvl' : 2, 
        'exp_gain' : 8, 
        'gold_drop' : 20, 
        'enc_mult' : 25,
        'damage' : 4,
        'dice' : 2
    },
    'zombie' : {
        'solo' : 'a zombie',
        'many' : 'a band of zombies',
        'health' : 60, 
        'base_lvl' : 5, 
        'exp_gain' : 20, 
        'gold_drop' : 50, 
        'enc_mult' : 15,
        'damage' : 5,
        'dice' : 4
    },
    'bandit' : {
        'solo' : 'a bandit',
        'many' : 'a couple of bandits',
        'health' : 40, 
        'base_lvl' : 3, 
        'exp_gain' : 12, 
        'gold_drop' : 35, 
        'enc_mult' : 15,
        'damage' : 3,
        'dice' : 5
    },
    'boss' : {
        'solo' : 'Big Bad Lachlan',
        'many' : 'Big Bad Lachlan',
        'health' : 200,
        'base_lvl' : 10,
        'exp_gain' : 200,
        'gold_drop' : 0,
        'enc_mult' : 0,
        'damage' : 20,
        'dice' : 1
    }
}
# FOR REFERENCE (#,#,#) = damage, dice, price
swords = {
    'Wooden Sword' : (1,2,0), # a basic integer. Cant decide if 1d5 type stat would be more interesting 
    'Stone Sword' : (2,2,20),
    'Iron Blade' : (4,2,50), # and so on
    'Mithril Daggers' : (5,3,100),
    'God Sword' : (6,3,200)
}
hero = {
    'name' : 'unknown', #change to some user_input later
    'maxhealth' : 100, # need a max to show how much you COULD have if youre missing HP
    'currenthealth' : 100, # the current amount of health our hero has
    'strength' : 1, # an int (same as above, to increase combat prowess)
    'sword' : 'Wooden Sword',
    'potions' : 0, # an integer 
    'gold' : 0,
    'experience' : 0,
    'level' : 1,
    'xp2level' : [0, 10, 20, 40, 80, 160, 320],
    'map_progress' : 0,
    'map_goal' : 10, #placeholder for the map progress
    'swords_dict' : swords,
    'enemy_dict' : enemy #WTH, did not expect this to work
}


def main():
    valid_input_main = ['1','2','3','4','gimme gold']
    def consume_potion():
        if hero['potions'] > 0:
            print("\nGlug, Glug! Ahhhh, feels better!")
            print("25 hit points restored")
            hero['currenthealth'] += 25
            hero['potions'] -= 1
            if hero['currenthealth'] > hero['maxhealth']: hero['currenthealth'] = hero['maxhealth']
        else: print("You have no Potions to consume.")

    def is_valid_main(user_input):
        if user_input in valid_input_main: return True
        else: return False
            
    
    main_menu = """- - Map Menu - -
1 - Progress forward 
2 - Return to the Inn
3 - View Stats
4 - Consume Potion (25HP)"""

    print("You are about to embark on a rather short, linear journey! Prepare yourself hero, for the way is guarded by monsters.")
    print("Your quest: to reach the other side of the map! Fight monsters, upgrade your equipment, level up and stay alive!")
    print("\nAs you progress, you will encounter monsters that will take your 'H'it 'P'oints.")
    print("You can REST at the INN to restore that HP, but your progress on the map will be reset")
    print("If you die, your will wake up at the INN, lose half your GOLD and all EXPERIENCE for your current level - beware")
    print("\nWhat should we call you, hero?")
    user_input = input(": ")
    hero['name'] = user_input
    print(display_stats(hero))
    
    
    while True:
        print(art_list[hero['map_progress']])
        print(main_menu)
        user_input = input(": ")
        if is_valid_main(user_input):
            if user_input == '1': progress_forward(hero)
            if user_input == '2': 
                print("\nTraveling back to the Inn!")
                inn(hero)
            if user_input == '3': print(display_stats(hero))
            if user_input == '4': consume_potion()
            if user_input == 'gimme gold': hero['gold'] += 200
        else:
            print("Invalid response, try again.")

main()
