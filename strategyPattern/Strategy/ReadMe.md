To the implementation for our case, the context will be a ShippingCost Class, which uses an abstract base class called AbsStrategy, to exectue the various concrete stragies, one each for federal express, UPS and postal. Setting it up this way also makes it very to add new shippers since we would only add new concrete strategies, everything else remains the same.

[Strategy Pattern Structure](StrategyPattern_Structure.png)

Adventages with this pattern:

No more SOLID violations.
Each algorithm is separate, it is easy to test each one in isolation using simple calling code and objects designed to hit the corner case, it also easy to the outer code with deterministic mock algorithms
We haven't completly fixed the dependency inversion problem,. There is still a direct reference to an order object, it can be achived with Factory patter. 