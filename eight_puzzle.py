'''
Eight Puzzle Problem

'''

from copy import deepcopy

class EightPuzzle:

    def __init__(self, initial_state, goal_state):
        self.state = initial_state
        self.goal = goal_state
        self.action = ['ml','mr','mu','md']
        global h2
            
    def check_goal(self):
        if self.state == self.goal:
            return True
        else:
            return False

    h1 = 0
    h2 = 0

    def heuristic1(self):
        global h1
        h1 = 0
        state = self.state.state
        for i in range(0,len(state)):
            for z in range(0,len(state)):
                if state[i][z] == self.state.goal[i][z]:
                    h1 = h1 + 1
        h1 = len(state)**2 - h1
        print ('Heuristic_1: ' + str(h1))
        return h1

    def heuristic2(self):
        state = self.state
        goal = self.goal
        h2=self.h2
        x_goal = 0
        y_goal = 0
        number = 0
        x_value = 0
        y_value = 0
        for i in range(0,len(state)):
            for z in range(0,len(state)):
                if state[i][z] != goal[i][z]:                        
                    number = state[i][z]
                    x_value=i
                    y_value=z
                    for x in range(0,len(state)):
                        for y in range(0,len(state)):
                            if number == 'e':
                                number == 'Null'
                                x_goal=x_value
                                y_goal=x_value
                                break
                            elif goal[x][y] == number:
                                x_goal=x
                                y_goal=y
                h2 = h2 + abs(x_value - x_goal) + abs(y_value - y_goal)
        print ('Heuristic_2: ' +str(h2))
        return h2


    def move(self, move):
        if move == 'ml': #move left
            dc = deepcopy(self)
            if dc.ml():
                return dc
        elif move == 'mr': #move right
            dc = deepcopy(self)
            if dc.mr():
                return dc
        if move == 'mu': #move up
            dc = deepcopy(self)
            if dc.mu():
                return dc
        elif move == 'md': #move down
            dc = deepcopy(self)
            if dc.md():
                return dc

    def ml(self):

        if (self.state[0][0] != 'e' and self.state[1][0] != 'e' and self.state[2][0] != 'e'):
            if ('e' in self.state[0]):
                if self.state[0][1] == 'e':
                    temp_val = self.state[0][0]
                    self.state[0][0] = self.state[0][1]
                    self.state[0][1] = temp_val
                elif self.state[0][2] == 'e':
                    temp_val = self.state[0][1]
                    self.state[0][1] = self.state[0][2]
                    self.state[0][2] = temp_val
            elif ('e' in self.state[1]):
                if self.state[1][1] == 'e':
                    temp_val = self.state[1][0]
                    self.state[1][0] = self.state[1][1]
                    self.state[1][1] = temp_val
                elif self.state[1][2] == 'e':
                    temp_val = self.state[1][1]
                    self.state[1][1] = self.state[1][2]
                    self.state[1][2] = temp_val
            else:
                if self.state[2][1] == 'e':
                    temp_val = self.state[2][0]
                    self.state[2][0] = self.state[2][1]
                    self.state[2][1] = temp_val
                elif self.state[2][2] == 'e':
                    temp_val = self.state[2][1]
                    self.state[2][1] = self.state[2][2]
                    self.state[2][2] = temp_val
            return True

    def mr(self):

        if (self.state[0][2] != 'e' and self.state[1][2] != 'e' and self.state[2][2] != 'e'):
            if ('e' in self.state[0]):
                if self.state[0][0] == 'e':
                    temp_val = self.state[0][1]
                    self.state[0][1] = self.state[0][0]
                    self.state[0][0] = temp_val
                elif self.state[0][1] == 'e':
                    temp_val = self.state[0][2]
                    self.state[0][2] = self.state[0][1]
                    self.state[0][1] = temp_val
            elif ('e' in self.state[1]):
                if self.state[1][0] == 'e':
                    temp_val = self.state[1][1]
                    self.state[1][1] = self.state[1][0]
                    self.state[1][0] = temp_val
                elif self.state[1][1] == 'e':
                    temp_val = self.state[1][2]
                    self.state[1][2] = self.state[1][1]
                    self.state[1][1] = temp_val
            else:
                if self.state[2][0] == 'e':
                    temp_val = self.state[2][1]
                    self.state[2][1] = self.state[2][0]
                    self.state[2][0] = temp_val
                elif self.state[2][1] == 'e':
                    temp_val = self.state[2][2]
                    self.state[2][2] = self.state[2][1]
                    self.state[2][1] = temp_val
            return True

    def mu(self):

        if ('e' not in self.state[0]):
            if ('e' in self.state[1]):
                if self.state[1][0] == 'e':
                    temp_val = self.state[0][0]
                    self.state[0][0] = self.state[1][0]
                    self.state[1][0] = temp_val
                elif self.state[1][1] == 'e':
                    temp_val = self.state[0][1]
                    self.state[0][1] = self.state[1][1]
                    self.state[1][1] = temp_val
                elif self.state[1][2] == 'e':
                    temp_val = self.state[0][2]
                    self.state[0][2] = self.state[1][2]
                    self.state[1][2] = temp_val
            elif ('e' in self.state[2]):
                if self.state[2][0] == 'e':
                    temp_val = self.state[1][0]
                    self.state[1][0] = self.state[2][0]
                    self.state[2][0] = temp_val
                elif self.state[2][1] == 'e':
                    temp_val = self.state[1][1]
                    self.state[1][1] = self.state[2][1]
                    self.state[2][1] = temp_val
                elif self.state[2][2] == 'e':
                    temp_val = self.state[1][2]
                    self.state[1][2] = self.state[2][2]
                    self.state[2][2] = temp_val
            return True

    def md(self):

        if ('e' not in self.state[2]):
            if ('e' in self.state[0]):
                if self.state[0][0] == 'e':
                    temp_val = self.state[1][0]
                    self.state[1][0] = self.state[0][0]
                    self.state[0][0] = temp_val
                elif self.state[0][1] == 'e':
                    temp_val = self.state[1][1]
                    self.state[1][1] = self.state[0][1]
                    self.state[0][1] = temp_val
                elif self.state[0][2] == 'e':
                    temp_val = self.state[1][2]
                    self.state[1][2] = self.state[0][2]
                    self.state[0][2] = temp_val
            elif ('e' in self.state[1]):
                if self.state[1][0] == 'e':
                    temp_val = self.state[2][0]
                    self.state[2][0] = self.state[1][0]
                    self.state[1][0] = temp_val
                elif self.state[1][1] == 'e':
                    temp_val = self.state[1][1]
                    self.state[1][1] = self.state[2][1]
                    self.state[2][1] = temp_val
                elif self.state[1][2] == 'e':
                    temp_val = self.state[1][2]
                    self.state[1][2] = self.state[2][2]
                    self.state[2][2] = temp_val
            return True


    def pretty_print(self):
        print('----------------------------')
        print(self.state[0])
        print(self.state[1])
        print(self.state[2])
        print('----------------------------')

