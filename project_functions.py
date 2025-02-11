import datetime
from project_classes import User, Vault, Pot, Transaction
from time import sleep

def submit_transaction(x, pot):
    
    # Collect transaction name
    print()
    print_slow("Please provide a name reference for this transaction: ")
    transaction_name = input()
    print()

    # Collect pot id
    transaction_id = x

    # Collect date data and create date object
    print_slow("Excellent. Now we'll define when the transaction took place. Please note, all date input values must be in the format DD/MM/YY")
    print()
    print()

    date = collect_date("Date of transction: ")

    # Collect transaction type
    print()
    
    while True:
        types = ["in", "out"]
        print_slow('Please define the type of transaction. "in" or "out": ')
        type = input()
        if type not in types:
            print("incorrect transaction reference")
        else:
            break
    
    # Collect transaction amount
    print()
    print_slow("What is the transaction amount?: ")
    while True:
        amount = int_validator()
        if amount > 0:
            break
        else:
            print("amount must be greater than 0")
        
    if type == "out":
        amount = amount * -1
    else:
        pass

    #Input all information into the Class
    
    transaction = Transaction(transaction_id=transaction_id, transaction_name=transaction_name, date=date, pot=pot, type=type, amount=amount)
    
    if transaction:
        print_slow("Thanks, your transaction has been created succesfully")
        print()
    else:
        print_slow("ERROR: transaction not created succesfully")
    
    return transaction

def print_slow(txt):
    for x in txt: 
        print(x, end='', flush=True)
        sleep(0.025)

def int_validator():
    while True:
        try:
            value = int(input())
            print()
            break
        except ValueError:
            print_slow("Invalid input. Please enter a valid integer: ")
        
    return value

def collect_date(message):
    while True:
        print_slow(message)
        try:
            date_input = input()
            date = datetime.datetime.strptime(date_input,"%d/%m/%y")
            break 
        except ValueError as err:
            print(err)
    return date

def summary(vaults, pots):

    for i in vaults:
        print()
        print_slow(f"\033[31mVault\033[0m") 
        print()
        print_slow(f"{vaults[i].vault_name} = $")
        vault_value = vaults[i].vault_value()
        print_slow(f"{vault_value}")
        print()
        print_slow(f"\033[31mPots\033[0m") 
        print()
        for j in pots:
                if pots[j].vault == vaults[i]:
                    print_slow(f"{pots[j].pot_name} = ${pots[j].amount}")
                    print()
                else:
                    continue