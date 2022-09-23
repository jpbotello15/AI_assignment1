"""
Define nodes of search tree and vanilla bfs search algorithm

Author: Tony Lindgren
"""

import queue
from time import process_time
from missionaries_and_cannibals import MissionariesAndCannibals
from eight_puzzle import EightPuzzle

from dataclasses import dataclass, field
from typing import Any


@dataclass(order=True)
class PrioritizedItem:
    priority: int
    item: Any = field(compare=False)


class Node:
    """
    This class defines nodes in search trees. It keep track of:
    state, cost, parent, action, and depth
    """

    def __init__(self, state, cost=0, parent=None, action=None, verbose=False):
        self.parent = parent
        self.state = state
        self.action = action
        self.cost = cost
        self.depth = 0
        self.verbose = verbose
        if parent:
            self.depth = parent.depth + 1

    def __lt__(self, other):
        return self.cost < other.cost

    def __gt__(self, other):
        return self.cost > other.cost

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

    # priority_successor PROBLEM IN THIS FUNCTION,
    def priority_successor(self):
        successors = queue.PriorityQueue()
        for action in self.state.action:
            child = self.state.move(action)
            if child != None:
                childNode = Node(child, self.cost + 1, self, action)
                if self.verbose:
                    print(childNode)
                weight = EightPuzzle.heuristic2(childNode)
                # successors.put puts weight as a first value, and later it is extracted like a state of childNode as integer.
                successor = PrioritizedItem(weight, childNode)
                successors.put(successor)

        return successors

    def pretty_print_solution(self, verbose=False):
        solution = []
        if verbose == False:
            print("Here is the list of moves:")
            solution.append(self.action)
            print_domain = self.parent
            while self.parent.action != None:
                solution.append(print_domain)
                print_domain = print_domain.parent

            for i in reversed(solution):
                print(i)
        else:
            print("Here is the list of moves and states:")
            solution.append(["Done!", self.state])
            while self.parent.action != None:
                solution.append([self.action, self.state])
                self = self.parent

            for i in reversed(solution):
                i[1].pretty_print()
                print(i[0])


