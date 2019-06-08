#
# import sys
#
# try:
#     file = open(sys.argv[1] , 'r')
# except:
#     print('File not found')
#     exit(1)
#
# code = file.read()
#

#An example of mepa code. Using to avoid loading archive every time
code ='''INPP
     AMEM 2
     AMEM 3
     DSVS R00
R00: NADA 
     LEIT
     ARMZ 0, 0
     CRCT 0
     ARMZ 0, 2
     CRCT 1
     ARMZ 0, 3
     CRCT 1
     ARMZ 0, 1
R01: NADA 
     CRVL 0, 1
     CRVL 0, 0
     CMEG
     DSVF R02
     CRVL 0, 2
     CRVL 0, 3
     SOMA
     ARMZ 0, 4
     CRVL 0, 3
     ARMZ 0, 2
     CRVL 0, 4
     ARMZ 0, 3
     CRVL 0, 1
     CRCT 1
     SOMA
     ARMZ 0, 1
     DSVS R01
R02: NADA 
     CRVL 0, 0
     IMPR
     CRVL 0, 2
     IMPR
     DMEM 5
     PARA

'''

functions = []
label = ''
for i in code:
    if i == ' ':
        if label == '':
            pass
        else:
            label += i
    elif i == '\n':
        functions.append(label)
        label = ''
    elif i == ',':
        pass
    else:
        label += i


mepa = []
for i in functions:
    mepa.append(i.split(' '))

M = []
D = []
s = 0
k = '' # k is the actual function to execute

initial_stack_memory = 1024
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
    M[s-1] = M[s-1] + M[s]
    s = s-1

def MULT():
    global s
    M[s-1] = M[s-1] * M[s]
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
    if M[s-1] <= M[s]:
        M[s] = 1
    else:
        M[s] = 0

    s = s-1


def DSVF(p):
    global s
    if M[s] == 0:
        if mepa[index][0] == p + ':':
            return iter(mepa[index: len(mepa)])
        else:
            return False
    s = s+1


def DSVS(p):
    for index in range(len(mepa)):
        if mepa[index][0] == p+':':
            return iter(mepa[index: len(mepa)])



def NADA():
    pass


def AMEM(n):
    global s
    #put '-2' to say that area is reserved
    s = s+int(n)


def DMEM(n):
    global s
    s = s-int(n)


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

'''
['INPP']
['DSVS', 'R00']
['DSVF', 'R00']
['AMEM', '2']
['AMEM', '3']
['R00:', 'NADA']
['LEIT']
['ARMZ', '0,', '0']
['CRCT', '0']
'''


mepa_iter = iter(mepa)

try:

    while True:
        i = next(mepa_iter)
        if i[0][-1] == ':':
            pass
        elif i[0] == 'DSVS':
            mepa_iter = DSVS(i[1])
        elif i[0] == 'DSVF':
            k = DSVF(i[1])
            if k != False:
                mepa_iter = DSVF(i[1])
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


except:
    exit(1)


















