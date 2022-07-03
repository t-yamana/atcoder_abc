import math

pep, cookie = map(int, input().split())
ids = [int(a) for a in input().split()]
sorted_ids = sorted(ids)

# math.floor は桁数が大きい時、誤った値を返す可能性が出てくる
# // を使用するとそんなことはない

# cookie = 1_000_000_000_000_000_000 の時、誤った値
common_point1 = math.floor(cookie / pep)
common_point = cookie // pep
cookie -= common_point * pep

print(common_point1)
print(common_point)

# 辞書に順番はない
cookie_dict = {id: common_point for id in ids}

for i in sorted_ids[0:cookie]:
    cookie_dict[i] += 1

for i in ids:
    print(cookie_dict[i])
