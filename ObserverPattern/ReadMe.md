It's a heavily ised for event monitoring
Classification: Behavioral
So it used to control the operation of some object
The pattern provides a way to define a one-to-many relationship between a set of objects, so that when the state of one object changes, all its dependent objects are notified
This pattern is also knows as DEPENDENT PATTERN or PUBLISH- SUBSCRIBE pattern


From the UML doagram:
First there is an abstract subject, that contains the required methods attach, detach and notify
We have the abstract observer with its one required method update.
The concrete subject implements the required methods, attach, detach and notify, commonly it also implements getState method for observers to use to obtain the subject state when it change, the concrete observer implements the update method. now when the subject's state changes, it loops  through all currently attached observers and calls theri update metods, when called, the observer's update methods callthe subject's getState method to acquire the changes, in response, the subject returns the state requested