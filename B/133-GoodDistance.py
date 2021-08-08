
def calc_dist(dim, coo_arr1, coo_arr2) -> float:
    sum = 0
    for i in range(dim):
        sum += pow(coo_arr1[i]-coo_arr2[i], 2)
    return pow(sum, 0.5)


if __name__ == '__main__':
    num, dim = map(int, input().split())

    world_arr = [None] * num
    for n in range(num):
        world_arr[n] = list(map(int, input().split()))

    pattern = 0
    for i in range(num-1):
        for j in range(i+1, num):
            if calc_dist(dim, world_arr[i], world_arr[j]).is_integer():
                pattern += 1
    print(pattern)
