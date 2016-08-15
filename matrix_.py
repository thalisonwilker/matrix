import sys,time

class matrix:
    def __init__(self):
        frase = ['Call trans opt: received. 9-18-99 14:32:21 REC:Log>',
        'WARNING: carrier anomaly',
        'Trace program: running',
        'SISTEM FAILURE',
        'SISTEM FAILURE',
        'SISTEM FAILURE',
        'SISTEM FAILURE',
        'SISTEM FAILURE',
        'SISTEM FAILURE',
        'SISTEM FAILURE',
        'SISTEM FAILURE']
        for l in frase:
            if 'SISTEM FAILURE' in l:
                for c in l:
                    sys.stdout.write(c)
                    time.sleep(0.01)
            else:
                for c in l:
                    sys.stdout.write(c)
                    time.sleep(0.03)
            time.sleep(2)
            print ''

matrix()
