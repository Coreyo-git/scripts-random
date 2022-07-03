coke_price = 50
input_price = 0

def whichCoin(coin):
  match coin:
    case 5:
      return 5
    case 10:
      return 10
    case 25:
      return 25
    case _:
    	return 0

while True:
  coin_inserted = int(input("Insert Coin: "))
  input_price = int(input_price) + int(whichCoin(coin_inserted))
  if input_price > 50:
    print("Paid, Change Amount: ", input_price - coke_price)
    break

  
