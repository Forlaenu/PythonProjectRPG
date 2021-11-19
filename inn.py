from display_stats import display_stats
"""
    The Inn is like home. It brings us back to the beginning of our map, but allows us to restore health and upgrade/shop

"""

inn_menu = """1 - Rest
\tResting restores your health to max, but resets encounters
2 - Shop
\tThe shop allows you to upgrade your swords and buy potions
3 - View stats
\tSee your current level, health, strength and sword
4 - Leave the Inn"""

valid_input = ['1','2','3','4']

def inn(hero):
    swords = hero['swords_dict']
    def is_valid_inn(user_input):
        if user_input in valid_input:
            return True
        else:
            return False
    def rest(): 
        print("\nResting for the night.")
        hero['currenthealth'] = hero['maxhealth']
        hero['map_progress'] = 0

    def shop():
        print("\n- - Welcome to the shop - -")
        while True:
            # some code for displaying a shop list... 
            #!STATIC
            print("1 - Potion (25HP) - 50g")
            count = 2
            temp_list = [None, None,]
            for key,value in swords.items():
                sword_cost_stat = 2
                print(f"{count} - {key} - {value[sword_cost_stat]}g")
                temp_list.append(key)
                count += 1
            print("q - Leave the Shop")
            print(f"You currently have {hero['gold']}g, and {hero['sword']}")
            user_input = input(": ")
            if user_input == '1':
                print("You bought a Potion for 50g")
                #check they have the gold
                if hero['gold'] >= 50:
                    hero['potions'] += 1
                    hero['gold'] -= 50
                #otherwise no sale
                else:
                    print("You cannot afford that!\n")
            if user_input == 'q':
                print(f"Thank you for stopping by, {hero['name']}")
                break
            if int(user_input) >=2 and int(user_input) <= len(temp_list):
                weapon_name = temp_list[(int(user_input))]
                weapon_cost = swords[weapon_name][sword_cost_stat]
                print(f"\n{weapon_name} will cost you {weapon_cost}g")
                if hero['gold'] >= weapon_cost:
                    hero['sword'] = weapon_name
                    hero['gold'] -= weapon_cost
                else:
                    print("You cannot afford that!")
            #this may be a poor solution
            # result should look like:
            # 1 - Potion (25HP) - 30g
            # 2 - Wooden Sword - 0g
            # 3 - Stone Sword - 20g
            # 4 - Iron Blade - 50g
            # hero['gold'] -= sword_value

    user_input = 0
    while user_input != 4:
        print("\n- - WELCOME TO THE INN - -")
        print(inn_menu)
        user_input = input(": ")
        if is_valid_inn(user_input):
            if user_input == '1':
                rest()
            if user_input == '2':
                shop()
            if user_input == '3':
                print(display_stats(hero))
            if user_input == '4':
                print("\nSee you next time!")
                break
        else:
            print("Invalid response, try again.")
