## Package diagram
![](https://github.com/RadicalOyster/ot-harjoitustyo/blob/master/images/pakkauskaavio.png)

The project consists of 3 packages: entities, logic and ui.
* Entities contains objects tied to the core functionality of the game such as levels, units and items.
* Logic is for computational tasks. It contains classes for pathfinding, artifical intelligence and combat resolution.
* Ui contains classes that explicitly deal with graphics.

## Sequence diagrams of core functionality
Below is an example of a (somewhat simplified) sequence diagram of selecting the 'Attack' command from the character menu. The main game loop needs to pass on values from various entities such as the camera and the cursor to the TargetSelector and so arguments have been simplified for some calls to maintain readability.
![](https://github.com/RadicalOyster/ot-harjoitustyo/blob/master/images/sequence%20diagram%20(select%20attack).png)
