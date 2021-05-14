# User Guide

## User interface and the basics of gameplay

The core gameplay takes place on a map represented by a 2-dimensional grid as seen in the screenshot below. The player interacts with the game through a cursor that moves along the grid with the arrow keys on the keyboard. Friendly units are color coded in blue and enemy units in red.

The Z and X key respectively are used to confirm or cancel actions.

<img src="https://github.com/RadicalOyster/ot-harjoitustyo/blob/master/images/interface_1.png">

While the cursor is hovering over a unit, statistics about that unit such as its hit points are displayed. Additionally, if the cursor is hovering over an ally unit, the Z key will display the tiles that unit can reach in green and tiles beyond its movement range that it can reach with its attack in red as seen below.

<img src="https://github.com/RadicalOyster/ot-harjoitustyo/blob/master/images/interface_2.png">

In this state, moving the cursor to any of the tiles highlighted in blue will display the path to that tile and pressing the Z key will move the unit to the selected tile. Whether the unit moved or not, the Z key will bring up a menu from which the player can choose the unit's next action.

<img src="https://github.com/RadicalOyster/ot-harjoitustyo/blob/master/images/interface_3.png">

The up and down arrow keys will scroll through the menu and the Z button will confirm selection. The wait option will simply deactivate the unit until the end of the turn after which the player can move it again. An inactive unit turns gray to indicate that it has already taken its action.

The items option will allow the unit to manage its inventory and use items, such as potions to restore health.

The attack option will display tiles within the unit's attack range in red and allow the player to cycle through enemy units in reach, and the Z key will confirm the player's selection and commence battle.

<img src="https://github.com/RadicalOyster/ot-harjoitustyo/blob/master/images/interface_4.png">

In combat, the units will take turns to attack each other with the initiating unit having intiative and getting the first blow. The resulting damage from attacks is calculated based on each unit's individual attributes and speedier units may be able to strike twice.

<img src="https://github.com/RadicalOyster/ot-harjoitustyo/blob/master/images/interface_5.png">

After combat, both units' health will be updated and dead units removed from the map. The selected unit will also become inactive as it has taken its action for the turn.

<img src="https://github.com/RadicalOyster/ot-harjoitustyo/blob/master/images/interface_6.png">

The item menu lets you browse a unit's inventory and activate items such as potions that can restore a unit's hit points. This will also deactivate the unit.
Items have limited uses which are displayed next to the item's name in the item menu.

<img src="https://github.com/RadicalOyster/ot-harjoitustyo/blob/master/images/interface_7.png">

Maps can span distances greater than what the game window can display. Moving your cursor towards the screen boundary will scroll the map to give you
a better view of the battlefield.

<img src="https://github.com/RadicalOyster/ot-harjoitustyo/blob/master/images/interface_8.png">

## Ending your turn

Whether all your units have acted or not, when you wish to end your turn, pressing the C key will begin the enemy phase during which the AI takes control
of enemy units to move around the map or attack your units.

## A note on movement

As seen in the image below, player units cannot move through enemy units, but ally units do not hinder your unit's movement although two units still cannot
occupy the same space. This applies for enemy units as well, who may move freely through other enemy units while player units will impede their movement.

<img src="https://github.com/RadicalOyster/ot-harjoitustyo/blob/master/images/interface_9.png">