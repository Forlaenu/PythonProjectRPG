from inn import inn
def death(hero):
    #!CREATE a function for returning to inn, resetting progress, dropping gold and hp
    print("\n\nYou wake up in the Inn.")
    print("Your coin purse feels lighter, and your memories of battle fade")
    # halve hero gold
    hero['gold'] = int(hero['gold'] / 2)
    # drop all experience
    hero['experience'] = 0
    #reset map progress
    hero['map_progress'] = 0
    #RESET HERO HEALTH
    hero['currenthealth'] = hero['maxhealth']
    inn(hero)