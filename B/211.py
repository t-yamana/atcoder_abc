
if __name__ == '__main__':
    check_hits = {'H', '2B', '3B', 'HR'}
    actual_hits = set()
    for i in range(4):
        actual_hits.add(input())
    print('Yes') if actual_hits == check_hits else print('No')
