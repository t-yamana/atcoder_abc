
n = int(input())
factors = sorted(map(int, input().split()))

pat = 1
pre = None
for i, a in enumerate(factors):
    # 毎回やらないと TLE
    pat = pat * (a-i) % 1_000_000_007

print(pat % 1_000_000_007)
