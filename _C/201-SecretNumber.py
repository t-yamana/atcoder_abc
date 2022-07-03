

class number_checker:
    def __init__(self, format: str) -> None:
        self._cnt = 0
        self._good_chars = []
        self._bad_chars = []
        for i in range(10):
            if format[i] == 'o':
                self._good_chars.append(str(i))
            elif format[i] == 'x':
                self._bad_chars.append(str(i))

    def check_format(self, num: int) -> None:
        string_number = str(num).zfill(4)
        flag = True
        for a in self._good_chars:
            if a not in string_number:
                flag = False
                break
        for a in self._bad_chars:
            if a in string_number:
                flag = False
                break
        if flag is True:
            self._cnt += 1

    def sum_count(self) -> int:
        return self._cnt


pass_str = input()
nc = number_checker(pass_str)

if pass_str.count('o') >= 5:
    print(0)
else:
    for a in range(10000):
        nc.check_format(a)
    print(nc.sum_count())
