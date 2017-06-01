import numpy as np
import pdb

# R matrix
R = np.matrix([
        [-1,0,-1,-1,-1,-1],
        [0,0,0,0,0,-1],
        [-1,0,-1,-1,-1,-1],
        [-1,0,-1,-1,-1,100],
        [-1,0,-1,-1,-1,100],
        [-1,-1,-1,0,0,100] ])

# Q matrix
Q = np.matrix(np.zeros([6,6]))

# Find possible actions.
# Return all R matrix values greater than equal to 0
def get_available_actions(state):
    current_state = R[state]
    
    # Return all values not -1
    available_actions = np.where(current_state >= 0)[1]
    return available_actions

def choose_random_action(available_actions):
    next_action = np.random.choice(available_actions, 1)
    return next_action


for _ in range(1000):
    while (True):
        #pdb.set_trace()


        initial_state = np.random.choice(6, 1)

        available_actions = get_available_actions(initial_state)

        next_action = choose_random_action(available_actions)


        #print(next_action)

        next_states = get_available_actions(next_action)

        #print(Q[5,next_states])

        Q[initial_state, next_action] = R[initial_state, next_action] + ( 0.8 * np.max(Q[next_action,next_states]))

        if next_action == 5:
            break

Q = Q / np.max(Q) * 100
print(Q)



## Test

current_state = 0
print("\nStarting at: ",current_state)

while current_state != 5:
    #pdb.set_trace()
    #print(current_state)
    next_step = np.argmax(Q[current_state])
    print("\n Next Step: ",next_step)

    current_state = next_step

current_state = 2
print("\nStarting at: ",current_state)

while current_state != 5:
    #pdb.set_trace()
    #print(current_state)
    next_step = np.argmax(Q[current_state])
    print("\n Next Step: ",next_step)

    current_state = next_step

current_state = 4
print("\nStarting at: ",current_state)

while current_state != 5:
    #pdb.set_trace()
    #print(current_state)
    next_step = np.argmax(Q[current_state])
    print("\n Next Step: ",next_step)

    current_state = next_step
