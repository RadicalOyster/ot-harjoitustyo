def ReturnAttackOrder(attacker, defender):
    """Returns the order in which two units attack in combat

    Args:
        attacker: The unit initiating combat.
        defender: The unit defending in combat.
    """
    attack_order = []

    attack_order.append((attacker, defender))
    attack_order.append((defender, attacker))

    if (attacker.speed >= defender.speed + 4):
        attack_order.append((attacker, defender))
    elif (defender.speed >= attacker.speed + 4):
        attack_order.append((defender, attacker))

    return attack_order


def Combat(attacker, defender):
    """A method for resolving combat between two units.

    Args:
        attacker: The unit initiating combat.
        defender: The unit defending in combat.
    """
    attack_order = ReturnAttackOrder(attacker, defender)
    for combatants in attack_order:
        current_attacker = combatants[0]
        current_defender = combatants[1]
        total_damage = current_attacker.strength + \
            current_attacker.might - current_defender.defense
        current_defender.update_hp(total_damage)

        print(current_defender.name, " took ", total_damage,
              " damage, hp remaining: ", current_defender.current_hp)
        if current_defender.dead:
            print(current_defender.name, " has died, ending combat")
            return current_defender
    return None