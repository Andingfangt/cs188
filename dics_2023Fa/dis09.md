# Regular Discussion 9

## 1. Bayes’ Nets Sampling

(a)
**Review: four type of Sampling**

* *Prior Sampling*: sample according the CPTs. Then use count to compute the possibility
* *Rejection Sampling*: is pretty much the same as prior sampling, just by throw away the bad samples that against our evidence.
* *Likelihood Weighting*: following the CPTs, for non-evidence variables, we simply do sampling according to the conditional distribution given the values already sampled for the variable's parents, for evidence variables, we multiply the Weight of this sample by $P(e|e(parents))$. Then use the Weight of each samples to compute the possibility. The Weight ensure the consistent.
* *Gibbs Sampling*: first set evidence and all other variables to some totally random value (not taking into account any CPTs). Then repeatedly pick one non evidence variable at a time, clear its value, and resample it given the values currently assigned to all other variables(can be easily calculated only using the CPTs that connect with its neighbors).

(i) $\frac{5}{8}$
(ii) $\frac{2}{3}$

(b)
$$w_1 = 1 \cdot P(+b|-a) \cdot P(-d|-a,+b,+c) = \dfrac{1}{3}* \dfrac{5}{6}= \dfrac{5}{18}$$
$$w_2 = 2 \cdot P(+b|+a) \cdot P(-d|+c) = \dfrac{1}{5} * \dfrac{5}{6} = \dfrac{1}{6}$$
$$w_3 = 2 \cdot P(+b|+a) \cdot P(-d|-c) = \dfrac{1}{5} * \dfrac{1}{8} = \dfrac{1}{40}$$
$$w_4 = 2 \cdot P(+b|-a) \cdot P(-d|-c) = \dfrac{1}{3} * \dfrac{1}{8} = \dfrac{1}{24}$$

(c) 
$P(-a|+b,-d) =\dfrac{w_1+w_4}{\sum_{i=1}^{i=4}w_i} = 0.625$

(d)
Since likelihood weighting conditions only on upstream evidence. The Weight for A is just the possibility of A, no conditionally. So $P(D|A)$ is better.

(e)
In Gibbs Sampling:
The evidence variables stay unchanged, so pass Sequence 2
Each time only resampling one non evidence variable, so pass Sequence 4.
So Sequence 1 and Sequence 3 is valid.


## 2. Decision Networks and VPI

**Review**:

* 1. Nodes in Decision Networks:
  * Chance nodes: behave identically to Bayes’ nets, represented as ovals.
  * Action nodes: are nodes that we have complete control over, represented as rectangles.
  * Utility nodes: are children of some combination of action and chance nodes, output a utility based on the values taken on by their parents, represented as diamonds.
* 2. Expected Utility:
  * The expected utility of taking an action a given evidence e and n chance nodes is computed with the following formula: 
  $$EU(a|e) = \sum_{x_1, \cdots, x_n} P(x_1, \cdots, x_n|e) \cdot U(a | x_1, \cdots, x_n)$$
* 3. Maximum Expected Utility
  * $$MEU(e) = \underset{a}{max}EU(a|e)$$
* 4. The Value of Perfect Information:
  * VPI is the expected to  increase if we observe some new evidence.
  * $$VPI(E'|e) = MEU(e, E') - MEU(e)$$
  * note that the new evidence is represented as an random variable $E$
  * $$MEU(e,E') = \sum_{e'}P(e'|e) \cdot MEU(e,e')$$
* 5. Properties of VPI:
  * Nonnegativity. $∀E', e VPI(E'|e) \geq 0$
  * Nonadditivity. $VPI(E_j, E_k | e) \neq VPI(E_j|e) + VPI(E_k|e)$
  * Order-independence. $VPI(E_j, E_k | e) = VPI(E_j|e) + VPI(E_k|e,E_j) = VPI(E_k|e) + VPI(E_j|e,E_k)  $


(a)
$EU(+buy) = P(+q)\cdot U(+buy,+q) + P(-q) \cdot U(+buy,-q) = 0.7*(2000-1500) + 0.3*(-700+2000-1500) = 290$

(b)
| $P(T\|Q)$ |  |  |
| ------ | -- | -- |
| $+q$ | $-t$ | 0.1 |
| $+q$ | $+t$ | 0.9 |
| $-q$ | $-t$ | 0.8 |
| $-q$ | $+t$ | 0.2 |

| $P(Q)$ |  |
| ------ | -- |
| $+q$ | 0.7 |
| $-q$ | 0.3 |


$P(+t) = \sum P(+t,Q) = \sum P(+t | Q) \cdot P(Q) = 0.9*0.7 + 0.2*0.3 = 0.69$
$P(-t) = 1- P(+t) = 0.31$
$P(+q|+t) = \dfrac{P(+t,+q)}{P(+t)} = \dfrac{0.7*0.9}{0.69} = 0.91$
$P(+q|-t) = \dfrac{P(+q,-t)}{P(-t)} = \dfrac{0.7*0.1}{0.31} = 0.22$

(c)
$EU(+buy|+t) = \sum P(Q|+t) \cdot U(+buy, Q) = 0.91*500 + (1-0.91)*-200 = 437$
$EU(-buy|+t) = 0$
$EU(+buy|-t) = \sum P(Q|-t) \cdot U(+buy, Q) = 0.22*500 + (1-0.22)*-200 = -46$
$EU(-buy|-t) = 0$

$MEU(+t) = 437 \text{ with } +buy$ 
$MEU(-t) = 0 \text{ with } -buy$ 

(d)
$VPI(T) = MEU(T) - MEU(\emptyset)$
$MEU(\emptyset) = 290$
$MEU(T) = P(+t)\cdot MEU(+t) + P(-t) \cdot MEU(-t) = 0.69*437 + 0.31*0 = 301.53$
$\Rightarrow VPT(T) = 301.53 - 290 = 11.53 < 50$
$\therefore$ should not pay for it.

