def porov(s):
    for c in s:
        if not(c in '1234567890'):
            return False
    return True


def main(*args):
    l1 = []
    l2 = []
    for c in args:
        if type(c) == str:
            if porov(c):
                l1.append(int(c))
            else:
                l2.append(c)
        else:
            l1.append(c)
    l3 = sorted(l1) + sorted(l2)
    return l3


print(main(3, '167', 'a', 'г', 'б', 'я', 1, 49, 0, True, False, 8.2324))


if __name__ == '__main__':
    assert main(3, 2, 1, 49, 0) == [0, 1, 2, 3, 49], "Сортировка не удалась"
    assert main(4, 1, 7, 92, 3) == [1, 3, 4, 7, 92], "Сортировка не удалась"
    assert main(9, 21, 1, 38, 98, 56) == [1, 9, 21, 38, 56, 98], "Сортировка не удалась"