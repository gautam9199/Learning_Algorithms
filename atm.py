import math

#overall balance for initial stage
Balance ={
        "2000":100,
        "500":100,
        "200":100,
        "50":100
    }

#numbers of currancy not to be selected for entered amount
def numberofnote(cuuruncy, Ammount):
    reminder =  Ammount / cuuruncy
    reminder = math.floor(reminder)
    return reminder
#calculate remaining balance after tr ansaction
def RemainingBalance(noteCount, currency, Balance, Ammount):
    count = Balance[str(currency)]
    Balance[str(currency)] = count - noteCount
    Ammount = Ammount - (currency*noteCount)
    print(f"Remaining Ammount..{Ammount}"  )
    combo = [Balance, Ammount]
    return combo
#flow
def main():
    Ammount = input("Enter the amount you want to withdraw..: ")
    Ammount = int(Ammount)
    withdraw(Ammount)

#algorithm for withdraval ...
def withdraw (Ammount):
  #  Balance ={
  #      "2000":100,
  #      "500":100,
  #      "200":100,
  #      "50":100
  #  }


 if Ammount > 2000:
    print("in 2000")
    noteCount = numberofnote(2000, Ammount)
    combo = RemainingBalance(noteCount, 2000, Balance, Ammount)
    withdraw(combo[1])
 elif Ammount > 500:
    print("in 500")
    noteCount = numberofnote(500, Ammount)
    combo = RemainingBalance(noteCount, 500, Balance, Ammount)
    withdraw(combo[1])
 elif Ammount > 200:
    print("in 200")
    noteCount = numberofnote(200, Ammount)
    combo = RemainingBalance(noteCount, 200, Balance, Ammount)
    withdraw(combo[1])
 elif Ammount > 100:
    print("in 100")
    noteCount = numberofnote(100, Ammount)
    combo = RemainingBalance(noteCount, 100, Balance, Ammount)
    withdraw(combo[1])
 elif Ammount > 50:
    print("in 50")
    noteCount = numberofnote(50, Ammount)
    combo = RemainingBalance(noteCount, 50, Balance, Ammount)
    withdraw(combo[1])
 else:
    print(Balance)
    main()



main()

