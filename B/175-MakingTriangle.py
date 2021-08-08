# from scipy.special import comb
from functools import reduce


def calc_dist(dim, coo_arr1, coo_arr2) -> float:
    sum = 0
    for i in range(dim):
        sum += pow(coo_arr1[i]-coo_arr2[i], 2)
    return pow(sum, 0.5)


if __name__ == '__main__':
    num = int(input())
    len_arr = list(map(int, input().split()))

    # Combination の数をチェックする
    # print(comb(num, 3))

    pat = 0
    for i in range(num-2):
        for j in range(i+1, num-1):
            for k in range(j+1, num):
                len_set = {len_arr[i], len_arr[j], len_arr[k]}
                max_len = max(len_set)
                len_set.discard(max_len)  # 返り値ないことに注意
                others = list(len_set)
                if len(others) < 2:
                    continue
                else:
                    other_sum = reduce(lambda a, b: a+b, others)
                    if max_len >= other_sum:
                        continue
                    else:
                        pat += 1
    print(pat)
