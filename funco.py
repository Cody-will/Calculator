# Separates the values and operators, so they can be worked with separately.

class Separate:
    def __init__(self, *args):
        self.args = args
        self.a = ''
        self.b = ''
        self.mods = ''
        self.separator()

    def separator(self):
        if len(self.args) == 1:
            self.a = str(self.args[0])
        elif len(self.args) == 2:
            self.a = str(self.args[0])
            self.mods = str(self.args[1])
        elif len(self.args) == 3:
            self.a = str(self.args[0])
            self.b = str(self.args[2])
            self.mods = str(self.args[1])



# Joins together the numbers and symbols, so they can be calculated using eval.


class Joiner:

    def the_joining(self, a, b, mods):
        a = str(a)
        b = str(b)
        mods = str(mods)
        return str(a + mods + b)


class Commas:

    def remove(self, *args):
        pass

    def add(self, *args):
        pass

