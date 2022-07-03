
n = int(input())
a = int(input())
excess = n % 500
answer = 'Yes' if excess <= a else 'No'
print(answer)
