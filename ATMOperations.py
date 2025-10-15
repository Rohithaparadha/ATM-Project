#ATMOperations.py
bal=500
from ATMExcept import depositError, withdrawError,InsufficientFundsError


def deposit():
    damt=float(input("Enter the amount to deposit: "))
    if damt<=0:
        raise depositError
    else:
        global bal
        bal=bal+damt
        print("\t\tUr AC No:XXXX11243 Credited with {}".format(damt))
        print("\t\tUr AC No:XXXX11243 Balance after deposit: {}".format(bal))
def withdraw():
    global bal
    wamt=float(input("Enter the amount to withdraw: "))
    if (wamt<=0):
        raise withdrawError
    else:
        if (wamt+500)>bal:
            raise InsufficientFundsError
        else:
            bal=bal-wamt
            print("\t\tUr AC No:XXXX11243 Debited with {}".format(wamt))
            print("\t\tUr AC No:XXXX11243 Balance after withdraw: {}".format(bal))
def BalEnq():
    print("\t\tUR AC No:XXXX11243 Balance: {}".format(bal))



