import re
# import sys
#
# try:
#     sys.argv[1]
#     file = open(sys.argv[1], 'r')
# except:
#     print('No file in directory')
#     exit(1)
#
# code = file.read()

keywords = ['program', 'label', 'type', 'array', 'of', 'var', 'procedure'
                    ,'function', 'begin', 'end', 'if', 'then', 'else', 'while', 'do'
                    , 'or', 'and', 'div', 'not']


symbols = ['.', ';', ',', '(', ')', ':', '=',
           '<', '>', '+', '-', '*', '[', ':=', '..']


class SyntaxTree(object):

    def add_child(self, node):
        #assert if the node argument it's a SyntaxTree object
        assert isinstance(node, SyntaxTree)
        self.children.append(node)

    def __init__(self, name='root', children=None):
        self.name = name
        self.children = []
        if children is not None:
            for child in children:
                self.add_child(child)


##function to read the notes in the tree
# def check(object):
#     print(object.name)
#     if len(object.children) != 0:
#         for i in range(len(object.children)):
#             check(object.children[i])
#     else:
#         pass
#


code = '''
program exemplo5 (input, output);
var n, k      : integer;
   f1, f2, f3 : integer;
'''

code1 = '''
program exemplo5(input, output,);
'''
tokens = []

label = ''
for str in code1:
    if str in symbols:
        if label in keywords:
            tokens.append('<' + label + '>')
            tokens.append('<' + str + '>')
            label = ''
        else:
            if label is not '': tokens.append('#' + label + '#')
            tokens.append('<' + str + '>')
            label = ''
    elif str is ' ' or str is'\t' or str is '\n':
        if label in keywords:
            if label is not '' : tokens.append('<' + label + '>')
            label = ''
        else:
            if label is not '':
                tokens.append('#' + label + '#')
            label = ''
    else:
        label += str


#print(tokens)


program = SyntaxTree('root', [
    SyntaxTree('<program>'),
    SyntaxTree('<id>'),
    SyntaxTree('<(>'),
    SyntaxTree('<lid>'),
    SyntaxTree('<)>'),
    SyntaxTree('<;>'),
    SyntaxTree('<bloco>', [])
])


identifiers = []


def lid(token):

    for i in range(len(token)):
        if token[i][0] == '#' and token[i][-1] == '#':
            identifiers.append(i)
            continue
        elif token[i] == '<,>' and i != 0 and token[i+1][0] == '#' and token[i+1][-1] == '#':
            continue
        else:
            return token[i:len(token)]



def check(object, token):
    try:
        if object.name == token[0]:
            return 1
        elif object.name == '<id>':
            return 2
        elif object.name == '<lid>':
            return 3
        elif len(object.children) != 0:
            for i in range(len(object.children)):
                x = check(object.children[i], token)
                if x == 1:
                    token = token[1:len(token)]
                elif x == 2:
                    identifiers.append(token[0])
                    token = token[1:len(token)]
                elif x == 3:
                    token = lid(token)
        else:
            print('Error: expected {}'.format(object.name))
            exit(1)
    except IndexError:
        print('Missing arguments {}'.format(object.name))


#check function is working from correct tokens, but we need to create a
#form to raise a problem if the tokens are wrong


check(program, tokens)
print('ok')





