# Ethereum Wallet Generator
> DISCLAIMER: Do NOT use this to do anything illegal (like stealing), and if you do so, please don't make me responsible. This is for educational purposes only!

The Ethereum Wallet Generator is a little tool that can generate random ETH wallets and  check their balance. It achieves this, by generating a random private key, and calculating the corresponding public address. 
> Fun fact: There are 2²⁵⁶ different possible combinations! (SHA-256)

## Changelog
[NEW] - API key is now nessecary. BUT it uses the API way more efficient and is (in theory) 20 times(!) faster than before

## Installation
1. Make sure to install [Python](https://www.python.org/downloads/).
2. Open your console and type: `python -m pip install eth-account`
3. Download the code and extract the `.zip` file anywhere you want.
4. Create an Account on Etherscan.io, get an API key and paste it into `api_key.ini`
> You're done!

## Usage
Just open a new console in the same directory as the installed files.
After typing `main.py --help`, you can see all commands you can use instead of `--help`.

 The following help message will appear:
```
ethereum_wallet_generator>main_new_new.py --help
usage: Ethereum Wallet Generator [-h] [-b] [-gen NUMBER | -geninf] [-q]

A tool to generate valid Ethereum Wallets. Please optain an API Key on Etherscan.io and paste into api_key.ini

optional arguments:
  -h, --help            show this help message and exit
  -b, --balance         If specified, checks the balance of each generated wallet. | SLOWS DOWN
  -gen NUMBER, --generateWallets NUMBER
                        generates a given number of wallets with private and public key
  -geninf, --generateInfinite
                        generates random wallets forever | -q recommended | CTRL + C to stop
  -q, --quiet           prints only nessesary output | PRIVATEKEY PUBLICKEY [BALANCE]
```

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

NOTES:
The maximum API requests per day are 100.000
This means you can look up around 2 Million Wallets per day.
```
```
Syntax: -q
Usage: main.py -gen 1 -b -q

-q: reduces output to: PRIVATEKEY ADDRESS BALANCE(if -b)
```
```
Syntax: -qb
Usage: main.py -gen 1 -qb

-qb: outputs when balance > 0: PRIVATEKEY ADDRESS BALANCE
```

### Other (propably better working, and faster) Tools
- [Bitcoin-Stealer by Michael2SAB](https://github.com/Michal2SAB/Bitcoin-Stealer)
- [Ethereum-Stealer by Michael2SAB](https://github.com/Michal2SAB/Ethereum-Stealer)
- [ByeBye-Bitcoin by cloutjs](https://github.com/cloutjs/ByeBye-Bitcoin)


```
Pro tip: main.py -geninf -qb > output.txt
```
