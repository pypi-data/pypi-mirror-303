"""
PYCOLS
funcs:
about -- information about your release
classes:
Fore -- font styling tools
Back -- background styling tools
Style -- Style changing tools
color -- all tools united with further features
"""
def about():
    """
    Returns information about your release and other projects by LK
    """
    return {"Version":(1, 0, 3), "Author":"Leander Kafemann", "date":"22.10.2024", "recommend":("Büro by LK",  "pyimager by LK", "naturalsize by LK"), "feedbackTo": "leander@kafemann.berlin"}

class Fore:
    """
    contains colors of your font
    """
    def __init__(self):
        self.CLIST = []
        csq = "\x1b[3{}m"
        for i in range(10):
            self.CLIST.append(csq.format(str(i)))
        self.NLIST = ["BLACK", "RED", "GREEN", "YELLOW", "BLUE", "MAGENTA", "CYAN", "WHITE", "NORMAL", "RESET"]
        self.LLIST = []
        self.LCLIST = []
        for i in range(8):
            self.LLIST.append("LIGHT_"+self.NLIST[i])
            self.LCLIST.append(self.CLIST[i].replace("[3", "[9"))
            
class Back(Fore):
    """
    contains background colors
    """
    def __init__(self):
        Fore.__init__(self)
        self.BCLIST = []
        self.BLCLIST = []
        for i in range(10):
            if i < 8:
                self.BLCLIST.append(self.LCLIST[i].replace("[9", "[10"))
            self.BCLIST.append(self.CLIST[i].replace("[3", "[4"))
            
class Style:
    """
    contains styles for font
    """
    def __init__(self):
        self.BRIGHT = '\x1b[1m'
        self.DIM = "\x1b[2m"
        self.RESET = "\x1b[22m"
        
class color(Style, Back):
    """
    contains all defined values
    funcs:
    col -- returns given colors code
    bcol -- ...background color...
    lcol -- lighter colors
    lbcol -- ...background colors...
    """
    def __init__(self):
        Style.__init__(self)
        Back.__init__(self)
        self.RESET_ALL = "\x1b[0m"
        import colorama
        colorama.init() #neccessary for initializing command codes in system shell
    def col(self, name: str = "BLACK"):
        """
        Gives back code of given color
        """
        return self.CLIST[self.NLIST.index(name)] if not "LIGHT_" in name else self.lcol(name)
    def bcol(self, name: str = "BLACK"):
        """
        ... background color ...
        """
        return self.BCLIST[self.NLIST.index(name)] if not "LIGHT_" in name else self.lbcol(name)
    def lcol(self, name: str = "BLACK"):
        """
        Method for lighter colors
        """
        return self.LCLIST[self.LLIST.index(name)]
    def lbcol(self, name: str = "BLACK"):
        """
        ... background colors ...
        """
        return self.BLCLIST[self.LLIST.index(name)]

