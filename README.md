# Ohjelmistotekniikka, kevät 2021

![](https://github.com/RadicalOyster/ot-harjoitustyo/blob/master/screenshot.png)

# Generic strategy game
This project is a simple turn based strategy game in which units move across a grid to do battle in the style of [Fire Emblem](https://en.wikipedia.org/wiki/Fire_Emblem:_Shadow_Dragon_and_the_Blade_of_Light). More thorough documentation to come.

# Features
* Basic character movement including a pathfinding algorithm to navigate terrain (an implementation of [Dijkstra's algorithm](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm))
* Attack and movement range display, tiles highlighted in green show tiles unit can move to, red tiles show tiles unit can reach with its attack command
* Rudimentary menu system for selecting unit actions (only wait command has been implemented)

# Instructions
Currently the game only supports selecting a unit and moving it around.
The arrow keys are used to move around the cursor on the grid. While hovering the cursor over a unit, pressing the Z button on the keyboard will select the unit and highlight tiles that are within the unit's movement range. The X button will cancel this selection and hide the movement range display. While a unit is selected, pressing Z while the cursor is on a tile within the unit's movement range will move the unit to that tile.
For debugging purposes, the C button will make inactive units active.

# To do
* Implement enemy units and basic combat
* Simple ai
* (Possibly) a scrolling camera to allow for bigger maps
* Clean up project structure and code, especially the main loop

# Links

[Timekeeping](https://github.com/RadicalOyster/ot-harjoitustyo/blob/master/documentation/time%20spent.mkd)

# Tehtävät

## Viikko 1

[gitlog.txt](https://github.com/RadicalOyster/ot-harjoitustyo/blob/master/laskarit/viikko1/gitlog.txt)

[komentorivi.txt](https://github.com/RadicalOyster/ot-harjoitustyo/blob/master/laskarit/viikko1/komentorivi.txt)

## Viikko 2
