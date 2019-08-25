import abc

class AbsOcrederCommand(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod 
    def name(self):
        pass

    @abc.abstractmethod 
    def description(self):
        pass