"""
Define problem and start execution of search problems
Author: Tony Lindgren
"""


from tabnanny import verbose
from eight_puzzle import EightPuzzle
from missionaries_and_cannibals import MissionariesAndCannibals
from node_and_search import SearchAlgorithm
from node_and_search import Node

# init_state = [[0, 0], 'r', [3, 3]]
# goal_state = [[3, 3], 'l', [0, 0]]

init_state = [[1, 2, 3], [4, 5, 6], ["e", 7, 8]]
goal_state = [[1, 2, 3], [7, "e", 6], [5, 4, 8]]


def main():
    # mc = MissionariesAndCannibals(init_state, goal_state)
    # sa = SearchAlgorithm(mc)
    # solution = sa.bfs(statistics=True, FileSave=True)
    # solution = sa.dfs(statistics=True, FileSave=True)
    # solution = sa.ids(statistics=True, FileSave=True)
    # solution.pretty_print_solution(verbose=True)
    # print('Confirm solution is: ', solution.state.check_goal())

    ep = EightPuzzle(init_state, goal_state)
    sa = SearchAlgorithm(ep)
    solution = sa.greedy_search(depth_limit = 200, verbose=False, statistics=True, FileSave=True)
    if solution:
        solution.state.pretty_print()
    else:
        print("Did not yield a solution")


if __name__ == "__main__":
    main()
