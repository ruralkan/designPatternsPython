
class Order(object):
    def __init__(self, items):
        self._items = items
    
    @property
    def container(self):
        return self._items
        