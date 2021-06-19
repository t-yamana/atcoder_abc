
import math


def repute_price(price: int) -> str:
    if price < 206:
        rep = 'Yay!'
    elif price == 206:
        rep = 'so-so'
    else:
        rep = ':('
    return rep


row_price = int(input())
taxed_price = math.floor(row_price * 1.08)
print(repute_price(taxed_price))
