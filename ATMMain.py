from ATMMenu import menu
from ATMExcept import depositError,withdrawError,InsufficientFundsError
from ATMOperations import deposit,withdraw,BalEnq
while(True):
    try:
        menu()
        ch=int(input("Enter your choice:"))
        match(ch):
            case 1:
                try:
                    deposit()
                except depositError:
                    print("Dont Enter Zero or Negative Number for Deposit")
                except ValueError:
                    print("Dont Enter ALPHANUMERIC,STR AND SYMBOLS for Deposit")
            case 2:
                try:
                    withdraw()
                except withdrawError:
                    print("Dont Enter Zero or Negative Number for Withdraw")
                except InsufficientFundsError:
                    print("Dont Enter the amount Greater than available amount")
                except ValueError:
                    print("Dont Enter ALPHANUMERIC,STR AND SYMBOLS for Withdraw")
            case 3:
                BalEnq()
                break
            case 4:
                print("Thank You")
            case _:
                print("Invalid Choice----Try again")
    except ValueError:
        print("DONT Enter ALPHANUMERIC,STR AND SYMBOLS for Choice")



