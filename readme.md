# CLC

### ADP 2021/2022 final project

## Members

Ada Hryniewicka, Maciej Dzikowski

## Description

The main goal of the project is adding two new features to [click](https://click.palletsprojects.com/en/8.1.x/) library.

#### New features:
- `help` parameter for `@click.argument` decorator to preserve an UI consistency,
- second, not required parameter for `@click.argument` decorator to give a possibility of creating a Python argument differed from an argument name displayed in a help message.
  - Allows to avoid shadowing built-in names, e.g. when argument has to be named "filter".

## Code links:
- [branch: CLC1](https://github.com/MaciejDzikowski/click/tree/CLC1)
- [branch: CLC2](https://github.com/MaciejDzikowski/click/tree/CLC2)
