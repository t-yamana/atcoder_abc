
n = int(input())
nums = [int(i) for i in input().split()]
# nums = list(map(int, input().split()))

times = 0
nums = [i / 2 for i in nums if i % 2 == 0]

while len(nums) == n:
    times += 1
    nums = [i / 2 for i in nums if i % 2 == 0]

# 他の回答
# while all(a % 2 == 0 for a in nums)

print(times)
