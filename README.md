# Ethereum Wallet Generator
> DISCLAIMER: Do NOT use this to do anything illegal (like theft), and if you do so, please don't make me responsible. This is for educational purposes only!

The Ethereum Wallet Generator is a little tool that can generate random ETH wallets and even check their balance. It achieves this, by generating a random private key, and calculating the corresponding public address. 
> Fun fact: There are 2²⁵⁶ different possible combinations! (SHA-256)

## Installation
1. Make sure to install [Python](https://www.python.org/downloads/).
2. Open your console and type: `python -m pip install eth-account`
3. Download the code and extract the `.zip` file anywhere you want. 
> You're done!

## Usage
Just open a new console in the same directory as the installed files.
After typing `main.py --help`, you can see all commands you can use instead of `--help`.

 The following help message will appear:
```
ethereum_wallet_generator>main.py --help
usage: Ethereum Wallet Generator [-h] [-b] [-gen NUMBER | -geninf] [-q | -qb]

A tool to generate valid Ethereum Wallets

optional arguments:
  -h, --help            show this help message and exit
  -b, --balance         If specified, checks the balance of each generated wallet. | SLOWS DOWN A LOT
  -gen NUMBER, --generateWallets NUMBER
                        generates a given number of wallets with private and public key
  -geninf, --generateInfinite
                        generates random wallets forever | -q recommended | CTRL + C to stop
  -q, --quiet           prints only the output | -qq -qqq -qqqq for even less output
  -qb, --quietbalance   only prints ETH Adresses with balance > 0 | propably won't find anything | useful for output
                        to file
```
> Those `[]` in the first line indicate `mutually exclusive groups`. Basically, you can only use one argument per group at the time. For example, you could either use `-q` or `-qb`, but not both at the same time.

### Commands

```
Syntax: -gen NUMBER | --generateWallets NUMBER
Usage: main.py -gen 4

It will simply output the given number of random ETH wallets. 
```
```
Syntax: -geninf | --generateInfinite
Usage: main.py -geninf

Never stops generating ranom wallets. To stop, use CTRL + C.
```
```
Syntax: -b | --balance
Usage: main.py -gen 1 -b

Generates a random wallet and checks its balance using the etherscan.io API. 

WARNING: This will drastically reduce generation speed, due to the limitation of Etherscan. 
Without using an API key it is limited to 1 request per 5 seconds. 
With a valid API key in api_key.ini, it is limited to 5 requests per second.
```
```
Syntax: -q / -qq / -qqq / -qqqq
Usage: main.py -gen 1 -b -q

-q: reduces output to: PRIVATEKEY ADDRESS [BALANCE(if -b)]
-qq: reduces output to: PRIVATEKEY
-qqq: reduces output to: ADDRESS
-qqqq: reduces output to: BALANCE (even if -b is NOT given)
```
```
Syntax: -qb | --quietbalance
Usage: main.py -gen 1 -qb

Special variation of: -q
Only prints an output, if the balance is > 0.
Due to the low chance of generating a wallet which is actually in use, it will propably never output anything. 

Pro tip: main.py -geninf -qb > out.txt
```
