import LexicalAnalyzer
import SyntaxTree

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


code = '''
program exemplo5 (input, output);
var n, k      : integer;
   f1, f2, f3 : integer;
'''

code1 = '''
program exemplo5(input, output,);
'''


tokens = LexicalAnalyzer.get_tokens(code)

program = SyntaxTree.program

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





