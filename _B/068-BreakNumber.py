
a = int(input())
a_bin = '{:8b}'.format(a)  # 2進数へ変換
# print(a_bin)

start = a_bin.find('1')  # 0111 -> 最初の1以降は0とする
if start > -1:
    b_bin = 2 ** len(a_bin[start + 1:])  # 0100 -> 2**2 -> 4
else:
    b_bin = 0

print(b_bin)
