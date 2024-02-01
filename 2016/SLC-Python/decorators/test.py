# Simple example ##############################################################
def italic(text_func):
    def italicize(*a, **kw):
        return '<i>{}</i>'.format(text_func(*a, **kw))
    return italicize

def format_text(text):
    return text

format_text = italic(format_text)
format_text('Learning Decorators')


# Decorator sandwich ##########################################################
# https://stackoverflow.com/a/1594484
def bread(func):
    def wrapper():
        print('<======>')
        func()
        print('<======>')
    return wrapper

def vegetables(func):
    def wrapper():
        print('#tomatoes#')
        func()
        print('~leaves~')
    return wrapper

@vegetables
@bread
def sandwich(food='bean-product'):
    print(food)

sandwich()


# Property ####################################################################
# https://docs.python.org/3/library/functions.html#property
class C:
    def __init__(self):
        self._x = None

    def getx(self):
        return self._x

    def setx(self, value):
        self._x = value

    def delx(self):
        del self._x

    x = property(getx, setx, delx, "I'm the 'x' property.")

class D:
    def __init__(self):
        self._x = None

    @property
    def x(self):
        """I'm the 'x' property."""
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @x.deleter
    def x(self):
        del self._x
