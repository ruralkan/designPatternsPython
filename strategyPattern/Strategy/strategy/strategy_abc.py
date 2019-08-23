from abc import ABCMeta, abstractmethod

class AbsStrategy(object):
    __metaclass_ = ABCMeta

    @abstractmethod
    def calculate(self, order):
        """Calculate shipping cost"""
    
    