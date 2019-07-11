import re


def declaracao_funcao(tokens):
    if tokens[0] == 'function':
        tokens = tokens[1:len(tokens)]
    else:
        return False

    if tokens[0][0] == '#':
        tokens = tokens[1:len(tokens)]
    else:
        return False

    x = parametros_formais(tokens)
    if x is not False:
        tokens = x

    if tokens[0] == ':':
        tokens = tokens[1:len(tokens)]
    else:
        return False

    if tokens[0][0] == '#':
        tokens = tokens[1:len(tokens)]
    else:
        return False

    if tokens[0] == ';':
        tokens = tokens[1:len(tokens)]
    else:
        return False

    x = bloco(tokens)
    if x is not False:
        tokens = x
    else:
        return False

    return tokens

def parte_declaracao_sub_rotinas(tokens):
    x = declaracao_de_procedimento(tokens)
    if x is not False:
        tokens = x

        if tokens[0] == ';':
            tokens = tokens[1:len(tokens)]
        else:
            return False

        return tokens

    x = declaracao_funcao(tokens)
    if x is not False:
        tokens = x
    else:
        return False


    return tokens


def secao_parametros_formais(tokens):

    if tokens[0] == 'function':

        tokens = tokens[1:len(tokens)]
        x = lista_de_identificadores(tokens)
        if x is not False:
            tokens = x

        if tokens[0] == ':':
            tokens = tokens[1:len(tokens)]
        else:
            return False

        if tokens[0][0] == '#':
            tokens = tokens[1:len(tokens)]
        else:
            return False
    elif tokens[0] == 'procedure':
        tokens = tokens[1:len(tokens)]
        x = lista_de_identificadores(tokens)
        if x is not False:
            tokens = x
        else:
            return False
    elif tokens[0] == 'var':
        tokens = tokens[1:len(tokens)]
        x = lista_de_identificadores(tokens)
        if x is not False:
            tokens = x
            if tokens[0] == ':':
                tokens = tokens[1:len(tokens)]
            else:
                return False

            if tokens[0][0] == '#':
                tokens = tokens[1:len(tokens)]
            else:
                return False

        else:
            return False

    elif tokens[0][0] == '#':
        x = lista_de_identificadores(tokens)
        if x is not False:
            tokens = x
        else:
            return False

        if tokens[0] == ':':
            tokens = tokens[1:len(tokens)]
        else:
            return False

        if tokens[0][0] == '#':
            tokens = tokens[1:len(tokens)]
        else:
            return False


    return tokens






def parametros_formais(tokens):
    if tokens[0] == '(':
        tokens = tokens[1:len(tokens)]
    else:
        return False

    x = secao_parametros_formais(tokens)
    if x is not False:
        tokens = x
    else:
        return False

    while True:
        if tokens[0] == ';':
            tokens = tokens[1:len(tokens)]
            x = secao_parametros_formais(tokens)
            if x is not False:
                tokens = x
            else:
                return False

        else:
            break

    if tokens[0] == ')':
        tokens = tokens[1:len(tokens)]
    else:
        return False

    return tokens



def declaracao_de_procedimento(tokens):
    if tokens[0] == 'procedure':
        tokens = tokens[1:len(tokens)]
    else:
        return False

    #<identificador>
    if tokens[0][0] == '#':
        tokens = tokens[1:len(tokens)]
    else:
        return False

    x = parametros_formais(tokens)

    if x is not False:
        tokens = x

    if tokens[0] == ';':
        tokens = tokens[1:len(tokens)]
    else:
        return False

    x = bloco(tokens)
    if x is not False:
        tokens = x
    else:
        return False

    return tokens



def parte_declaracao_rotulos(tokens):
    if tokens[0] == 'label':
        tokens = tokens[1:len(tokens)]
    else:
        return False

    x = numero(tokens)
    if x is not False:
        tokens = x
    else:
        return False

    while True:
        if tokens[0] == ',':
            x = numero(tokens)
            if x is not False:
                tokens = x
            else:
                return False

        else:
            break

    if tokens[0] == ';':
        tokens = tokens[1:len(tokens)]
    else:
        return False

    return tokens


def parte_declaracao_tipo(tokens):
    if tokens[0] == 'type':
        tokens = tokens[1:len(tokens)]
    else:
        return False

    x = definicao_de_tipo(tokens)
    if x is not False:
        tokens = x
    else:
        return False

    return tokens


def definicao_de_tipo(tokens):
    if tokens[0][0] == '#':
        tokens = tokens[1:len(tokens)]
    else:
        return False

    if tokens[0] == '=':
        tokens = tokens[1:len(tokens)]
    else:
        return False

    x = tipo(tokens)
    if x is not False:
        tokens = x
    else:
        return False

    return tokens


def tipo(tokens):

    if tokens[0][0] == '#':
        tokens = tokens[1:len(tokens)]
    else:
        return False

    #TODO fazer array types
    return tokens







def desvios(tokens):
    if tokens[0] == 'goto':
        x = numero(tokens)
        if x is not False:
            return x
        else:
            return False
    else:
        return False



