# https://atcoder.jp/contests/abc246/tasks/abc246_c

import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

n, k, x = map(int, input().split())
prices = LI()

full_times = list(map(lambda p: p//x, prices))

# check lack of tickets
used_tickets = min(sum(full_times), k)

excesses = list(map(lambda p: p%x, prices))

lefted_item_counts = len(excesses) - excesses.count(0)

# check excess tickets
pick = min(k - used_tickets, lefted_item_counts)
picked = sorted(excesses, reverse=True)[:pick]

ans = sum(prices) - x * used_tickets - sum(picked)
print(ans)
