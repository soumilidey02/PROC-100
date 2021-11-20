class Atm:

    def __init__(self,card_number,pin_number):
        self.cardnumber = card_number
        self.pin = pin_number

    def check_balance(self):
        print("Your balance is 50000")

    def withdrawl(self,amount):
        new_amount = 50000 - amount
        print("you have withdrawn amount "+str(amount) +". Your remaining balance is "+ str(new_amount))


def main():
    Card_number = input("please insert your card number: ")
    pin_number  = input("please enter your pin number: ")

    new_user =  Atm(Card_number ,pin_number)

    print("Choose what to do ")
    print("1.Balance Enquriy   2.Withdrawl")
    work = int(input("please enter the number for work chosen: "))

    if (work == 1):
        new_user.check_balance()
    elif (work == 2):
        amount = int(input("please enter the amount: "))
        new_user.withdrawl(amount)
    else:
        print("please enter a valid number")


if __name__ == "__main__":
    main()