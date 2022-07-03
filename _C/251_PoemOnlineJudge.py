
n = int(input())
org_txt = set()
org = dict()
all_txt = [None] * n
for i in range(n):
  sub = input().split()
  all_txt[i] = sub[0]
  if sub[0] not in org_txt:
    org_txt.add(sub[0])
    org.setdefault(sub[0], int(sub[1]))

max_score = max(list(org.values()))
max_txt = []

for txt, score in org.items():
  if score == max_score:
    max_txt.append(txt)

ans = []
for txt in max_txt:
  ans.append(all_txt.index(txt))

print(min(ans)+1)
