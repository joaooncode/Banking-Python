from time import sleep

running = True
balance = 0

print("PYTHON BANKING\n".center(50))


def display_balance(balance):
    print(f"Your current balance is ${balance:.2f}")


def withdraw(balance):
    withdraw = float(input(f"How much would like to withdraw? $: "))
    if withdraw > balance:
        print(f"Insuficient funds! Please enter a valid amount $: ")
        withdraw = float(input(f"How much would like to withdraw $: "))
    elif withdraw <= 0:
        print("With draw can not be 0 or less... Please enter a valid amount $: ")
        withdraw = float(input(f"How much would like to withdraw? $: "))

    else:
        balance -= withdraw
        print(f"Withdraw Successful! Your current balance is ${balance:.2f}")
        print(f"Amount withdrawn {withdraw:.2f}")


def deposit(balance):
    deposit = float(input("How much would like to deposit?  $: "))
    if deposit <= 0:
        print("Please enter a amount greater than 0...")
        deposit = float(input("How much would like to deposit?  $: "))
    else:
        balance = balance + deposit
        print(f"Deposit successful! Your current balance is ${balance:.2f}")


def main():
    while running:

        print("-" * 50)
        print("1. Display current balance")
        print("2. Withdraw")
        print("3. Deposit")
        print("4. Exit the program")
        choice = int(input("Enter your option: 1-4: "))
        match choice:
            case 1:
                display_balance(balance)
            case 2:
                withdraw(balance)
            case 3:
                deposit(balance)
            case 4:
                print("EXITING APP!")
                sleep(2)
                break
            case _:
                print("INVALID OPTION!!")
                continue


if "__name__" == "__main__":
    main()

main()