class SearchAlgorithm:
    """
    Class for search algorithms, call it with a defined problem
    """

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
                    print("whoops repeat")
            if curr_node.goal_state():
                stop = True
                time_stop = process_time()
                if statistics == True:
                    print("Cannibals and Missionaries. Solution found")
                    print("Elapsed time (s):", time_stop - time_start)
                    print("Solution found at depth:", curr_node.depth)
                    print("Number of nodes explored:", self.counter)
                    print("Cost of solution:", curr_node.depth)
                    print(
                        "Estimated effective branching factor:",
                        self.counter ** (1 / curr_node.depth),
                    )
                if FileSave == True:
                    file = open("results.txt", "w")
                    write = file.write
                    write("Cannibals and Missionaries. Solution for BFS" + "\n")
                    write("Elapsed time (s):" + str(time_stop - time_start) + "\n")
                    write("Solution found at depth:" + str(curr_node.depth) + "\n")
                    write("Number of nodes explored:" + str(self.counter) + "\n")
                    write("Cost of solution:" + str(curr_node.depth) + "\n")
                    write(
                        "Estimated effective branching factor:"
                        + str(self.counter ** (1 / curr_node.depth))
                        + "\n \n"
                    )
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

                if depth_limit == curr_node.depth:
                    return None

            else:

                if depth_limit == curr_node.depth:
                    return None

                if (frontier.get().state) not in self.visited:
                    curr_node = frontier.get()
                    self.visited.append(curr_node.state)
                    self.counter += 1
                else:
                    print("whoops repeat")
            EightPuzzle.pretty_print(curr_node.state)
            if curr_node.goal_state():
                stop = True
                time_stop = process_time()
                if statistics == True:
                    print("Cannibals and Missionaries. Solution found")
                    print("Elapsed time (s):", time_stop - time_start)
                    print("Solution found at depth:", curr_node.depth)
                    print("Number of nodes explored:", self.counter)
                    print("Cost of solution:", curr_node.depth)
                    print(
                        "Estimated effective branching factor:",
                        self.counter ** (1 / curr_node.depth),
                    )

                    if FileSave == True:
                        file = open("results.txt", "a")
                        write = file.write
                        write("Cannibals and Missionaries. Solution for DFS" + "\n")
                        write("Elapsed time (s):" + str(time_stop - time_start) + "\n")
                        write("Solution found at depth:" + str(curr_node.depth) + "\n")
                        write("Number of nodes explored:" + str(self.counter) + "\n")
                        write("Cost of solution:" + str(curr_node.depth) + "\n")
                        write(
                            "Estimated effective branching factor:"
                            + str(self.counter ** (1 / curr_node.depth))
                            + "\n \n"
                        )
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
                        print(
                            "Estimated effective branching factor:",
                            self.counter ** (1 / curr_node.depth),
                        )

                        if FileSave == True:
                            file = open("results.txt", "a")
                            write = file.write
                            write("Cannibals and Missionaries. Solution for IDS" + "\n")
                            write(
                                "Elapsed time (s):" + str(time_stop - time_start) + "\n"
                            )
                            write(
                                "Solution found at depth:" + str(curr_node.depth) + "\n"
                            )
                            write(
                                "Number of nodes explored:" + str(self.counter) + "\n"
                            )
                            write("Cost of solution:" + str(curr_node.depth) + "\n")
                            write(
                                "Estimated effective branching factor:"
                                + str(self.counter ** (1 / curr_node.depth))
                                + "\n \n"
                            )
                            file.close()
                    return curr_node

    def greedy_search(
        self, depth_limit=None, verbose=False, statistics=False, FileSave=False
    ):
        time_start = process_time()
        frontier = queue.PriorityQueue()
        frontier.put(self.start)
        stop = False
        self.visited = []
        counter = -1
        while not stop:

            counter += 1
            if frontier.empty():
                return None

            if self.visited == []:
                curr_node = frontier.get()
                self.visited.append(curr_node.state.state)

                if depth_limit == curr_node.depth:
                    return None

            else:
                if depth_limit <= curr_node.depth:
                    return None
                if (frontier.get().item.state) not in self.visited:
                    try: 
                        curr_node = frontier.get(False)
                        #EightPuzzle.pretty_print(curr_node.item.state)
                        #print('parent', curr_node)
                    except Exception:
                        curr_node = None
                        print('exception', curr_node)
                    if curr_node:
                        curr_node = curr_node.item
                    else:
                        #print('returned none')
                        return None
                    self.visited.append(curr_node.state.state)
                    self.counter += 1
                else:
                    print('whoops repeat')
                    a = input()
            if verbose:
                EightPuzzle.pretty_print(curr_node.state)
            if curr_node.goal_state():
                stop = True
                time_stop = process_time()
                if statistics:
                    branching_factor = self.counter ** (1 / curr_node.depth)
                    output = f"""
                    Eight Puzzle. Solution found
                    Elapsed time (s): {time_stop - time_start}
                    Solution found at depth: {curr_node.depth}
                    Number of nodes explored: {self.counter}
                    Cost of solution: {curr_node.depth}
                    Estimated effective branching factor: {branching_factor}
                    """
                    print(output)

                    if FileSave == True:
                        with open("task5check.txt", "a") as f:
                            f.write(output)
                return curr_node

            successors = curr_node.successor()

            while not successors.empty():
                successor = successors.get()
                #print(counter, successor)
                priority = (self.heuristic1(successor.state, verbose)) * counter
                #print("Potential successor", successor.state.state)
                #if not successor.state.state in self.visited:
                frontier.put(PrioritizedItem(priority, successor))
                    

    def heuristic1(self, state, verbose=False):
        global h1
        h1 = 0
        for i in range(0, len(state.state)):
            for z in range(0, len(state.state[0])):
                if state.state[i][z] == state.goal[i][z]:
                    h1 = h1 + 1
        # h1 = len(state) ** 2 - h1
        if verbose:
            print("Heuristic_1: " + str(h1))
        return h1