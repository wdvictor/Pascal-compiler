#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

"""
Created on Sun Jul  7 23:22:16 2019

@author: victorh
"""

code = '''program exemplo5 (input, output);
var f, n : integer;
    f1, f3 : integer;
begin
   read (n);
   f1:=0; f2:=1; k:=1;
   while k<=n do
   begin
      f3:=f1+f2;
      f1:=f2;
      f2:=f3;
      k:=k+1
   end;
   write (n, f1)
end.
'''



import LexicalAnalyzer

tokens = LexicalAnalyzer.get_tokens(code)


def relacao(tokens):

    if tokens[0] == '<' and tokens[1] == '=':
        return tokens[1:len(tokens)]
    elif tokens[0] == '>' and tokens[1] == '=':
        return tokens[1:len(tokens)]
    elif tokens[0] == '<' and tokens[1] == '>':
        return tokens[1:len(tokens)]
    elif tokens[0] == '=' or tokens[0] == '<' or tokens[0] == '>':
        return tokens[1:len(tokens)]
    else:
        return False


def comando_repetitivo(tokens):
    if tokens[0] == 'while':
        tokens = tokens[1:len(tokens)]
    else:
        return False

    x = expressao(tokens)
    if x is not False:
        tokens = x
    else:
        return False

    if tokens[0] == 'do':
        tokens = tokens[1:len(tokens)]
    else:
        return False

    x = comando_sem_rotulo(tokens)
    if x is not False:
        tokens = x
    else:
        return False

    return tokens


def numero(tokens):
    if len(re.findall('[\W][0-9]+', tokens[0])) != 0:
        return tokens[1:len(tokens)]
    else:
        return False

#TODO : <lista de identificadores>
def lid(token):
    for i in range(len(token)):
        if token[i][0] == '#':
            #identifiers.append(i)
            continue
        elif token[i] == ',' and i != 0 and token[i+1][0] == '#':
            #i != 0 para evitar erros do tipo : ", n1 , n2"
            #tokens[i+1][0]: verifica se o proximo token é um identificador, para evitar erros do tipo "n1,n2, "
            continue
        else:
            return token[i:len(token)]


#TODO : <parte de declaração de variáveis>
def pdv(tokens):

    tokens = lid(tokens)

    if tokens[0] == ':':
        tokens = tokens[1:len(tokens)]

    if tokens[0][0] == '#':
        tokens = tokens[1:len(tokens)]

    if tokens[0] == ';':
        tokens = tokens[1:len(tokens)]
        if tokens[0][0] == '#':
            tokens = pdv(tokens)

    return tokens


def variavel(tokens):

    if tokens[0][0] == '#':
        return tokens[1:len(tokens)]
    else:
        return False



def fator(tokens):

    x = variavel(tokens)
    if x is not False:
        return x

    x = numero(tokens)
    if x is not False:
        return x

    return False




def termo(tokens):

    x = fator(tokens)
    if x is not False:
        tokens = x
    else:
        return False

    if tokens[0] == '*' or tokens[0] == 'div' or tokens[0] == 'and':
        tokens = tokens[1:len(tokens)]
        x = fator(tokens)
        if x is not False:
            return x
        else:
            return False

    return tokens


def  expressao_simples(tokens):

    if tokens[0] == '+' or tokens[0] == '-':
        tokens = tokens[1:len(tokens)]

    x = termo(tokens)
    if x is not False:
        tokens = x
    else:
        return False

    if tokens[0] == '+' or tokens[0] == '-' or tokens[0] == 'or':
        tokens = tokens[1:len(tokens)]
        x = fator(tokens)
        if x is not False:
            tokens = x
        else:
            return False

    return tokens


def expressao(tokens):
    x = expressao_simples(tokens)
    if x is not False:
        tokens = x
    else:
        return False

    x = relacao(tokens)
    if x is not False:
        tokens = x
        x = expressao_simples(tokens)
        if x is not False:
            tokens = x
        else:
            return False

    return tokens

    #fazer <ralaao><expressão simlpes>


def lista_de_expressao(tokens):
    x = expressao(tokens)

    if x is not False:
        tokens = x
    else:
        return False

    while True:
        if tokens[0] == ',':
            x = expressao(tokens)
            if x is not False:
                tokens = x
            else:
                return False
        else:
            break

    return tokens





def atribuicao(tokens):

    if tokens[1] == ':' and tokens[2] == '=':
        tokens = tokens[4:len(tokens)]
    else:
        return False

    return tokens


    #TODO : continuar


def chamada_de_procedimento(tokens):

    if tokens[0][0] == '#':
        tokens = tokens[1:len(tokens)]
    else:
        return False

    if tokens[0] == '(':
        tokens = tokens[1:len(tokens)]
        x = lista_de_expressao(tokens)
        if x is not False:
            tokens = x
        else:
            return False

    if tokens[0] == ')':
        tokens = tokens[1:len(tokens)]
    else:
        return False

    return tokens


def comando_sem_rotulo(tokens):

    x = atribuicao(tokens)
    if x is not False:
        return x

    x = chamada_de_procedimento(tokens)
    if x is not False:
        return x

    x = comando_repetitivo(tokens)
    if x is not False:
        return x

    #<desvio>

    #<comando composto>

    #<comando condicional>

    #<comando repetitivo>

    return tokens


def comando(tokens):
    x = numero(tokens)
    if x is not False:
        tokens = x
        if tokens[0] == ':':
            tokens = tokens[1:len(tokens)]
        else:
            return False

    x = comando_sem_rotulo(tokens)

    if x is not False:
        tokens = x
    else:
        return False

    return tokens


#TODO : <comdando composto>
def comando_composto(tokens):

    if tokens[0] == 'begin':
        tokens = tokens[1:len(tokens)]

    x = comando(tokens)
    if x is not False:
        tokens = x
    else:
        return False

    while True:
        if tokens[0] == ';':
            tokens = tokens[1:len(tokens)]
            x = comando(tokens)
            if x is not False:
                tokens = x
            else:
                return False
        else:
            break




#TODO : <bloco>
def bloco(tokens):
    if tokens[0] == 'var':
        tokens = tokens[1:len(tokens)]
        tokens = pdv(tokens)


    x = comando_composto(tokens)
    if x is not False:
        tokens = x

    return tokens


#TODO : <program>
def program(tokens):
    if tokens[0] == 'program':
        tokens = tokens[1:len(tokens)]
    # <identificador>
    if tokens[0][0] == '#':
        tokens = tokens[1:len(tokens)]
    # (
    if tokens[0] == '(':
        tokens = tokens[1:len(tokens)]
        # <lista de identificadores>
    tokens = lid(tokens)
    # )
    if tokens[0] == ')':
        tokens = tokens[1:len(tokens)]

    if tokens[0] == ';':
        tokens = tokens[1:len(tokens)]

    tokens = bloco(tokens)

    return tokens


print(program(tokens))
