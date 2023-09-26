# Markov Username Generator

This project uses a pre-trained Markov chain model to generate realistic usernames. The training set consisted of
username lists provided by [SecLists](https://github.com/danielmiessler/SecLists/tree/master/Usernames).

## Installation

```bash
pipx install git+https://github.com/karrni/username-generator
```

## Usage

To generate a username simply run:

```bash
usergen
```

You can also generate multiple usernames and change their length:

```bash
usergen --num 5 --length 10
```
