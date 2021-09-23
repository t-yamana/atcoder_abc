
rot_str = reversed(input())

rot_dict = {
    '0': '0',
    '1': '1',
    '6': '9',
    '8': '8',
    '9': '6',
}

ans = ''
for a in rot_str:
    ans += rot_dict[a]

print(ans)
