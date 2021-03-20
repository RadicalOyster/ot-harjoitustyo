import pygame
from cursor import Cursor, CursorState
from movement_display import MovementDisplay
from sprite_renderer import SpriteRenderer
from menu_cursor import MenuCursor, CharMenuCommands
from unit import Unit, Alignment
import os
from game_loop import GameLoop
from event_queue import EventQueue

def ReturnAttackOrder(attacker, defender):
    attack_order = []
    
    attack_order.append((attacker, defender))
    attack_order.append((defender, attacker))

    if (attacker.speed >= defender.speed + 4):
        attack_order.append((attacker, defender))
    elif (defender.speed >= attacker.speed + 4):
        attacker.append((defender, attacker))
    
    return attack_order
    
    #for combatants in attack_order:
        #current_attacker = combatants[0]
        #current_defender = combatants[1]
        #total_damage = current_attacker.strength + current_attacker.might - current_defender.defense
        #current_defender.current_hp -= total_damage

        #print(current_defender.name, " took ", total_damage, " damage, hp remaining: ", current_defender.current_hp)
        #if current_defender.current_hp < 0:
            #current_defender.dead = True
            #print(current_defender.name, " has died, ending combat")
            #break

dirname = os.path.dirname(__file__)

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 640
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Faux Emblem")

units = []
units.append(Unit(1,1,name="Ferdinand", strength=8, speed=6, defense=5))
units.append(Unit(5,3,Alignment.ENEMY))

combat_order = ReturnAttackOrder(units[0], units[1])
#print(combat_order)

pygame.font.init()
font = pygame.font.SysFont("Arial", 20)

game_loop = GameLoop(screen, SpriteRenderer(), Cursor(), MenuCursor(), EventQueue(), units, MovementDisplay(), font)

pygame.init()
game_loop.start()

pygame.quit()