
num = int(input())

mountains = []
for i in range(num):
    name, height = input().split()
    mountains.append((name, int(height)))  # tupleの配列
mountains = sorted(mountains, key=lambda u: u[1])

print(mountains[num-2][0])  # 後ろから二番目
