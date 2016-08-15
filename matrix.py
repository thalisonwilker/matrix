import sys,time

def matrix():
    frase = ['Wake up, Neo','The matrix has you','Follow the white rabbit...']
    
    for i in frase:
        for c in i:
            sys.stdout.write(c)
            time.sleep(0.12)
        time.sleep(1)
        print ''
    time.sleep(2)
    print 'Knock, Kcnock, Neo.'

matrix()
