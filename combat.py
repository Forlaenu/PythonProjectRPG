from random import choice, randint
from display_stats import display_stats
from update_stats import update_stats
from hero_died import death

valid_input = ['1','2','3']
def combat_encounter(hero, enemy):
    #passed 3 dictionaries since combat references each
    enemy_dict = hero['enemy_dict']
    swords = hero['swords_dict']
    #This validates the user input, plain and simple
    def is_valid_combat(user_input):
        if user_input in valid_input:
            return True
        else:
            return False
    # calculates the damage numbers used in combat, and changes per call which is cool
    def attackDMG(dmg, dice):
        damage = 0
        for i in range(dice):
            damage += randint(1,dmg)
        return damage

    # !STATIC
    #this helps me keep track of the indices of the values (tuples) inside swords dictionary
    sword_stat_damage = 0
    #this helps me keep track of the indices of the values (tuples) inside swords dictionary
    sword_stat_dice = 1
    # for calculating hero's damage in combat
    current_sword = hero.get('sword')
    sword_damage = swords[current_sword][sword_stat_damage] + hero['strength']
    sword_dice = swords[current_sword][sword_stat_dice]
    
    # Setting up all the variables for combat. means i don't have to reference the dictionary
    e_hp = enemy_dict[enemy]['health']
    e_base_lvl = enemy_dict[enemy]['base_lvl']
    e_base_exp = enemy_dict[enemy]['exp_gain']
    e_gold_drop = enemy_dict[enemy]['gold_drop']
    e_enc_mult = enemy_dict[enemy]['enc_mult']
    e_dmg = enemy_dict[enemy]['damage']
    e_dmg_dice = enemy_dict[enemy]['dice']
    e_name = enemy_dict[enemy]['solo']
    e_enc_hp = e_hp

    in_combat = True
    while in_combat:
        combat_display = f"""\n- - Combat Encounter - - 
Hero: {hero['name']}\tEnemy: {e_name}
HP: {hero['maxhealth']}/{hero['currenthealth']}\tHP:{e_hp}/{e_enc_hp}

1 - Attack
2 - Escape
3 - View Stats"""
        #Display some info to console:
        print(combat_display)
        user_input = input(": ")
        if is_valid_combat(user_input):
            #ATTACK SCRIPT
            if user_input == '1':
                # enemy hits, hero hits
                #calculate damage
                enemy_hit = attackDMG(dmg=e_dmg,dice=e_dmg_dice)
                hero_hit = attackDMG(dmg=sword_damage,dice=sword_dice)
                #print enemy hit
                print(f"{e_name} hits you for {enemy_hit} damage. ({e_dmg_dice}d{e_dmg})")
                # reduce hero health
                hero['currenthealth'] = hero['currenthealth'] - enemy_hit
                #check if hit killed hero
                if hero['currenthealth'] <= 0:
                    print(f"\n\n{hero['name']} has died at the hands of {e_name}.")
                    user_input_temp = input("\nHit enter to continue\n")
                    death(hero)
                    #end combat
                    in_combat = False
                    break
                #otherwise continue combat
                else:
                    #print hero hit
                    print(f"You hit {e_name} for {hero_hit} damage. ({sword_dice}d{sword_damage})")
                    # reduce enemy health
                    e_enc_hp = e_enc_hp - hero_hit
                    #check if hit killed enemy
                    if e_enc_hp <= 0:
                        #!CREATE a combat win function to display and update stats
                        print(f"\n{e_name} has been slain.")
                        print(f"{e_base_exp} XP gained!")
                        print(f"Your loot is worth {e_gold_drop} gold.\n")
                        # update stats
                        update_stats(hero, e_gold_drop, e_base_exp)
                        #end combat
                        in_combat = False
                        break
                #ESCAPE SCRIPT                
            if user_input == '2':
                print("Escaping combat - Function not in game yet")
            if user_input == '3':
                print(display_stats(hero))
        else:
            print("Invalid response, try again.")