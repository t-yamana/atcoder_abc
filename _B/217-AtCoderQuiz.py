
if __name__ == '__main__':
    compes = set(['ARC', 'AGC', 'AHC', 'ABC'])
    for i in range(3):
        compes.remove(input())
    assert(len(compes) == 1)
    print(compes.pop())
