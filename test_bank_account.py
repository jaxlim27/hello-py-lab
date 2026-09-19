from bank_account import BankAccount

def main():
    # Create an account
    name = input("Enter account holder name: ")
    account = BankAccount(name)
    
    print(f"\nWelcome, {account.account_holder}!")
    print(f"Initial balance: ₱{account.get_balance():.2f}")
    
    # Deposit
    deposit_amount = float(input("\nEnter deposit amount: "))
    if account.deposit(deposit_amount):
        print(f"Deposit successful. New balance: ₱{account.get_balance():.2f}")
    else:
        print("Invalid deposit amount.")
    
    # Withdraw
    withdraw_amount = float(input("\nEnter withdrawal amount: "))
    if account.withdraw(withdraw_amount):
        print(f"Withdrawal successful. New balance: ₱{account.get_balance():.2f}")
    else:
        print("Insufficient funds or invalid amount.")
    
    # Final details
    print("\n" + str(account))

if __name__ == "__main__":
    main()
