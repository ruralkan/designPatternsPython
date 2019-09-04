from before_strategy import Order, Shipper, ShippingCost

"""When its instantiated a new cost calculator (ex. cost_calculator = ShippingCost()),
we programming an implementation (the shippingCost() Object), not an abstraction. 
This violate the D principle in Solid"""

#Test federal Express Shipping

order = Order(Shipper.fedex)
#This is a implementation not an abstraction
cost_calculator = ShippingCost()
cost = cost_calculator.shipping_cost(order)
assert cost == 3.0


#Test UPS Shipping

order = Order(Shipper.ups)
cost_calculator = ShippingCost()
cost = cost_calculator.shipping_cost(order)
assert cost == 4.0

#Test Postal Service Shipping

order = Order(Shipper.postal)
cost_calculator = ShippingCost()
cost = cost_calculator.shipping_cost(order)
assert cost == 5.0

print('Test passed')