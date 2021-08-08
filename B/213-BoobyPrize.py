
if __name__ == '__main__':
    n = int(input())
    scores = list(map(int, input().split()))

    max_score = max(scores)

    semi_max = 0
    semi_max_idx = 0

    for i, s in enumerate(scores, 1):
        if semi_max < s and s < max_score:
            semi_max = s
            semi_max_idx = i

    print(semi_max_idx)
