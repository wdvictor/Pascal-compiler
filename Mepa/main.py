

import sys
file = open(sys.argv[1], 'r')

code = file.read()

code = code.replace(',', '')

code = code.split('\n')

mepa = []

for i in range(len(code)):
    code[i] = code[i].lstrip()

for i in range(len(code)):
    mepa.append(code[i].split(' '))

M = []
D = []
s = 0
line = 0

initial_stack_memory = 300
index = 0

while index <= initial_stack_memory:
    index += 1
    M.append(-1)


def INPP():
    D.append(0)
    global s
    s = -1

def CRCT(k):
    global s
    s += 1
    M[s] = int(k)


def SOMA():
    global s
    M[s-1] = int(M[s-1]) + int(M[s])
    s = s-1


def MULT():
    global s
    M[s-1] = int(M[s-1]) * int(M[s])
    s = s-1


def DIV():
    global s
    M[s-1] = M[s-1]/M[s]
    s = s-1



def INVR():
    global s
    M[s] = -M[s]


def NEGA():
    global s
    M[s] = 1 - M[s]



def CONJ():
    global s
    if M[s-1] == 1 and M[s] == 1:
        M[s-1] = 1
    else:
        M[s-1] = 0

    s = s-1



def DISJ():
    global s
    if M[s-1] == 1 or M[s] == 1:
        M[s] = 1
    else:
        M[s] = 0

    s = s-1



def CMME():
    global s
    if M[s-1] < M[s]:
        M[s-1] = 1
    else:
        M[s-1] = 0

    s = s-1


def CMIG():
    global s
    if M[s-1] == M[s]:
        M[s-1] = 1
    else:
        M[s-1] = 0

    s = s-1



def CMDG():
    global s
    if M[s-1] != M[s]:
        M[s] = 1
    else:
        M[s] = 0

    s = s-1



def CMAG():
    global s
    if M[s-1] >= M[s]:
        M[s] = 1
    else:
        M[s] = 0

    s = s -1



def CMEG():
    global s
    if int(M[s-1]) <= int(M[s]):
        M[s-1] = 1
    else:
        M[s-1] = 0

    s = s-1



def DSVF(p):
    global s, line
    if M[s] == 0:
        for index in range(len(mepa)):
            if mepa[index][0] == p + ':':
                line = index
                return iter(mepa[index: len(mepa)])
    else:
        return False



def DSVS(p):
    global s, line
    for index in range(len(mepa)):
        if mepa[index][0] == p+':':
            line = index
            return iter(mepa[index: len(mepa)])

    print('Linha {}: RunTime error rotulo {} invalido'.format(line, p))
    exit(1)




def NADA():
    pass


def AMEM(n):
    global s
    s = s+int(n)


def DMEM(n):
    global s
    s = s-int(n)
    if s < -1:
        print('Linha {}: RunTime error. Stack underflow'.format(line))
        exit(1)



def CRVL(m, n):
    global s
    s = s+1
    M[s] = M[D[int(m)] + int(n)]


def ARMZ(m, n):
    global s
    M[D[int(m)] + int(n)] = M[s]
    s -= 1


def LEIT():
    global s
    s = s + 1
    M[s] = input()


def IMPR():
    global s
    print(M[s])
    s = s - 1


functions = {'INPP': INPP, 'CRCT': CRCT, 'AMEM': AMEM, 'SOMA': SOMA, 'MULT': MULT,
             'DIV': DIV, 'INVR': INVR, 'NEGA': NEGA, 'CONJ': CONJ, 'DISJ': DISJ,
             'CMME': CMME, 'CMIG': CMIG, 'CMDG': CMDG, 'CMAG': CMAG, 'CMEG': CMEG,
             'DSVF': DSVF, 'DSVS': DSVS, 'NADA': NADA, 'DMEM': DMEM, 'CRVL': CRVL,
             'ARMZ': ARMZ, 'LEIT': LEIT, 'IMPR': IMPR
             }


def get_func(arg):
    return functions.get(arg)


mepa_iter = iter(mepa)

while True:
    line += 1
    i = next(mepa_iter)
    if i[0][-1] == ':':
        pass
    elif i[0] == 'DSVS':
        mepa_iter = DSVS(i[1])
    elif i[0] == 'DSVF':
        k = DSVF(i[1])
        if k != False:
            mepa_iter = k
        s-=1
    elif i[0] == 'PARA':
        import time

        start_time = time.time()
        print("--- %s seconds ---" % (time.time() - start_time))
        exit(1)
    else:
        if len(i) == 1:
            func = get_func(i[0])
            func()
        elif len(i) == 2:
            func = get_func(i[0])
            func(i[1])
        elif len(i) == 3:
            func = get_func(i[0])
            func(i[1], i[2])



















