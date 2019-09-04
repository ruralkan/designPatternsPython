from strategy import Order, ShippingCost
from strategy import FedExStrategy, PostalStrategy, UPSStrategy

#Test federal exprass shipping
order = Order("papas")
strategy = FedExStrategy()
cost_calculator = ShippingCost(strategy)
cost = cost_calculator.shipping_cost_calc(order)
print(order.container)
assert cost == 3.0

#Test UPS shipping
order = Order("papas")
strategy =UPSStrategy()
cost_calculator = ShippingCost(strategy)
cost = cost_calculator.shipping_cost_calc(order)
assert cost == 4.0
#Test Postal Service shipping
order = Order("papas")
strategy = PostalStrategy()
cost_calculator = ShippingCost(strategy)
cost = cost_calculator.shipping_cost_calc(order)
assert cost == 5.0

print("Test passed")