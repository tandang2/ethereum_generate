# import
from tkinter import *
import os

# code
root = Tk()
root.title("Ethereum Wallet Generator")
#root.geometry("600x300")

balance = StringVar()
genWallets = StringVar()
quiet = StringVar()


def run_program():
    global command
    command = f"main.py {balance.get()} {genWallets.get()} {genWalletsNumber.get()} {quiet.get()}"
    print(command)
    os.system(command)


#output = Entry(root, width=20)
#output.grid(row=4, column=0, columnspan=2)

heading = Label(root, text="Choose some commands and run the program").grid(row=0, column=0, columnspan=3)
fillertext = Label(root, text="< Enter number of generations").grid(row=2, column=2)

balanceButton = Checkbutton(root, text="check Balance", variable=balance, onvalue="-b", offvalue="")
balanceButton.grid(row=1, column=0)
balanceButton.deselect()

genWalletsButton = Checkbutton(root, text="generate wallets", variable=genWallets, onvalue="-gen", offvalue="")
genWalletsButton.grid(row=2, column=0)
genWalletsButton.deselect()

genWalletsNumber = Entry(root, width=10)
genWalletsNumber.grid(row=2, column=1)

quietButton = Checkbutton(root, text="less output", variable=quiet, onvalue="-q", offvalue="")
quietButton.grid(row=3, column=0)
quietButton.deselect()

run = Button(root, text="Run", command=run_program).grid(row=4, column=3)

root.mainloop()