
if __name__ == '__main__':
    n = int(input())
    scores = {}
    for i in range(n):
        key = input()
        scores.setdefault(key, 0)
        scores[key] += 1

    m = int(input())
    for i in range(m):
        key = input()
        scores.setdefault(key, 0)
        scores[key] -= 1

    highest = max(scores.values())
    print(highest) if highest > 0 else print(0)
