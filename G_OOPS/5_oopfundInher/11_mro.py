#method resolution order
class Top:
    def m_top(self):
        print("top")

class Middle(Top):
    def m_middle(self):
        print("middle")

class Bottom(Top, Middle):
    def m_bottom(self):
        print("bottom")

object = Bottom()
#TypeError it should be Middle ,Top to be valid