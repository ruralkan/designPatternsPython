This is the structure of the command pattern in UML diagram.
[Command Pattern Structure](CommandPattern_structure.png)

The client, this is the part that wants to get something done. For the command line order processor, that would be you or me sitting at the keyboard. For some app with lot of bells and whistles, the app itself is the Client.

Invoker, this component asks the command to perform a request. In the command line order system, this is the main program

Concrete command, it knows how to perform the action requested, and may enlist the help of a Receiver object, or may go it alone, if the action is simple enough. In the command line order system there should be a concreteCommand for every command in the system. 

The receiver, could be a separate object or just a method in the ConcreteClass, depeding on the complexity. The ConcreteCommand fully encapsulate the command so that the client is not longer concerned with the particulars.

The undo method is optional, though it is frequently found in many apps. 