def ReturnAttackOrder(attacker, defender):
    attack_order = []
    
    attack_order.append((attacker, defender))
    attack_order.append((defender, attacker))

    if (attacker.speed >= defender.speed + 4):
        attack_order.append((attacker, defender))
    elif (defender.speed >= attacker.speed + 4):
        attacker.append((defender, attacker))
    
    return attack_order

def Combat(attacker, defender):
    attack_order = ReturnAttackOrder(attacker, defender)
    for combatants in attack_order:
        current_attacker = combatants[0]
        current_defender = combatants[1]
        total_damage = current_attacker.strength + current_attacker.might - current_defender.defense
        current_defender.updateHP(total_damage)

        print(current_defender.name, " took ", total_damage, " damage, hp remaining: ", current_defender.current_hp)
        if current_defender.dead:
            print(current_defender.name, " has died, ending combat")
            return current_defender
    return None