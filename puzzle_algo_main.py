from lab3 import Node
import numpy as np

test = np.array([1,2,3,8,6,4,7,5,0]).reshape(3,3)
easy = np.array([1,3,4,8,6,2,7,0,5]).reshape(3,3)
medium = np.array([2,8,1,0,4,3,7,6,5]).reshape(3,3)
hard = np.array([5,6,7,4,0,8,3,2,1]).reshape(3,3)

initial_state = easy
goal_state = np.array([0,1,2,3,4,5,6,7,8]).reshape(3,3)
print(initial_state,'\n')
print(goal_state)

root_node = Node(state=initial_state,parent=None,action=None,depth=0,step_cost=0,path_cost=0,heuristic_cost=0)

# search as far as possible along each branch before backtracking, using stack
root_node.best_first_search(goal_state)

root_node.print_path()
