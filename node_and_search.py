'''
Define nodes of search tree and vanilla bfs search algorithm

Author: Tony Lindgren
'''

import queue
from time import process_time
from missionaries_and_cannibals import MissionariesAndCannibals
from eight_puzzle import EightPuzzle

class Node:
    '''
    This class defines nodes in search trees. It keep track of: 
    state, cost, parent, action, and depth 
    '''
    def __init__(self, state, cost=0, parent=None, action=None):
        self.parent = parent
        self.state = state
        self.action = action
        self.cost = cost
        self.depth = 0
        if parent:
            self.depth = parent.depth + 1 

    def goal_state(self):
        return self.state.check_goal()
    
    def successor(self):
        successors = queue.Queue()
        for action in self.state.action:                     
            child = self.state.move(action)      
            if child != None:                                
                childNode = Node(child, self.cost + 1, self, action)              
                successors.put(childNode)
        return successors
    
    def depth_successor(self):
        successors = queue.LifoQueue()
        for action in self.state.action:                     
            child = self.state.move(action)      
            if child != None:                                
                childNode = Node(child, self.cost + 1, self, action)              
                successors.put(childNode)
        return successors

    def pretty_print_solution(self, verbose=False):
        solution = []
        if verbose == False:
            print('Here is the list of moves:')
            solution.append(self.action)
            while (self.parent.action != None):
                solution.append(self.parent.action)
                self = self.parent
            
            for i in reversed(solution):
                print(i)

        else:
            print('Here is the list of moves and states:')
            solution.append(['Done!', self.state])
            while (self.parent.action != None):
                solution.append([self.action, self.state])
                self = self.parent
        
            for i in reversed(solution):
                i[1].pretty_print()
                print(i[0])

             
class SearchAlgorithm:
    '''
    Class for search algorithms, call it with a defined problem 
    '''
    def __init__(self, problem):
        self.start = Node(problem)
        self.visited = []
        self.counter = 0
        
    def bfs(self, verbose=False, statistics=False, FileSave=False):
        time_start = process_time()
        frontier = queue.Queue()
        frontier.put(self.start)
        stop = False
        while not stop:
            if frontier.empty():
                return None

            if self.visited == []:
                curr_node = frontier.get()
                self.visited.append(curr_node.state)
            else:
                if (frontier.get().state) not in self.visited:
                    curr_node = frontier.get()
                    self.visited.append(curr_node.state)
                    self.counter += 1
                else:
                    print('whoops repeat')
            if curr_node.goal_state():
                stop = True
                time_stop = process_time()
                if statistics == True:
                    print("Cannibals and Missionaries. Solution found")
                    print("Elapsed time (s):", time_stop - time_start)
                    print("Solution found at depth:", curr_node.depth)
                    print("Number of nodes explored:", self.counter)
                    print("Cost of solution:", curr_node.depth)
                    print("Estimated effective branching factor:", self.counter**(1/curr_node.depth))
                if FileSave == True:
                    file = open("results.txt", "w")
                    write=file.write
                    write("Cannibals and Missionaries. Solution for BFS" + "\n")
                    write("Elapsed time (s):" + str(time_stop - time_start) + "\n")
                    write("Solution found at depth:" + str(curr_node.depth) + "\n")
                    write("Number of nodes explored:" + str(self.counter) + "\n")
                    write("Cost of solution:" + str(curr_node.depth) + "\n")
                    write("Estimated effective branching factor:" + str(self.counter**(1/curr_node.depth)) + "\n \n")
                    file.close()
                return curr_node        
                        
            successor = curr_node.successor() 
            while not successor.empty():
                frontier.put(successor.get())  

    def dfs(self, depth_limit=None, verbose=False, statistics=False, FileSave=False):
        time_start = process_time()
        frontier = queue.Queue()
        frontier.put(self.start)
        stop = False
        self.visited = []
        while not stop:

            if frontier.empty():
                return None

            if self.visited == []:
                curr_node = frontier.get()
                self.visited.append(curr_node.state)

                if (depth_limit == curr_node.depth):
                    return None

            else:

                if (depth_limit == curr_node.depth):
                    return None
                    
                if (frontier.get().state) not in self.visited:
                    curr_node = frontier.get()
                    self.visited.append(curr_node.state)
                    self.counter += 1
                else:
                    print('whoops repeat')
            if curr_node.goal_state():
                stop = True
                time_stop = process_time()
                if statistics == True:
                    print("Cannibals and Missionaries. Solution found")
                    print("Elapsed time (s):", time_stop - time_start)
                    print("Solution found at depth:", curr_node.depth)
                    print("Number of nodes explored:", self.counter)
                    print("Cost of solution:", curr_node.depth)
                    print("Estimated effective branching factor:", self.counter**(1/curr_node.depth))
                    
                    if FileSave == True:
                        file = open("results.txt", "a")
                        write=file.write
                        write("Cannibals and Missionaries. Solution for DFS"  + "\n")
                        write("Elapsed time (s):" + str(time_stop - time_start) + "\n")
                        write("Solution found at depth:" + str(curr_node.depth) + "\n")
                        write("Number of nodes explored:" + str(self.counter) + "\n")
                        write("Cost of solution:" + str(curr_node.depth) + "\n")
                        write("Estimated effective branching factor:" + str(self.counter**(1/curr_node.depth)) + "\n \n")
                        file.close()
                return curr_node        
                        
            successor = curr_node.depth_successor() 
            while not successor.empty():
                frontier.put(successor.get())

    def ids(self, verbose=False, statistics=False, FileSave=False):
        time_start = process_time()
        frontier = queue.Queue()
        frontier.put(self.start)
        stop = False
        depth_counter = 0

        while not stop:

            curr_node = self.dfs(depth_counter, False, False, False)
            depth_counter += 1

            if curr_node != None:
                if curr_node.goal_state():
                    stop = True
                    time_stop = process_time()
                    if statistics == True:
                        print("Cannibals and Missionaries. Solution found")
                        print("Elapsed time (s):", time_stop - time_start)
                        print("Solution found at depth:", curr_node.depth)
                        print("Number of nodes explored:", self.counter)
                        print("Cost of solution:", curr_node.depth)
                        print("Estimated effective branching factor:", self.counter**(1/curr_node.depth))
                        
                        if FileSave == True:
                            file = open("results.txt", "a")
                            write=file.write
                            write("Cannibals and Missionaries. Solution for IDS"  + "\n")
                            write("Elapsed time (s):" + str(time_stop - time_start) + "\n")
                            write("Solution found at depth:" + str(curr_node.depth) + "\n")
                            write("Number of nodes explored:" + str(self.counter) + "\n")
                            write("Cost of solution:" + str(curr_node.depth) + "\n")
                            write("Estimated effective branching factor:" + str(self.counter**(1/curr_node.depth)) + "\n \n")
                            file.close()
                    return curr_node        
    