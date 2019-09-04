The strategy pattern is classified like a Beheavioral pattern, so it is use to control the operation of some object, in this case, the patter provides a way to take a family of algorithms, encapsulate each one and make them interchangeable with each other.

Since the algorithm form a family, they will normally operate with the same set of inputs and outputs. This is often accomplished by passing in some common object as input.

The algorithms are allowed to vary independently and their implementation can be quite different. Consider the differences between calculating gravitational attraction using Newton's formula as opposed to Einstain's  general relativity, very different, yet both have the same inputs and outputs

Some times the strategy pattern is called the Policy pattern, reflecting its use in applying some sort of policy to the behavior of a software system.

Example:
Shipping cost calculator

Must support: 
- Federal Express
- UPS
- Postal Service
- Must be extendable (add new shippers)


This UML diagram shows the structure of the Strategy pattern. Within some context, we have an interface, which is an abstract base class in Python terms that is common to all the supported algorithms.

The context uses this interface to call the various algorithms defined by the concrete strategies that implement the base class. Each concrete strategy implementation, taks the same inputs and returns the same type of outputs, but is free to do so as the algorith being implemented dictates.

[Strategy Pattern Structure](StrategyPattern_Structure.png)



