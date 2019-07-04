
class SyntaxTree(object):

    def add_child(self, node):
        assert isinstance(node, SyntaxTree)
        self.children.append(node)

    def __init__(self, name='root', children=None):
        self.name = name
        self.children = []
        if children is not None:
            for child in children:
                self.add_child(child)

#Comando Composto(cc)
cc = SyntaxTree('<begin>', [
    SyntaxTree('<comando>'),
    SyntaxTree('<end>')
])


#parte de declaração de variáveis (PDV)
pdv = SyntaxTree('[pdv]', [
    SyntaxTree('<var>'),
    SyntaxTree('<dv>')
])




program = SyntaxTree('root', [
    SyntaxTree('<program>'),
    SyntaxTree('<id>'),
    SyntaxTree('<(>'),
    SyntaxTree('<lid>'),
    SyntaxTree('<)>'),
    SyntaxTree('<;>'),
    SyntaxTree('<bloco>', [pdv, cc , SyntaxTree('.')])
])



identifiers = []


#lista de identificadores(LID)
def lid(token):

    for i in range(len(token)):
        if token[i][0] == '#' and token[i][-1] == '#':
            identifiers.append(i)
            continue
        elif token[i] == '<,>' and i != 0 and token[i+1][0] == '#' and token[i+1][-1] == '#':
            #i != 0 para evitar erros do tipo : ", n1 , n2"
            #tokens[i+1][0]: verifica se o proximo token é um identificador, para evitar erros do tipo "n1 , "
            continue
        else:
            return token[i:len(token)]


#parte de declaração de variáveis(DV)
def pdv(token):
    token = lid(token)
    #pegar os tipos
    if token[0] == '<:>':
        if token[1][0] == '#': #se o proximo for um identificador
            if token[2] == '<;>': # verifica o ponto e vírgula
                if token[3][0] == "#": #se tiver um identicador depois do ponto e vírgula, entra em recursividade
                    return pdv(token[3:len(token)])
                else:
                    return token[3:len(token)]       #Se não continua o parser






