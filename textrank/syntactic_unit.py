
class SyntacticUnit(object):

    def __init__(self, text, token=None, tag=None):
        self.text = text
        self.token = token
        if tag:
            self.tag = tag[:2] # just first two letters of tag
        self.index = -1
        self.score = -1

    def __str__(self):
        return "Original unit: '" + self.text + "' *-*-*-* " + "Processed unit: '" + self.token + "'"

    def __repr__(self):
        return str(self)