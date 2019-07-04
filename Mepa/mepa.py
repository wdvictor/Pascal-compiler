
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

labels = []
if mepa[-1] == ['']:
    mepa.pop()

for i in range(len(mepa)):
    if mepa[i][0][-1] == ':':
        labels.append([mepa[i][0], i])

M = []
D = []
s = 0
line = 0

initial_stack_memory = 1024
index = 0

while index <= initial_stack_memory:
    index += 1
    M.append(-1)

def DSVF(p):
    global s, line, labels
    interator = 0
    for i in labels:
        if i[0] == p + ':':
            line = i[1]
            interator = iter(mepa[i[1]: len(mepa)])

    if interator == 0:
        print('Linha {}: RunTime error rotulo {} invalido'.format(line, p))
        exit(0)

    if M[s] == 0:
        return interator

    else:
        return False

def DSVS(p):
    global s, line, labels
    interator = 0
    for i in labels:
        if i[0] == p + ':':
            line = i[1]
            interator = iter(mepa[i[1]: len(mepa)])

    if interator == 0:
        print('Linha {}: RunTime error rotulo {} invalido'.format(line, p))
        exit(0)
    else:
        return interator


mepa_iter = iter(mepa)

while mepa is not None:
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
        exit(0)
    elif i[0] == 'INPP':
        D.append(0)
        s = -1
    elif i[0] == 'CRCT':
        s += 1
        M[s] = int(i[1])
    elif i[0] == 'SOMA':
        M[s - 1] = int(M[s - 1]) + int(M[s])
        s = s - 1
    elif i[0] == 'MULT':
        M[s - 1] = int(M[s - 1]) * int(M[s])
        s = s - 1
    elif i[0] == 'DIVI':
        M[s - 1] = M[s - 1] / M[s]
        s = s - 1
    elif i[0] == 'INVR':
        M[s] = -M[s]
    elif i[0] == 'NEGA':
        M[s] = 1 - M[s]
    elif i[0] == 'CONJ':
        if M[s - 1] == 1 and M[s] == 1:
            M[s - 1] = 1
        else:
            M[s - 1] = 0
        s = s - 1
    elif i[0] == 'DISJ':
        if M[s - 1] == 1 or M[s] == 1:
            M[s-1] = 1
        else:
            M[s-1] = 0

        s = s - 1
    elif i[0] == 'CMME':
        if M[s - 1] < M[s]:
            M[s - 1] = 1
        else:
            M[s - 1] = 0

        s = s - 1
    elif i[0] == 'CMIG':
        if M[s - 1] == M[s]:
            M[s - 1] = 1
        else:
            M[s - 1] = 0

        s = s - 1
    elif i[0] == 'CMDG':
        if M[s - 1] != M[s]:
            M[s-1] = 1
        else:
            M[s-1] = 0

        s = s - 1
    elif i[0] == 'CMAG':
        if M[s - 1] >= M[s]:
            M[s-1] = 1
        else:
            M[s-1] = 0

        s = s - 1
    elif i[0] == 'CMEG':
        if int(M[s - 1]) <= int(M[s]):
            M[s - 1] = 1
        else:
            M[s - 1] = 0

        s = s - 1
    elif i[0] == 'NADA':
        pass
    elif i[0] == 'AMEM':
        s = s+int(i[1])
    elif i[0] == 'DMEM':
        s = s - int(i[1])
        if s < -1:
            print('Linha {}: RunTime error. Stack underflow'.format(line))
            exit(0)
    elif i[0] == 'CRVL':
        s = s + 1
        M[s] = M[D[int(i[1])] + int(i[2])]
    elif i[0] == 'ARMZ':
        M[D[int(i[1])] + int(i[2])] = M[s]
        s -= 1
    elif i[0] == 'LEIT':
        s = s + 1
        M[s] = input()
    elif i[0] == 'IMPR':
        print(M[s])
        s = s - 1
    elif i[0] == 'SUBT':
        M[s-1] = M[s-1] - M[s]
        s -= 1
    elif i[0] == 'CMMA':
        if M[s-1] > M[s]:
            M[s-1] = 1
        else:
            M[s-1] = 0

        s -= 1
