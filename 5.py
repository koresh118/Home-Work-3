
def my_func (a, d, e, b, g):
    for i in range (a + 1):
            if (d < 0):
                e = int (b [0 : ])
            else:
                e = int (b [0 : d]) 
                b = b [(d + 1) : ]
                d = b.find (' ')
            g += e
            print (g)
a = 0
c = 0
e = 0
g = 0
d = 0
f = 0
h = 0
s = 0
j = ''
win = True
while (win):
    b = input ('Введите целые числа, разделяя их пробелом: ')
    a = b.count (' ', 0)
    d = b.find (' ')
    f = b.count ('q', 0)
    if (f > 0):
        h = b.find ('q')
        b = b [0 : (h - 1)]
        my_func (a, d, e, b, g)
        win = False
        
    else:
        my_func (a, d, e, b, g)
        j = input ('Посчитать ещё (ENTER - ДА, Q - выход)? ')
        if (j == 'q'):
            win = False
        else:
            s = g
            win = True
            
