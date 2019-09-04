"""This class CommandExecutro violates the SRP and open close principle
"""

class CommandExecutor(object):
    def execute_command(self, args):
        # execute_command uses If, elif and else to dispatch helper methods
        if args[0] == "CreateOrder":
            self.create_order()
        elif  args[0] == "UpdateQuantity":
            self.update_quantity(args[1])
        elif  args[0] == "ShipOrder":
            self.ship_order()
        else:
            print("Unrecognized command: " + args[0])

    def create_order(self):
        pass
    
    def update_quatity(self, val):
        print (val)
        old_val = 5
        print("Logging updated quenatity from %s to %s" %(old_val, val))
    
    def shiporder(self):
        pass