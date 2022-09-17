import sys
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

seed = I()
seed_bin = '{:8b}'.format(seed).strip()  # 2進数へ変換

def find(s, ch):
  return [i for i, ltr in enumerate(s) if ltr == ch]

indices = find(seed_bin, '0')
indices.reverse()
indices = [len(seed_bin) - a for a in indices]  # お尻からのidx

# 0 を挟まない連続数列
one_count = len(seed_bin)-len(indices)
nums = list(range(pow(2, one_count)))

nums_offset = []
_nums_offset = []  # Debug
for n in nums:
  txt = '{:8b}'.format(n).strip()
  for i in indices:
    idx = len(txt)-i+1 if len(txt)-i >= 0 else None
    if idx is None: break
    txt = txt[:idx]+'0'+txt[idx:]
  _nums_offset.append(txt)
  nums_offset.append(int(txt, 2)) # bit string -> int

# print(_nums_offset)
for a in nums_offset:
  print(a)
