
if __name__ == '__main__':
    h, w, n = map(int, input().split())
    xxx = set()
    yyy = set()
    cards = []
    for i in range(n):
        a, b = map(int, input().split())
        cards.append((a, b))
        xxx.add(a)
        yyy.add(b)

    # { 変換前の行: 変換後の行 }
    x_dict = {x: i for i, x in enumerate(sorted(xxx), start=1)}
    # { 変換前の列: 変換後の列 }
    y_dict = {y: i for i, y in enumerate(sorted(yyy), start=1)}

    for a, b in cards:
        print(x_dict[a], y_dict[b])
