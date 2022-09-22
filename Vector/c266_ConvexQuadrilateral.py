# https://atcoder.jp/contests/abc266/tasks/abc266_c

import sys
def TI(): return tuple(map(int,sys.stdin.readline().rstrip().split()))

vecs = [TI() for _ in range(4)]
angs = [None] * 4

for i in range(4):
  # 順番は反時計回りとなるように
  # 後の点へのベクトル
  vec1 = (vecs[(i+1)%4][0]-vecs[i][0], vecs[(i+1)%4][1]-vecs[i][1])
  # 前の点へのベクトル
  vec2 = (vecs[(i+3)%4][0]-vecs[i][0], vecs[(i+3)%4][1]-vecs[i][1])

  # 内積(inner) -> angle とすると違う側の角度が取られたのでダメ
  # 外積(cross_product) からベクトルの関係が分かる
  x_product = vec1[0]*vec2[1] - vec1[1]*vec2[0]
  # 負だと最初のベクトルの右側に二番目のベクトルが来る(180度以上)
  if x_product < 0:
    print('No')
    exit()

print('Yes')
