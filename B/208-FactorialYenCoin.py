
p = int(input())

fact_arr = []
idx = 1
val = 1
while True:
    val *= idx
    if val > 10_000_000:
        break
    fact_arr.append(val)
    idx += 1

# [1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800]
fact_arr.reverse()  # 副作用アリ

idx = 0
num_coins = 0
while True:
    if p >= fact_arr[idx]:
        num_coins += 1
        p -= fact_arr[idx]
    elif p == 0:
        break
    else:
        idx += 1

print(num_coins)