def comando_condicional(tokens):

    if tokens[0] == 'if':
        tokens = tokens[1:len(tokens)]
    else:
        return False

    x = expressao(tokens)
    if x is not False:
        tokens = x
    else:
        return False

    if tokens[0] == 'then':
        tokens = tokens[1:len(tokens)]
    else:
        return False

    x = comando_sem_rotulo(tokens)
    if x is not False:
        tokens = x
    else:
        return False

    if tokens[0] == 'else':
        tokens = tokens[1:len(tokens)]
        x = comando_sem_rotulo(tokens)
        if x is not False:
            tokens = x
        else:
            return False

    return tokens



def relacao(tokens):

    if tokens[0] == '<' and tokens[1] == '=':
        return tokens[2:len(tokens)]
    elif tokens[0] == '>' and tokens[1] == '=':
        return tokens[2:len(tokens)]
    elif tokens[0] == '<' and tokens[1] == '>':
        return tokens[2:len(tokens)]
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
def lista_de_identificadores(token):
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
def parte_declaracao_variaveis(tokens):

    if tokens[0] == 'var':
        tokens = tokens[1:len(tokens)]
    else:
        return False

    x = lista_de_identificadores(tokens)
    if x is not False:
        tokens = x
    else:
        return False

    if tokens[0] == ':':
        tokens = tokens[1:len(tokens)]
    else:
        return False

    x = tipo(tokens)
    if x is not False:
        tokens = x
    else:
        return False

    if tokens[0] == ';':
        tokens = tokens[1:len(tokens)]
    else:
        return False

    while True:
        x = lista_de_identificadores(tokens)
        if x[0] == ':':
            x = x[1:len(x)]
            x = tipo(x)
            if x is not False:
                tokens = x
                if tokens[0] == ';':
                    tokens = tokens[1:len(tokens)]
                else:
                    return False
            else:
                return False
        else:
            break


    return tokens


def variavel(tokens):

    if tokens[0][0] == '#':
        return tokens[1:len(tokens)]
    else:
        return False


def chamada_de_funcao(tokens):
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


def fator(tokens):

    x = variavel(tokens)
    if x is not False:
        return x

    x = numero(tokens)
    if x is not False:
        return x

    x = chamada_de_funcao(tokens)
    if x is not False:
        return x

    if tokens[0] == '(':
        tokens = tokens[1:len(tokens)]
        x = expressao(tokens)
        if x is not False:
            tokens = x
        else:
            return False

        if tokens[0] == ')':
           tokens = tokens[1:len(tokens)]
        else:
            return False

        return tokens
    else:
        return False



def termo(tokens):

    x = fator(tokens)
    if x is not False:
        tokens = x
    else:
        return False

    while True:
        if tokens[0] == '*' or tokens[0] == 'div' or tokens[0] == 'and':
            tokens = tokens[1:len(tokens)]
            x = fator(tokens)
            if x is not False:
                tokens = x

            else:
                return False
        else:
            break

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
        x = termo(tokens)
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
            tokens = tokens[1:len(tokens)]
            x = expressao(tokens)
            if x is not False:
                tokens = x
            else:
                return False
        else:
            break

    return tokens




#TODO problema aqui

def atribuicao(tokens):

    x = variavel(tokens)
    if x is not False:
        tokens = x

    if tokens[0] == ':' and tokens[1] == '=':
        tokens = tokens[2:len(tokens)]
    else:
        return False

    x = expressao(tokens)
    if x is not False:
        tokens = x
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

    x = desvios(tokens)
    if x is not False:
        return x

    x = comando_condicional(tokens)
    if x is not False:
        return x

    x = comando_repetitivo(tokens)
    if x is not False:
        return x

    x = comando_composto(tokens)
    if x is not False:
        return x

#TODO : Problema aqui
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
    else:
        return False

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

    if tokens[0] == 'end':
        tokens = tokens[1:len(tokens)]
    else:
        return False

    return tokens



#TODO : <bloco>
def bloco(tokens):

    x = parte_declaracao_variaveis(tokens)
    if x is not False:
        tokens = x


    x = parte_declaracao_tipo(tokens)
    if x is not False:
        tokens = x

    x = parte_declaracao_rotulos(tokens)
    if x is not False:
        tokens = x

    x = parte_declaracao_sub_rotinas(tokens)
    if x is not False:
        tokens = x


    x = comando_composto(tokens)
    if x is not False:
        tokens = x

    return tokens


#TODO : <program>
def program(tokens):
    if tokens[0] == 'program':
        tokens = tokens[1:len(tokens)]
    else:
        return False

    if tokens[0][0] == '#':
        tokens = tokens[1:len(tokens)]
    else:
        return False

    if tokens[0] == '(':
        tokens = tokens[1:len(tokens)]
    else:
        return False

    tokens = lista_de_identificadores(tokens)

    if tokens[0] == ')':
        tokens = tokens[1:len(tokens)]
    else:
        return False

    if tokens[0] == ';':
        tokens = tokens[1:len(tokens)]
    else:
        return False

    tokens = bloco(tokens)

    if tokens[0] == '.':
        pass
    else:
        return False

    return tokens
