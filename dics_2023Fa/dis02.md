# Regular Discussion 2

## 1. Search and Heuristics

(a) For each state, we should record [curr_position[X,Y], curr_velocity[0,$\cdots,V_{max}$], curr_toward[N,S,E,W]]
$\therefore $ The state size is $M\cdot N \cdot (V_{max}+1) \cdot 4$

(b) No, if heuristic be Manhattan distance, in this problem, agent has velocity, so Manhattan distance won't always underestimate the cost.

(c)
For Simply consider:
Assume agent can always move with $V_{max}$ and stop at target immediately. 
$\therefore H(x) = \dfrac{d_{Manhattan}}{V_{max}} + number\_turn\_to\_target$

Else:
Consider for a Manhattan distance, agent can speed up to $V_{max}$, and advance at $V_{max}$ for a while, then slowed down to 0 at target.
$$\begin{aligned}
\therefore d_{V_{max}} & = d_{manhattan} −\dfrac{(V_{max})\cdot(V_{max}+1)}{2} −\dfrac{(V_{max})(V_{max}−1)}{2} \\  & = d_{manhattan} − V_{max}^2 
\end{aligned}$$

$\therefore $If $d_{manhattan} > V_{max}^2$, agent will cost $V_{max}$ step to speed up,  $\dfrac{d_{manhattan} − V_{max}^2}{V_{max}}$ step for union  $V_{max}$, and $V_{max}$ step to slow down. Total step is $\dfrac{d_{manhattan}}{V_{max}} + V_{max}$

$$\Rightarrow H(x) = \left\{ 
\begin{aligned}
    &\dfrac{d_{Manhattan}}{V_{max}},  & \text{if } d_{Manhattan} \leq V_{max}^2 \\
    &\dfrac{d_{manhattan}}{V_{max}} + V_{max}, & \text{if } d_{Manhattan} > V_{max}^2
\end{aligned}
\right.
$$

(d)
If we apply a inadmissible heuristic, the A* graph search will find a solution, but it may not be optimal.

(e)
No, even if we have an admissible heuristic, it still won't guaranteed to return an optimal solution in A* graph search. Unless it is also consistent.
P.S: it will return optimal if it is tree search, due to graph search won't visit a node twice.

(f)
Inadmissible one is easy to compute.


## Q2. Pacfriends Unite

(a)
(i)
For each state, we need to record [Pacman_position[M*N], ghosts_status[$2^G$]]
$\therefore $ total is $M\cdot N \cdot 2^G$

(ii)
neither, cause this h may overestimate.

(iii)
neither, cause this h may be overestimate.

(iv)
both.
For admissible: the number of remaining ghosts is definitely $\leq$ actual cost.
For consistent: the cost between two neighbor state is 1, and the diff between those two h is $0$ or $1$ $\leq 1 $. 

(b)
(i)
For each state, we need to record [all_pacman_position[$C_{MN}^P$], ghosts_status[$2^G$]]
$\therefore $ total states is $\binom{MN}{P} \cdot 2^G$

(ii)
neither, this h may overestimate.

(iii)
both.
For admissible, smallest Manhattan distance $\leq$ reduce one ghost $\leq$ reduce all ghost.
For consistent, the cost between two neighbor state is 1, and the diff between those two h is 0 1 or -1 $\leq$ 1.

(iv)
neither
Cause since we now have multi Pacman, we can eliminate more than 1 ghost at one step.

(v)
both.
For admissible, since at the beginning we have $P==G$, \
$\therefore \dfrac{\text{number of remaining ghosts}}{P} \leq 1 \leq \text{actual cost}$ 
For consistent, the cost between two neighbor state is 1, and the diff between those two h is 0  or $\dfrac{1}{p}$ $\leq$ 1.