class bank:
    bank_name="BOI"
    rate_of_interest= 12.25

    def si(p,n):
        si=(p* bank.rate_of_interest*n)/100
        print(si)
p = float(int(input("Enter the principal amount: ")))
n= int(input("Enter the number of years: "))
bank.si(p,n)