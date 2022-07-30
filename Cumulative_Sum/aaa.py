
A = [2, 5, 1]

sum = [None] * (len(A)+1)
sum[0] = 0

for i in range(len(A)):
  sum[i+1] = sum[i] + A[i]

print(sum)
