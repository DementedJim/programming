def f(r, T, t, ts):
    return -r * ts * (T - t)


Ts = 22
y = 83
r = 0.073
b = 10
a = 0
x = 0
h = (b - a) / 60
while x <= b - h:
    x += h
    y = y + h * f(r, y, Ts, x)
    print ('Температура кофе = {:.2f}\t Температура окр. среды = {}\t Времени прошло = {:.2f}'.format(y, Ts, x))