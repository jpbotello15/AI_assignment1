'''
Eight Puzzle Problem

'''

from copy import deepcopy

class EightPuzzle:

    def __init__(self, initial_state, goal):
        self.state = initial_state
        self.goal = goal
        self.action = ['ml','mr','mu','md']
    
    def check_goal(self):
        if self.state == self.goal:
            return True
        else:
            return False

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

