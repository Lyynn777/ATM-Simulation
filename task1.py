import time

print("Insert your card")
#wait for 5 seconds
time.sleep(5)
password = 5678 #set the password
pin = int(input("Enter ATM pin: ")) #ask the user for their PIN
balance = 7000 #set the initial balance
transaction_history = [] #an empty list is created to store transaction history

if pin == password: #check if the entered PIN is correct
    #loop indefinitely to allow the user to perform multiple transactions
    while True:
        #print the menu options
        print("""
        1. Account balance enquiry
        2. Cash Withdrawal
        3. Cash deposit
        4. PIN change
        5. Transaction History
        6. Exit
        """)
        try:
            option = int(input("Please enter your choice: "))
        except ValueError:
            print("Please enter a valid choice.") #if the user enters something that's not a number, print an error message
            continue
        if option == 1:
            print(f"Your current account balance is {balance}") #print the current balance
        elif option == 2:
            withdraw_amt = int(input("Please enter withdrawal amount: "))
            if withdraw_amt <= balance: #check if the withdrawal amount is less than or equal to the balance
                balance -= withdraw_amt
                transaction_history.append(f"Withdrawal: -{withdraw_amt}") #append the transaction to the transaction history
                print(f"{withdraw_amt} has been debited from your account")
            else:
                print("Insufficient balance!")
        elif option == 3:
            deposit_amt = int(input("Please enter deposit amount: ")) #ask the user for the deposit amount
            balance += deposit_amt
            transaction_history.append(f"Deposit: +{deposit_amt}")
            print(f"{deposit_amt} has been credited into your account")
        elif option == 4:
            old_pin = int(input("Enter current PIN: "))
            if old_pin == password:  #check if the entered PIN is correct
                new_pin = int(input("Enter new PIN: "))
                confirm_pin = int(input("Confirm new PIN: "))
                if new_pin == confirm_pin:  #check if the new PIN and confirmed PIN match
                    password = new_pin  #update the password to the new PIN
                    print("PIN changed successfully!")
                else:
                    print("PIN mismatch! Try again.")
            else:
                print("Invalid PIN! Try again.")
        elif option == 5:
            print("Transaction history:")  #print the transaction history
            for transaction in transaction_history:
                print(transaction)
        elif option == 6: #exit the loop and end the program
            break
        else:
            print("Invalid option! Try again.")
else:
    print("Invalid PIN! Please try again")