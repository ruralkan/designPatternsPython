The singleton pattern is useful when you need to control access to class instances. 
Classification Creational
Used to create just one object. Singleton can be used to ensure that a class has only one instance. This is handy whem you want to control access to limited resources such a hardware devices, a set of budder pools or perhaps connection pools for a web client or database access.
Singleton also provides a global point of access for its one instance, and is responsible for creating that instance.
Singleton can also provide for lazy instantiation, which can be important if the object is costly to instanciate or not always be used
