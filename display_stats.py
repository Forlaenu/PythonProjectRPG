def display_stats(hero):
    return f"""\n\n\n\n\n\n\n- - {hero['name']} - - 
LVL: {hero['level']} (EXP: {hero['experience']}/{hero['xp2level'][hero['level']]})
HP: {hero['currenthealth']} / {hero['maxhealth']}
Strength: {hero['strength']}
Sword: {hero['sword']}
Gold: {hero['gold']}
Potions: {hero['potions']}
Map Progress: {hero['map_progress']}\n"""