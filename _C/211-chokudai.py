
if __name__ == '__main__':
    text = input().rstrip("\n")
    his_name = "chokudai"
    combo_map = [0]*8

    # chcho■■■■■
    for i in range(len(text)):
        # chokudai
        for j in range(len(his_name)):
            if text[i] == his_name[j]:
                if j == 0:
                    combo_map[0] += 1  # 先頭文字 c の数
                else:
                    combo_map[j] += combo_map[j-1]
        combo_map[7] %= 1000000007
    print(combo_map[7])
