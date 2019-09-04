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


In fact strategy pattern also helps with a similar class of problems, though it's not a good fit here, since each  helper method has a different signature.

Plus of Command pattern
The commands are encapsulated  in separate ConcreteCommand objects. Each one knows how to process its command, and that's all it needs to do. 
Note though, that the client does not pass in arguments to the execute method. Thath information is hidden and allows the Client to invoke any command without knowing any details. It's also easy to add new commands to the system. Just write new ConcreteCommands. Thath means we're following the Open/Closed principle.
