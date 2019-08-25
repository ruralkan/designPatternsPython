The command pattern is find in toolkits, command-line programs, GUI menus, in fact, just about anywhere you want a simple way to corral diverse request processing objects into a common structure

Classsification: Behavioral
It's used to control the operations of some object.
The pattern provides a way to encapsulate a request as an object, this is in line with the principle encapsulate what varies, and this encapsulation lets you parametrize various objects with different request. 
The command pattern also provides a simple way to support queues and log operations, perhaps to updating a database or creating an audit trail of  requests.
Using the command pattern, we can bacon support for undoable operations and macros, that is sequences of commands. 

Sometimes, this pattern is also know as the Action Pattern or the transaction pattern

Example:
Command line oreder processing program
Support three  operations:
- CreateOrder
- UpdateQuantity
- ShipOrder

Should:
- parse the command line arguments
- Execute the command
- Notify user and log the results
