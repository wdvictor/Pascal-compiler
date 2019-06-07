
# import sys
#
# try:
#     file = open(sys.argv[1] , 'r')
# except:
#     print('File not found')
#     exit(1)
#
# code = file.read()

code = '''INPP
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
     PARA'''

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
    else:
        label += i


mepa = []




for i in functions:
   mepa.append(i.split(' '))


#print(mepa)



M = []
D = []
s = 0
i = ''


def INPP():
    D.append(0)
    global s
    s = -1

def CRCT(k):
    global s
    s = s + 1
    M.append(k)

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
    global s, i
    if M[s] == 0:
        i = p
    else:
        i = next(i)

    s = s+1


def DSVS(p):
    global i
    i = p

def NADA():
    pass


def AMEM(n):
    global s
    s = s+n


def DMEM(n):
    global s
    s = s-n


def CRVL(m, n):
    global s
    s = s+1
    M[s] = M[D[m] + n]


def ARMZ(m, n):
    global s
    M[D[m] + n] = M[s]
    s = s - 1


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
    return functions.get(arg[0])


# func = get_func(mepa[1]) AMEM
# func(2)
# print(s) 2














