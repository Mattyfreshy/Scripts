import random
from enum import Enum

# Enum to store information about every command
class inputs(Enum):
    roll = "Roll a Dice"
    
# Function to handle responses
def handle_responses(message) -> str:
    p_message = message.lower()
    
    if p_message == 'hello':
        return 'Howdy!'
    
    if p_message == 'roll':
        return str(random.randint(1,6))    
    
    return 'Message not handled'
