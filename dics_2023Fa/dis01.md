# Regular Discussion 1

## 1. Towers of Hanoi

**(a) Propose a state representation for the problem**
Use three List, each inside is the order of its current discs.
Like $[[1,2,3,4,5],[ \quad],[\quad ]]$ is the beginning state.

**(b) What is the size of the state space?**
If we have $k$ pegs and $n$ discs, for each disc, we can set it in one of the $k$ pegs, thus the total possibility is $k^{n}$

**(c) What is the start state?**
$[[1,2\cdots,n],[ \quad],[\quad ]]$

**(d) From a given state, what actions are legal?**
For each action, we are allowed to pop the first disc of any peg, and push it to the front of any other peg, as long as this push action don't against the rule, which is we are never allowed to move a larger disc on top of a smaller disc.

**(e) What is the goal test?**
To check whether the current state is $[[\quad],[\quad],[1,2,\cdots,n]]$

## 2. Search Algorithms in Action

**a) DFS**
States Expanded: Start, A, C, D, Goal
Path Returned: Start-A-C-D-Goal


**b) BFS**
States Expanded: Start, A, B, D, C, Goal
Path Returned: Start-D-Goal

**c) Uniform cost search.**
States Expanded: Start, A, B, D, C, Goal
Path Returned: Start-A-C-Goal


