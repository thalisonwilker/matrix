#! /usr/bin/python3
import time
import os
os.system('clear')
frase = ['Wake up, Neo...','The matrix has you...','Follow the white rabbit...']
for i in frase:
    for c in i:
        if( c == '.' ):
            time.sleep(0.3)
        elif ( c == ' ' ):
            time.sleep(0.4)
        else:
            time.sleep(0.2)
        print(c, sep='', end='', flush=True)
    print(sep="\n")
    time.sleep(0.7)
    os.system('clear')

time.sleep(3)
print('Knock, Kcnock, Neo.')
time.sleep(30)

