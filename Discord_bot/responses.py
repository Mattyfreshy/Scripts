import random
from enum import Enum

# Enum to store information about every command
class Inputs(Enum):
    roll = "Roll a Dice"
    
# Function to handle responses
def handle_responses(message) -> str:
    p_message = message.lower()
    
    if p_message == 'hello':
        return 'Howdy!'
    
    if p_message == 'roll':
        return str(random.randint(1,6))   
    
    if p_message == "help":
        # generate list of commands w/ corrosponding information.
        help_lst = ['Below is a list of commands: \n']
        for i in Inputs:
            help_lst.append(i.name + ': ' + i.value)
            
        return '\n'.join(help_lst)
    
    return 'Message not handled'
