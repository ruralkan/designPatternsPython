class Singleton(object):
    ans = None

    @staticmethod
    def instance():
        if '_instance' not in Singleton.__dict__:
            Singleton._instance = Singleton()
        return Singleton._instace
    
s1 = Singleton.instance()
s2 = Singleton.instance()

assert s1 is s2

s1.ans = 42

s1.ans = s2.ans
print('assertion passed')