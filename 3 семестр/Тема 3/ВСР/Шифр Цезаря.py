"""
Иванов Дмитрий, ИВТ3

Программа работает только с латиницей
"""

def caesar(s, step):
    u = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    l = 'abcdefghijklmnopqrstuvwxyz'
    res = ''
    for i in s:
        if (i.islower()):
            res += l[(l.index(i) + step) % len(l)]
        else:
            res += u[(u.index(i) + step) % len(u)]
    return res
    
print('vvedite sdvig')
step = int(input())
print('vvedite text dlya shifrovania')
s = str(input())
print(rot(s, step))
