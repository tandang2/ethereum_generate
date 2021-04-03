'''
depends on module: "eth-account"
install: pip install eth-account
'''

# import
from eth_account import Account
from os import urandom as rand
import argparse

# variables
loops = type=int

# functions
def generate_acc():
    global acc
    acc = Account.create(rand(256))
    return acc

def gen_output():
    generate_acc()
    if args.quiet == 1:
        print(acc.privateKey.hex(), acc.address)
    elif args.quiet == 2:
        print(acc.privateKey.hex())
    elif args.quiet >= 3:
        print(acc.address)
    #elif args.verbose >= 1:
    #    print(f"\nThe address is: {acc.address}")
    #    print(f"The private Key is: {acc.privateKey.hex()}")
    else:
        print(f"\nPrivate Key: {acc.privateKey.hex()}\nAdress: {acc.address}")


# argparse
parser = argparse.ArgumentParser(description="A tool to generate valid Ethereum Wallets", prog="Ethereum Wallet Generator")

gen_wallet = parser.add_mutually_exclusive_group()
gen_wallet.add_argument("-gen", "--generateWallets", metavar="NUMBER", help="Generate a number of wallets with private and public key", type=int)
gen_wallet.add_argument("-genone", "--generateOneWallet", help="Generate one random wallet with private and public key", action="store_true")

outprint = parser.add_mutually_exclusive_group()
outprint.add_argument("-q", "--quiet", help="prints only the output | -qq -qqq also possible", action="count", default=0)
#outprint.add_argument("-v", "--verbose", help="print additional information", action="count", default=0)

args = parser.parse_args()

# code
if args.generateWallets != None and args.generateWallets > 0:
    for wallet in range(int(args.generateWallets - 1)):
        gen_output()

# if opened directly
if __name__ == "__main__":
    if not any(vars(args).values()) or args.generateOneWallet or not args.quiet: #or not args.verbose:
        gen_output()
