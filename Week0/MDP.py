# This program simulates a simple MDP

import numpy as np
import random


# define a "state" class
# which consists of its name, reward, and a list of possible actions from this state
class State:
    def __init__(self, name,actions):
        self.name = name
        self.actions = actions
    
    def __str__(self):
        return self.name
    
    

if __name__ == "__main__":
    # Define 3 states Cool, Warm and Overheated
    # and possible actions from each state

    # Cool
    Cool = State("Cool", ["Fast", "Slow"])

    # Warm
    Warm = State("Warm", ["Fast", "Slow"])

    # Overheated
    Overheated = State("Overheated", [])


    # Take Input as strings of actions each on a new line
    # We start from Cool state.

    # Initialize the current state to Cool
    current_state = Cool

    # Initialize the total reward to 0
    total_reward = 0

    # Initialize the list of states visited to empty
    states_visited = []

    # Read the input
    # First line is the number of actions
    num_actions = int(input())
    actions = []

    # Read the actions
    for i in range(num_actions):
        actions.append(input())

    print(actions)

    # Iterate over the actions
    for action in actions:
        # Check if the action is valid
        if total_reward>20:
            print("Reached")
            break
        if action not in current_state.actions:
            print("Invalid action")
            break

        # Add the current state to the list of states visited
        states_visited.append(current_state)

        print(current_state)


        # Update the current state
        if current_state.name == "Cool":
            if action == "Fast":
                chance=np.random.randint(0,2)
                if chance==0:
                    current_state=Warm
                else:
                    current_state=Cool
                total_reward+=2
            elif action == "Slow":
                current_state = Cool
                total_reward+=1;
            else:
                print("Invalid action")
                break
        elif current_state.name == "Warm":
            if action == "Fast":
                print(Overheated)
                current_state=Overheated
                break
            elif action == "Slow":
                chance=np.random.randint(0,2)
                if chance==0:
                    current_state=Warm
                else:
                    current_state=Cool
                total_reward+=0.5
            
            else:
                print("Invalid action")
                break
      
    if total_reward<=20 and current_state!=Overheated:
        print("Halted Midway")
