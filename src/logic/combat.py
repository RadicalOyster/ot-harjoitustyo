"""
A module containing functions relating to combat.
"""
def _return_attack_order(attacker, defender):
    """
    Returns the order in which two units attack in combat

    Args:
        attacker: The unit initiating combat.
        defender: The unit defending in combat.
    Returns:
        A list of units ordered by the order they will attack
    """
    attack_order = []

    attack_order.append((attacker, defender))
    attack_order.append((defender, attacker))

    if attacker.speed >= defender.speed + 4:
        attack_order.append((attacker, defender))
    elif defender.speed >= attacker.speed + 4:
        attack_order.append((defender, attacker))

    return attack_order


def combat(attacker, defender):
    """
    A method for resolving combat between two units.

    Args:
        attacker: The unit initiating combat.
        defender: The unit defending in combat.
    Returns:
        If either unit's HP is reduced to 0, returns that unit. Else, returns None.
    """
    attack_order = _return_attack_order(attacker, defender)
    for combatants in attack_order:
        current_attacker = combatants[0]
        current_defender = combatants[1]
        total_damage = current_attacker.strength + \
            current_attacker.might - current_defender.defense
        if total_damage < 0:
            total_damage = 0
        current_defender.update_hp(total_damage)

        print(current_defender.name, " took ", total_damage,
              " damage, hp remaining: ", current_defender.current_hp)
        if current_defender.dead:
            print(current_defender.name, " has died, ending combat")
            return current_defender
    return None
