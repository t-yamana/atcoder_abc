
if __name__ == '__main__':

    n = int(input())
    ropes = [None] * n
    for i in range(n):
        l, s = map(int, input().split())
        ropes[i] = (l, s)

    cl = 0  # calculated_length
    for i in range(n):
        cl += ropes[i][0] / ropes[i][1]

    c_proc = 0  # calc_process
    r_proc = 0  # real_process

    for i in range(n):
        partial = ropes[i][0] / ropes[i][1]
        if c_proc + partial < cl/2:
            c_proc += partial
            r_proc += ropes[i][0]
            continue
        else:
            c_dist = c_proc + partial - cl/2
            r_dist = ropes[i][0] - (c_dist * ropes[i][1])
            break

    print(r_proc + r_dist)
