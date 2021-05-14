# Testing document
The game has been tested with automatic unit testing as well as extensive manual testing to ensure that everything functions correctly.

# Unit Testing

Automatic tests have been written for most classes in the logic and entities packages. Many of these tests involve the integration of multiple different classes. Manual testing was mostly performed on Windows 10,
though some testing has been performed on Linux as well.

## Test Coverage

Excluding ui elements and the main game loop, which would be cumbersome to test automatically and primarily relies on components that have been individually tested, the automated unit tests cover 77% of branches.

<img src="">

## Installation

Fresh installation has been tested on both Windows 10 and on Linux machines.

## Functionality

All functionality outlined in the project specifications has been tested and deemed to function according to specifications. All known crashes have been fixed.

## Bugs

There is a bug while having a unit selected for movement and hovering the cursor over an enemy unit where the information display turns red to indicate that
the information displayed is for an enemy unit, but the displayed information is that of the player unit. This is purely visual and does not cause any issues
in terms of functionality.