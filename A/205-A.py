

def liquid_amount(concent: int, amt: int) -> float:
    return concent / 100 * amt


if __name__ == '__main__':
    a, b = map(int, input().split())
    print(liquid_amount(a, b))
