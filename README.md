# Ohjelmistotekniikka, kevät 2021

![](https://github.com/RadicalOyster/ot-harjoitustyo/blob/master/images/interface_2.png)

# Faux Emblem
This project is a simple turn based strategy game inspired by [Fire Emblem](https://en.wikipedia.org/wiki/Fire_Emblem:_Shadow_Dragon_and_the_Blade_of_Light). See links below for documentation.

# Links

[Project specifications](https://github.com/RadicalOyster/ot-harjoitustyo/blob/master/documentation/project%20specifications.md)

[User guide](https://github.com/RadicalOyster/ot-harjoitustyo/blob/master/documentation/user%20guide.md)

[Timekeeping](https://github.com/RadicalOyster/ot-harjoitustyo/blob/master/documentation/time%20spent.md)

[Project architecture](https://github.com/RadicalOyster/ot-harjoitustyo/blob/master/documentation/arkkitehtuuri.md)

## Releases
* [Release 1](https://github.com/RadicalOyster/ot-harjoitustyo/releases/tag/viikko5)
* [Release 2](https://github.com/RadicalOyster/ot-harjoitustyo/releases/tag/viikko6)
* [Final release]()

## Compatibility

This project has been developed using python 3.8.0. Running the project with an older version of Python may cause issues.

# Installation

1. Install dependencies

In the root directory of the project run the following command:

```bash
poetry install
```

2. Run the project

After installing depencies with poetry, run the project with the command:

```bash
poetry run invoke start
```

# Testing

To run automatic tests, use the command:

```bash
poetry run invoke test
```

## Test coverage report

To generate a coverage report for the automatic tests run the command:

```bash
poetry run invoke coverage-report
```

## Pylint

To run pylint on the project run the command:

```bash
poetry run invoke lint
```