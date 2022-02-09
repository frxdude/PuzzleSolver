import numpy as np
import time
from queue import Queue

randomPuzzle = []
cols, rows = 3, 3
# start_point = 0
i = 0
for x in range(0, cols):
    row = []
    for y in range(0, rows):
        i = i + 1
        row.append(i)
    np.random.shuffle(row)
    randomPuzzle.append(row)

np.random.shuffle(randomPuzzle)


# position 0 is i
# position 1 is j
class Node:
    def __init__(self, initPuzzle, parent, action, position):
        self.puzzle = initPuzzle
        self.initPuzzle = initPuzzle
        self.parent = parent
        self.action = action
        self.position = position
        # dood node
        self.moveUp = None
        self.moveLeft = None
        self.moveDown = None
        self.moveRight = None

    def move_down(self):
        if self.position[0] == 2:
            return False
        else:
            return True

    def move_up(self):
        if self.position[0] == 0:
            return False
        else:
            return True

    def move_right(self):
        if self.position[1] == 2:
            return False
        else:
            return True

    def move_left(self):
        if self.position[1] == 0:
            return False
        else:
            return True

    def print(self):
        for x in range(0, cols):
            print(node.initPuzzle[x])

    def solve(self, goal_state):
        print("current pos : ", self.position[0], self.position[1])
        done = []
        queue = [self]
        while queue:
            current_node = queue.pop(0)
            print(done)
            if np.array_equal(current_node.initPuzzle, goal_state):
                print("------- SOLVED --------")
                current_node.print()
                return True
            if current_node.position not in done:
                if current_node.move_up():
                    print("deesh")
                    oldPos = current_node.position[0]
                    current_node.position[0] = current_node.position[0] - 1
                    tempNode = current_node.puzzle[oldPos][current_node.position[1]]
                    tempPuzzle = current_node.puzzle.copy()
                    tempPuzzle[oldPos][current_node.position[1]] = tempPuzzle[current_node.position[0]][
                        current_node.position[1]]
                    tempPuzzle[current_node.position[0]][current_node.position[1]] = tempNode

                    current_node.moveUp = Node(initPuzzle=tempPuzzle, parent=current_node, action='deesh',
                                               position=current_node.position)
                    queue.append(current_node.moveUp)
                    if goal_state[current_node.position[0]][current_node.position[1]] == \
                            current_node.initPuzzle[current_node.position[0]][current_node.position[1]]:
                        done.append(current_node.position)
                    current_node.print()
                if current_node.move_right():
                    print("baruun")
                    oldPos = current_node.position[1]
                    current_node.position[1] = current_node.position[1] + 1
                    tempNode = current_node.puzzle[current_node.position[0]][oldPos]
                    tempPuzzle = current_node.puzzle.copy()
                    tempPuzzle[current_node.position[0]][oldPos] = tempPuzzle[current_node.position[0]][
                        current_node.position[1]]
                    tempPuzzle[current_node.position[0]][current_node.position[1]] = tempNode

                    current_node.moveRight = Node(initPuzzle=tempPuzzle, parent=current_node, action='baruun',
                                                  position=current_node.position)
                    queue.append(current_node.moveRight)
                    if goal_state[current_node.position[0]][current_node.position[1]] == \
                            current_node.initPuzzle[current_node.position[0]][current_node.position[1]]:
                        done.append(current_node.position)
                    current_node.print()
                if current_node.move_left():
                    print("zuun")
                    oldPos = current_node.position[1]
                    current_node.position[1] = current_node.position[1] - 1
                    tempNode = current_node.puzzle[current_node.position[0]][oldPos]
                    tempPuzzle = current_node.puzzle.copy()
                    tempPuzzle[current_node.position[0]][oldPos] = tempPuzzle[current_node.position[0]][
                        current_node.position[1]]
                    tempPuzzle[current_node.position[0]][current_node.position[1]] = tempNode

                    current_node.moveLeft = Node(initPuzzle=tempPuzzle, parent=current_node, action='zuun',
                                                 position=current_node.position)
                    queue.append(current_node.moveLeft)
                    if goal_state[current_node.position[0]][current_node.position[1]] == \
                            current_node.initPuzzle[current_node.position[0]][current_node.position[1]]:
                        done.append(current_node.position)
                    current_node.print()
                if current_node.move_down():
                    print("doosh")
                    oldPos = current_node.position[0]
                    current_node.position[0] = current_node.position[0] + 1
                    tempNode = current_node.puzzle[oldPos][current_node.position[1]]
                    tempPuzzle = current_node.puzzle.copy()
                    tempPuzzle[oldPos][current_node.position[1]] = tempPuzzle[current_node.position[0]][
                        current_node.position[1]]
                    tempPuzzle[current_node.position[0]][current_node.position[1]] = tempNode

                    current_node.moveDown = Node(initPuzzle=tempPuzzle, parent=current_node, action='doosh',
                                                 position=current_node.position)
                    queue.append(current_node.moveDown)
                    if goal_state[current_node.position[0]][current_node.position[1]] == \
                            current_node.initPuzzle[current_node.position[0]][current_node.position[1]]:
                        done.append(current_node.position)
                    current_node.print()

            # print("my pos data : ", self.puzzle[self.position[1]][self.position[0]])
        # while current_node:
        #     if np.array_equal(current_node.state, goal_state):
        #         print("hi")
        #         return True


node = Node(initPuzzle=randomPuzzle, parent=None, action=None, position=[1, 1])
goal = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
node.solve(goal_state=goal)
