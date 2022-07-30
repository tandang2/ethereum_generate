'''
depends on module: "eth-account"
installation: 
python -m pip install eth-account
'''

# import
from ast import Import
from cmath import exp
from eth_account import Account
from os import urandom
from urllib.request import urlopen
from json import load
from argparse import ArgumentParser
from time import sleep

# functions
def generate_acc():
    global acc
    acc = Account.create(urandom(256))
    return acc

def generate_list(times):
    global public_string
    global public_list
    global private_string
    global private_list
    public_list = []
    private_list = []
    for i in range(times):
        account = generate_acc()
        public_list.append(account.address)
        private_list.append(account.privateKey.hex())
    public_string = ",".join(public_list)
    private_string = ",".join(private_list)
    return public_string

def gen_output(num):
    stringlist = generate_list(num)
    if args.balance:
        balances = get_balance(stringlist)
    if args.quiet:
        if args.balance:
            i = 0
            while i < len(private_list):
                print(private_list[i], public_list[i], balances[i])
                i += 1
        else:
            j = 0
            while j < len(private_list):
                print(private_list[j], public_list[j])
                j += 1
    elif args.quietbalance:
        l = 0
        balances = get_balance(stringlist)
        while l < len(private_list):
                if balances[l] > 0:
                    print(private_list[l], public_list[l], balances[l])
                l += 1
    else:
        k = 0
        while k < len(private_list):
            print(f"\nPrivate Key: {private_list[k]}\nAdress: {public_list[k]}")
            if args.balance:
                print(f"Balance: {balances[k]} ETH")
            k += 1


def get_balance(addresses):
    try:
        global balance_list
        call = urlopen(f"https://api.etherscan.io/api?module=account&action=balancemulti&address={str(addresses)}&tag=latest&apikey={str(key)}")
        balance_list = []
        for j in load(call)["result"]:
            balance_list.append(int(j["balance"]))
        return balance_list
    except:
        print("\n\nCould not Access Etherscan.io API, or it gave an unusual response. Please check if your API key is entered correctly, or if the API might be currently unavailible.")
        quit()

def check_api_key():
    global key
    file = open("api_key.ini", "r")
    key = file.readline()
    file.close()
    if key != "":
        return key
    else:
        return False


if __name__ == "__main__":
# argparse
    parser = ArgumentParser(description="A tool to generate valid Ethereum Wallets. Please optain an API Key on Etherscan.io and paste into api_key.ini", prog="Ethereum Wallet Generator")
    parser.add_argument("-b", "--balance", help="If specified, checks the balance of each generated wallet. | SLOWS DOWN", action="store_true")

    gen_wallet = parser.add_mutually_exclusive_group()
    gen_wallet.add_argument("-gen", "--generateWallets", metavar="NUMBER", help="generates a given number of wallets with private and public key", type=int)
    gen_wallet.add_argument("-geninf", "--generateInfinite", help="generates random wallets forever | -q recommended | CTRL + C to stop", action="store_true")

    outprint = parser.add_mutually_exclusive_group()
    outprint.add_argument("-q", "--quiet", help="prints only nessesary output | PRIVATEKEY PUBLICKEY [BALANCE]", action="store_true")
    outprint.add_argument("-qb", "--quietbalance", help="prints only when balance is > 0 | forces -b activation | PRIVATEKEY PUBLICKEY BALANCE", action="store_true")
    
    args = parser.parse_args()
    
# code
global key
file = open("api_key.ini", "r")
key = file.readline()
file.close()
if key == "":
    print("\n\n KEY NOT FOUND. Please enter your Etherscan.io API key into api_key.ini")
    quit()

if args.generateInfinite:
    while True:
        gen_output(20)

if args.generateWallets != None and args.generateWallets > 0:
    for wallet in range(int(args.generateWallets)):
        gen_output(20)

if not any(vars(args).values()):
    gen_output(1)
