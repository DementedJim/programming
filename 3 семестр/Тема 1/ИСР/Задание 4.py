'''
Иванов Дмитрий, ИВТ3

1.4. Создание сценария, вычисляющего операции сложения, 
вычитания, умножения, деления для двух операндов.
'''


a=float(input('Введите первое число: '))
b=float(input('Введите второе число: '))
c=str(input('Введите операцию: +,-,*,/  : '))

def calc(a,b,c):
    if c=="+":
        print(a+b)
        
    if c=="-":
        print(a-b)
        
    if c=="*":
        print(a*b)
        
    if c=="/":
        if b==0:
            print("Деление на 0! ")
        else:
            print(float(a/b))

calc(a,b,c)
