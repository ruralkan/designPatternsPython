
[Discovered Problems](DiscoveredProblems.png)
This solution violate the single responsibility principle.     An  order should be about  who is ordering what. An order should probably not be concerned with how  the products will eventually be shipped, adding the shipper seems to go against the single responsibility principle.

There's also a violation of Open/ Close principle, since we would need to modify the shipping cost class to add new shipping method or shipper.

There's also a violation of the dependency inversion principle, since we are proggraming to a concrete class and method, the shippingCost class and its shipping_cost method.

Also shipping_cost method has a long list of  if/elif clouses that is a bit fragile and not very attractive