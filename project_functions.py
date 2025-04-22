import datetime
from project_classes import User, Vault, Pot, Transaction
from time import sleep

def submit_transaction(x, pot):
    # Collect transaction name
    print_slow("\nPlease provide a name reference for this transaction: ")
    transaction_name = input()
    
    # Collect pot id
    transaction_id = x

    # Collect date data and create date object
    print_slow("\nExcellent. Now we'll define when the transaction took place. Please note, all date input values must be in the format DD/MM/YY")
    date = collect_date("Date of transction: ")

    # Collect transaction type
    while True:
        types = ["in", "out"]
        print_slow('\nPlease define the type of transaction. "in" or "out": ')
        type = input()
        if type not in types:
            print_slow("\nincorrect transaction reference")
        else:
            break
    
    # Collect transaction amount
    print_slow("\nWhat is the transaction amount?: ")
    while True:
        amount = int_validator()
        if amount > 0:
            break
        else:
            print_slow("\namount must be greater than 0")
        
    if type == "out":
        amount = amount * -1
    else:
        pass

    #Input all information into the Class
    transaction = Transaction(transaction_id=transaction_id, transaction_name=transaction_name, date=date, pot=pot, type=type, amount=amount)
    
    if transaction:
        print_slow("\nThanks, your transaction has been created succesfully")
    else:
        print_slow("\nERROR: transaction not created succesfully")
    
    return transaction

def print_slow(txt):
    for x in txt: 
        print(x, end='', flush=True)
        sleep(0.0)
    print("", end="\n\n")

def print_slow_nospace(txt):
    for x in txt: 
        print(x, end='', flush=True)
        sleep(0.0)
    print("", end="\n")

def int_validator():
    while True:
        try:
            value = int(input())
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
            print_slow(err)
    return date

def summary(vaults, pots):
    for i in vaults:
        print_slow_nospace(f"\033[31mVault\033[0m") 
        vault_value = vaults[i].vault_value()
        print_slow_nospace(f"{vaults[i].vault_name} = ${vault_value}")
        print_slow_nospace(f"\033[31mPots\033[0m") 
        
        for j in pots:
                if pots[j].vault == vaults[i]:
                    print_slow_nospace(f"{pots[j].pot_name} = ${pots[j].amount}")
                else:
                    continue

        print_slow("")

def create_user():
    print_slow("Now firstly, what is your name?: ")
    username = input()
    user = User(username)
    return user

def create_pot(x, vault):
    # Collect pot name
    print_slow("\nWhat is your preferred name for the pot?: ")
    pot_name = input()
    
    # Collect pot id
    pot_id = x

    # Collect start date data and create date object
    print_slow("\nExcellent. Now we'll define when the pot will be in use. Please note, all date input values must be in the format DD/MM/YY")
    start_date = collect_date("What is the start date that this pot will be active?: ")

    # Collect end date data and create date object
    end_date = collect_date("\nWhat is the end date that this pot will be active?: ")

    # Collect pot amount
    print_slow("\nWhat is the amount of money in the pot?: ")
    while True:
        amount = int_validator()
        if amount > 0:
            break
        else:
            print_slow("\namount must be greater than 0") 

    #Input all information into the Class
    pot = Pot(pot_id=pot_id, pot_name=pot_name, start=start_date, end=end_date, vault=vault, amount=amount)
    
    if pot:
        print_slow("\nThanks, your pot has been created succesfully")
    else:
        print_slow("\nERROR: pot not created succesfully")
    
    return pot

def create_vault(x, user):
    # Collect vault name
    print_slow("What is your preferred name for the vault?: ")
    vault_name = input()
    
    # Collect vault id
    vault_id = x

    # Collect start date data and create date object
    print_slow("\nExcellent. Now we'll define when the vault will be in use. Please note, all date input values must be in the format DD/MM/YY")
    start_date = collect_date("What is the start date that this vault will be active?: ")

    # Collect end date data and create date object
    end_date = collect_date("\nWhat is the end date that this vault will be active?: ")

    #Input all information into the Class
    vault = Vault(vault_id=vault_id, vault_name=vault_name, start=start_date, end=end_date, user=user)
    
    if vault:
        print_slow("\nThanks, your vault has been created succesfully")
    else:
        print_slow("\nERROR: vault not created succesfully")
    
    return vault