
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


program = SyntaxTree('root', [
    SyntaxTree('<program>'),
    SyntaxTree('<id>'),
    SyntaxTree('<(>'),
    SyntaxTree('<lid>'),
    SyntaxTree('<)>'),
    SyntaxTree('<;>'),
    SyntaxTree('<bloco>', [])
])

bloco = SyntaxTree('<bloco>', [])
