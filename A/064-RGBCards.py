
from functools import reduce

rgb_str_arr = input().split()
# reduce は初期値の指定も第三引数で可能
combined_num = int(reduce(lambda s1, s2: s1+s2, rgb_str_arr))
answer = 'YES' if combined_num % 4 == 0 else 'NO'
print(answer)
