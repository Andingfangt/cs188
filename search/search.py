# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""
from typing import List, Tuple
import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem: SearchProblem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    hp = util.PriorityQueueWithFunction(lambda x: x[1])
    visited_set = set()
    start_state = problem.getStartState()
    hp.push((start_state, 0, []))
    while hp:
        curr_state_with_depth = hp.pop()
        curr_state: Tuple[int,int] = curr_state_with_depth[0]
        curr_depth: int = curr_state_with_depth[1]
        curr_action_lst: List[str] = curr_state_with_depth[2]
        visited_set.add(curr_state)
        if problem.isGoalState(curr_state):
            return curr_action_lst
        for succ in problem.getSuccessors(curr_state):
            succ_state = succ[0]
            if succ_state in visited_set:
                continue
            succ_depth  = curr_depth - 1
            succ_action_lst = curr_action_lst + [succ[1]]
            hp.push((succ_state,succ_depth,succ_action_lst))
    

def breadthFirstSearch(problem: SearchProblem):
    """Search the shallowest nodes in the search tree first."""
    hp = util.PriorityQueueWithFunction(lambda x: x[1])
    visited_set = set()
    start_state = problem.getStartState()
    hp.push((start_state, 0, []))
    while hp:
        curr_state_with_depth = hp.pop()
        curr_state: Tuple[int,int] = curr_state_with_depth[0]
        if curr_state in visited_set:
            continue
        visited_set.add(curr_state)
        curr_depth: int = curr_state_with_depth[1]
        curr_action_lst: List[str] = curr_state_with_depth[2]
        if problem.isGoalState(curr_state):
            return curr_action_lst
        for succ in problem.getSuccessors(curr_state):
            succ_state = succ[0]
            if succ_state in visited_set:
                continue
            succ_depth  = curr_depth + 1
            succ_action_lst = curr_action_lst + [succ[1]]
            hp.push((succ_state,succ_depth,succ_action_lst))

def uniformCostSearch(problem: SearchProblem):
    """Search the node of least total cost first."""
    hp = util.PriorityQueueWithFunction(lambda x: x[1])
    visited_set = set()
    start_state = problem.getStartState()
    hp.push((start_state, 0, []))
    while hp:
        curr_state_with_depth = hp.pop()
        curr_state: Tuple[int,int] = curr_state_with_depth[0]
        if curr_state in visited_set:
            continue
        visited_set.add(curr_state)
        curr_cost: int = curr_state_with_depth[1]
        curr_action_lst: List[str] = curr_state_with_depth[2]
        if problem.isGoalState(curr_state):
            return curr_action_lst
        for succ in problem.getSuccessors(curr_state):
            succ_state = succ[0]
            if succ_state in visited_set:
                continue
            succ_cost  = curr_cost + succ[2]
            succ_action_lst = curr_action_lst + [succ[1]]
            hp.push((succ_state,succ_cost,succ_action_lst))

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    hp = util.PriorityQueueWithFunction(lambda x: x[1]+x[3])
    visited_set = set()
    start_state = problem.getStartState()
    hp.push((start_state, 0, [], heuristic(start_state,problem)))
    while hp:
        curr_state_with_info = hp.pop()
        curr_state: Tuple[int,int] = curr_state_with_info[0]
        if curr_state in visited_set:
            continue
        visited_set.add(curr_state)
        curr_cost: int = curr_state_with_info[1]
        curr_action_lst: List[str] = curr_state_with_info[2]
        if problem.isGoalState(curr_state):
            return curr_action_lst
        for succ in problem.getSuccessors(curr_state):
            succ_state = succ[0]
            if succ_state in visited_set:
                continue
            succ_cost  = curr_cost + succ[2]
            succ_action_lst = curr_action_lst + [succ[1]]
            hp.push((succ_state,succ_cost,succ_action_lst,heuristic(succ_state,problem)))
    


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
