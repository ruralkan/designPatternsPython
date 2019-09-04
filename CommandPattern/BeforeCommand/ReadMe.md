This implementation violates single responsibility principle, CommandExecturo class parses commands, and then processes them, these concerns should be separate.

The class also violates the open close principle, since if we would to change it to add new commands or change or remove existing ones
The main program also violates the Dependency inversion principle, since it dependes upon the implementation of the ExecuteCommand method in the CommandExecturo class.
 The long list of if, elif, and else makes a bit fragile and a little hard on the eyes