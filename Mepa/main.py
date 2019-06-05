import sys
#
# try:
#     file = open(sys.argv[1] , 'r')
# except:
#     print('File not found')
#     exit(1)


code = '''
     INPP
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




M = []
D = []
s = 0



def INPP(D):
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




def IMPR():
    global s
    print(M[s])
    s = s - 1




# INPP CRCT SOMA MULT SUBT DIVI INVR NEGA CONJ DISJ CMME CMMA CMIG
# CMDG CMAG CMEG DSVF DSVS NADA AMEM DMEM CRVL ARMZ IMPR LEIT















