
# from functools import reduce

s_text = sorted(input())
t_text = sorted(input(), reverse=True)

# s_sorted = reduce(lambda c1, c2: c1+c2, s_text, '')
# t_reversed = reduce(lambda c1, c2: c1+c2, t_text, '')
# print('Yes' if s_sorted < t_reversed else 'No')

# 配列のままでも比較できる
print('Yes' if s_text < t_text else 'No')
