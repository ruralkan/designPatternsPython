import types


class Strategy(object):

    def __init__(self, func=None):
        if func is not None:
            #the types module you can convert a normal function into a bound method, namely a function that contains a reference to the instance it is bound to.
            # take a function, bind it to this instance, and replace the default bound method 'execute' with this new bound method.
            self.execute = types.MethodType(func, self)
            self.name = '{}_{}'.format(self.__class__.__name__, func.__name__)
        else:
            self.name = '{}_default'.format(self.__class__.__name__)

    def execute(self):
        print('Default method')
        print('{}\n'.format(self.name))


"""Let’s define a couple of replacement strategies for the default method execute.
Don’t mind the self parameter, for now these ones are just regular functions. 
I decided to use self because I know that these functions, passed to the Strategy’s __init__ method, will be bound to an instance of Strategy (this is done when the line types.MethodType(func, self) is executed)."""
def execute_replacement1(self):
    print('Replacement1 method')
    print('{}\n'.format(self.name))


def execute_replacement2(self):
    print('Replacement2 method')
    print('{}\n'.format(self.name))


#Select a strategy at runtime
def main():
    
    s0 = Strategy()
    s0.execute()

    s1 = Strategy(execute_replacement1)
    s1.execute()

    s2 = Strategy(execute_replacement2)
    s2.execute()

if __name__ == '__main__':
    main()