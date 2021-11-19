def update_stats(hero, delta_gold, delta_experience):
    xp2level = hero['xp2level']
    hero['gold'] += delta_gold
    hero['experience'] += delta_experience
    # if hero levels up
    level = hero['level']
    if hero['experience'] > xp2level[level]:
        print(f"DING! Congratulations on reaching level {level+1}!")
        print("Max health and strength increased!\n")
        #we should increase level, health and strength, modulus the experience to bring it back to zero + remainder
        hero['maxhealth'] += 20
        hero['currenthealth'] += 15
        hero['strength'] += 1
        hero['level'] += 1
        hero['experience'] = hero['experience'] % xp2level[level]