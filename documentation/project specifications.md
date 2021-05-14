# Project Specifications

## Purpose of the application

This is a simple grid-based strategy game in the vein of [Fire Emblem](https://en.wikipedia.org/wiki/Fire_Emblem:_Shadow_Dragon_and_the_Blade_of_Light). The player takes turns with the AI to guide their units in battle against the opposing army. Currently, the basics of gameplay have all been implemented. The player can move their units around using the in-game cursor, engage in combat with enemy units and use restorative
items to keep their army healthy. The AI in its current form is very basic, simply moving around randomly on the map if no player units are in reach or attacking a random player unit if one is in range.

## Users

Being a simple single player game with no login capabilities or private user data, the application has no need for different user roles.

## Basic functionality

* Cursor movement and unit selection
* Allied units under the player's control and enemy units
* Units with individual stats
* Basic combat (units can engage in battle and disappear from the map if their hit points drop to 0)
* Pathfinding and display for units' movement- and attack ranges (utilizes Dijkstra's algorithm)
* Terrain with varying movement costs
* Scrolling camera
* UI elements to allow the player to inspect a unit's attributes in detail
* Basic unit inventory system
* Basic AI to control enemy actions

## Features for future development

After basic functionality has been implemented, work will begin on the following features if time allows it:
* Equipment system allowing units to swap between different types of weapons
* Varying terrain movement cost depending on unit type (eg. cavalry might sufffer a movement penalty moving through marsh land while infarnty can move unimpeded)
* Experience and level up system to allow characters to grow
* Loading game data such as levels and items from external files
* Transitioning between multiple levels
* Saving game progress
* Add an .env file to toggle features such the debug display

## Other improvements

Before working on new features, the current project is in need of code clean up.

* The main game loop is rather messy and overdue for a major overhaul to maintain readability
 * The parsing of user input could be isolated into its own class to clean up the the game loop
* Class dependencies are somewhat muddled and should undergo some major refactoring to help with readability and maintainability