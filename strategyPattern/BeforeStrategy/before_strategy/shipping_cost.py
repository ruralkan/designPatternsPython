"""This violates the Open/Close principle and Dependency Inversion principle,
 the last because the shippingCost class is the shippingCost method
 """

from before_strategy import Shipper

class ShippingCost(object):

    def shipping_cost(self, order):
        """This method computes the cost according to the shippers stored in the order
        if the shipper is not one of those the method is programmed to handle.
        for each shipper this method calls a private helper method to get the actual cost.
        If a new shipper is added, we have to modify this calss, 
        adding a new elif condition and anew helper method. This violate the open close principle
        """
        if order.shipper == Shipper.fedex:
            return self._fedex_cost(order)
        elif order.shipper == Shipper.ups:
            return self._ups_cost(order)
        elif order.shipper == Shipper.postal:
            return self._postal_cost(order)
        else:
            raise ValueError('Invalid shipper %s', order.shipper)
    
    def _fedex_cost(self, order):
        return 3.00
    
    def _ups_cost(self, order):
        return 4.00
    
    def _postal_cost(self, order):
        return 5.00