# Weak Password

if __name__ == '__main__':
    pswd = input()
    pswd_arr = [int(a) for a in pswd]

    base_num = pswd_arr[0]
    weak_arr1 = [base_num] * 4

    weak_arr2 = [None] * 4
    for i in range(4):
        weak_arr2[i] = base_num
        if base_num == 9:
            base_num = 0
        else:
            base_num += 1

    # 配列の比較 (isはダメ)
    if pswd_arr == weak_arr1:
        print('Weak')
    elif pswd_arr == weak_arr2:
        print('Weak')
    else:
        print('Strong')
