import sys
from commad_executor import CommandExecutor
"""__main__.py violates dependency inversion principle since 
it depends upon the implementation of the ExecuteCommand method
 in the CommandExecutor class.
"""
if len(sys.argv) < 2:
    print("Usage -m BeforeCommand <command>")
    print("Commands:")
    print(" CreateOrder")
    print(" UpdateQuantity number")
    print(" ShipOrder")
    exit()

executor = CommandExecutor()
executor.execute_command(sys.argv[1:])