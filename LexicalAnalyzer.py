



keywords = ['program', 'label', 'type', 'array', 'of', 'var', 'procedure'
                    ,'function', 'begin', 'end', 'if', 'then', 'else', 'while', 'do'
                    , 'or', 'and', 'div', 'not']


symbols = ['.', ';', ',', '(', ')', ':', '=',
           '<', '>', '+', '-', '*', '[', ':=', '..']



def get_tokens(code):
    label = ''
    tokens = []
    for str in code:
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
    return tokens

