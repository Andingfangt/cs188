# Regular Discussion 6

## 1. Reinforcement Learning

(a)
$\hat{T}(B,\rightarrow,C) = \dfrac{2}{3}$
$\hat{R}(C,\rightarrow,X) = 1$

(b)
Since $A$ only $\rightarrow B$, and $R$ = 0, so $Q(A,\rightarrow) $ be nonzero when some $Q(B,a) $ be nonzero, and $B$ can reach $C$ and $A$, pass $A$, so only when some $Q(C,a)$ become nonzero. Since only the $R(C,\rightarrow,X) = 1 > 0$ in iterate 9,18,..., so in iteration 11, $Q(B,\rightarrow)$ become nonzero, in iteration 14 $Q(A,\rightarrow)$ become nonzero, in iteration 22, $Q(B,\leftarrow)$ become nonzero.

(c)
(i) True, Q learning is model-free, you learn the optimal policy explicitly, and the model itself implicitly.

(ii) False, TD Learning does not necessarily find the optimal policy, it only learns the value of the states following some given policy.

(iii) False, calculate state values based on some episode of training, no a single transitions.

(iv) False, not requires all samples must be from the optimal policy, Q-learning is off-policy.

## 2. MDPs: Grid-World Water Park

(a)(b)(c) are the same as disc5

(d) **feature-based Q-learning**
Update the weight:
$difference = [R(s,a,s') + \gamma \underset{a'}{max}Q(s',a')] - Q(s,a)$
$w_i = w_i + \alpha\cdot difference\cdot f_i(s,a)$ 

give a transition $(s=F, a=east, r=+2, s'=G)$, let's Update:
$difference = [2+0]-0=2; wi = 0+2*1=2$

With feature vectors, we can treat values of states and Q-states as linear value functions:
$V(s) = w_1\cdot f_1(s) + w_2 \cdot f_2(s) +\cdots w_n\cdot f_n(s)$
$Q(s,a) = w_1 \cdot f_1(s,a) + w_2 \cdot f_2(s,a) + \cdots + w_n \cdot f_n(s,a)$

**Advantage:** We can see with only one transition, we can update all Q-values in feature-based Q-learning, and we don't need to maintain the big table for all the Q-values.
PS: in our problem, we only has one feature $f$ or $f'$

in $f$ case, $Q(s,a) = a == east? 2 : 0$, means if we can go east, we always should choose east. So $\pi_2 $ is greedy
in $f'$ case, Q(s,a) = a == east and s == G or s == F? 2 : 0, means if we at F and G, we should go east. So all $\pi_1, \pi_2, \pi_3 $ is greedy.

## 3. RL

(a)
$sample = R(s,a,s') + \gamma \underset{a'}{max}Q(s',a')$
$Q(s,a) = (1-\alpha) \cdot Q(s,a) + \alpha \cdot sample$

$$
Q(A,Go) = 0.5*0 + 0.5(2+0) = 1 \\
Q(C,Stop) = 0.5*0 + 0.5(0+1) = 0.5 \qquad (i)\\
Q(B,Stop) = 0.5*0 + 0.5(-2+1) = -0.5 \\
Q(B,Go) = 0.5*0 + 0.5(-6+0.5) = -5.5/2 \\
Q(C,Go) = 0.5*0 + 0.5(2+1) = 1.5 \qquad (ii)
$$

(b)

* Step 1:
    Use a sample to compute $difference = [R(s,a,s') + \gamma \underset{a'}{max}Q(s',a')] - Q(s,a)$
* Step 2:
    Use $Q(s,a) = \sum_i w_i\cdot f_i$ to compute all the current Q-values we need in Step 1
* Step 3:
    Update $w_i = w_i + \alpha\cdot difference\cdot f_i(s,a)$ 

$Q(s,a) = 0$
$difference = 4+0 - 0 = 4$
(i) $w_1 = 0+0.5\cdot difference\cdot f_1(A,Go) = 2$
(ii) $w_2 = 0+0.5\cdot difference\cdot f_2(A,GO) = 2$

$Q(B,Stop) = 2*1 + 2* -1 = 0$
$Q(A,Stop) = 2*1 + 2* -1 = 0$
$Q(A,Go) = 2*1 + 2* 1 = 4$
$difference = 0+ max Q(A,a') - Q(B,Stop) = 4$
(iii) $w_1 = 2+0.5\cdot difference\cdot f_1(B,Stop) = 4$
(iv) $w_2 = 2+0.5\cdot difference\cdot f_2(B,Stop) = 0$


