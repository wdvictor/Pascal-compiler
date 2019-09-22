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


code = '''program exemplo5 (input, output);
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

code1 = '''
program exemplo5(input, output,);
'''


tokens = LexicalAnalyzer.get_tokens(code)

program = SyntaxTree.program


def check(object, token):
    try:
        if object.name == token[0]:
            return 1
        elif object.name == '<id>':
            return 2
        elif object.name == '<lid>':
            return 3
        elif object.name == '<dv>':
            return 4
        elif object.name == '[pdv]':
            if token[0] == '<var>':
                return 5
        elif len(object.children) != 0:
            for i in range(len(object.children)):
                x = check(object.children[i], token)
                if x == 1:
                    token = token[1:len(token)]
                elif x == 2:
                    SyntaxTree.identifiers.append(token[0])
                    token = token[1:len(token)]
                elif x == 3:
                    token = SyntaxTree.lid(token)
                elif x == 4:
                    token = SyntaxTree.pdv(token)
                elif x == 5:
                    token = token[1:len(token)] #consome o <var>
                    token = SyntaxTree.pdv(token)

        else:
            print('Error: expected {}'.format(object.name))
            exit(0)
    except IndexError:
        print('Missing arguments {}'.format(object.name))





check(program, tokens)
print('ok')





