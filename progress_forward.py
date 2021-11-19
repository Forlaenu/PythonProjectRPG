from combat import combat_encounter
from random import choice
def progress_forward(hero):
    #some code to move the character to the next encounter
    # increase map_progress by 1
    # LOGIC FOR ENCOUNTERS SHOULD GO HERE
    # Events (treasure, trap, rest etc) or COMBAT
    # Eventually combat can get harder the more the map progresses 
    print("\nYou progress forward on your journey... \n")

    hero['map_progress'] += 1
    progress_current = hero['map_progress']
    progress_goal = hero['map_goal']

    enemy_dict = hero['enemy_dict']

    def encounter():
        # this will be a playground for adding randomness to the outcome of progressing forward
        # for now, combat
        if progress_current < 10:
            enemy = get_enemy()
            print("\nQueue that combat music!\n")
            combat_encounter(hero, enemy)
            #DEBUG
            print(f"\n\nYou survived! Only {progress_goal - progress_current} more encounters to go!")
        #boss battle?
        elif progress_current == 10:
            print("\nOne last challenge remains!")
            enemy = 'boss'
            combat_encounter(hero, enemy)
        elif progress_current > 10:
            print("\n\n\n\nCONGRATULATIONS! YOU HAVE BEAT THE GAME!\n\n\n\n")
            exit()

    # turns enemy dictionary into a list of enemy names, then chooses one at random... for random's sake
    def get_enemy():
        temp_list = []
        for key in enemy_dict.keys():
            if key == 'boss': pass
            if enemy_dict[key]['base_lvl'] > hero['level']: pass
            else: temp_list.append(key)
        #hero_level = hero['level']
        return choice(temp_list)
        enemy_level = enemy_dict[random_enemy]['base_lvl']
        #DEBUG
        # if enemy_level > hero_level:
        #     #try again
        #     get_enemy()
        # else:
        #     return random_enemy

    #Basic call when progress_forward is called from main    
    encounter()