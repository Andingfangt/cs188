# valueIterationAgents.py
# -----------------------
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


# valueIterationAgents.py
# -----------------------
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


import mdp, util
from typing import Set

from learningAgents import ValueEstimationAgent
import collections

class ValueIterationAgent(ValueEstimationAgent):
    """
        * Please read learningAgents.py before reading this.*

        A ValueIterationAgent takes a Markov decision process
        (see mdp.py) on initialization and runs value iteration
        for a given number of iterations using the supplied
        discount factor.
    """
    def __init__(self, mdp: mdp.MarkovDecisionProcess, discount = 0.9, iterations = 100):
        """
          Your value iteration agent should take an mdp on
          construction, run the indicated number of iterations
          and then act according to the resulting policy.

          Some useful mdp methods you will use:
              mdp.getStates()
              mdp.getPossibleActions(state)
              mdp.getTransitionStatesAndProbs(state, action)
              mdp.getReward(state, action, nextState)
              mdp.isTerminal(state)
        """
        self.mdp = mdp
        self.discount = discount
        self.iterations = iterations
        self.values = util.Counter() # A Counter is a dict with default 0
        self.runValueIteration()

    def runValueIteration(self):
        # Write value iteration code here
        for _ in range(self.iterations):
            new_values = util.Counter()
            for state in self.mdp.getStates():
                if self.mdp.isTerminal(state):
                    continue
                else:
                    new_values[state] = self.getMaxIteration(state)
            self.values = new_values
            
    def getMaxIteration(self, state):
        '''
        return the max sum of all the possible actions,
        only used for non-terminal state
        '''
        max_new_value = -float('inf')
        for action in self.mdp.getPossibleActions(state):
            curr_new_value = sum(prob * (self.mdp.getReward(state, action, nextState) + self.discount * self.getValue(nextState)) for nextState, prob in self.mdp.getTransitionStatesAndProbs(state, action))
            max_new_value = max(curr_new_value, max_new_value)
        return max_new_value
        
    def getValue(self, state):
        """
          Return the value of the state (computed in __init__).
        """
        return self.values[state]


    def computeQValueFromValues(self, state, action):
        """
          Compute the Q-value of action in state from the
          value function stored in self.values.
        """
        return sum(prob * (self.mdp.getReward(state, action, nextState) + self.discount * self.getValue(nextState)) for nextState, prob in self.mdp.getTransitionStatesAndProbs(state, action))
            

    def computeActionFromValues(self, state):
        """
          The policy is the best action in the given state
          according to the values currently stored in self.values.

          You may break ties any way you see fit.  Note that if
          there are no legal actions, which is the case at the
          terminal state, you should return None.
        """
        if self.mdp.isTerminal(state):
            return None
        optimal_action = None
        max_value = -float('inf')
        for action in self.mdp.getPossibleActions(state):
            curr_Q_value = self.getQValue(state, action)
            if curr_Q_value > max_value:
                optimal_action = action
                max_value = curr_Q_value
        return optimal_action
            

    def getPolicy(self, state):
        return self.computeActionFromValues(state)

    def getAction(self, state):
        "Returns the policy at the state (no exploration)."
        return self.computeActionFromValues(state)

    def getQValue(self, state, action):
        return self.computeQValueFromValues(state, action)


class PrioritizedSweepingValueIterationAgent(ValueIterationAgent):
    """
        * Please read learningAgents.py before reading this.*

        A PrioritizedSweepingValueIterationAgent takes a Markov decision process
        (see mdp.py) on initialization and runs prioritized sweeping value iteration
        for a given number of iterations using the supplied parameters.
    """
    def __init__(self, mdp: mdp.MarkovDecisionProcess, discount = 0.9, iterations = 100, theta = 1e-5):
        """
          Your prioritized sweeping value iteration agent should take an mdp on
          construction, run the indicated number of iterations,
          and then act according to the resulting policy.
        """
        self.theta = theta
        ValueIterationAgent.__init__(self, mdp, discount, iterations)

    def getDiff(self, s):
        '''
        Find the absolute value of the difference between the current value of s in self.values 
        and the highest Q-value across all possible actions from s (this represents what the value should be); 
        call this number diff. 
        '''
        curr_value = self.getValue(s)
        highest_Q_value = -float('inf')
        for a in self.mdp.getPossibleActions(s):
            highest_Q_value = max(highest_Q_value, self.getQValue(s,a))
        diff = abs(curr_value - highest_Q_value)
        return diff
    
    
    def runValueIteration(self):
        # Compute predecessors of all states.
        predecessors_dict = dict()
        for s in self.mdp.getStates():
            for a in self.mdp.getPossibleActions(s):
                for n_s, _ in self.mdp.getTransitionStatesAndProbs(s, a):
                    old_set: Set = predecessors_dict.get(n_s, set())
                    old_set.add(s)
                    predecessors_dict[n_s] = old_set
        
        
        # Initialize an empty priority queue.
        pq = util.PriorityQueue()
        
        # For each non-terminal state s, do: 
        for s in self.mdp.getStates():
            if self.mdp.isTerminal(s):
                continue
                
            # Find the absolute value of the difference between the current value of s in self.values 
            # and the highest Q-value across all possible actions from s (this represents what the value should be); 
            # call this number diff. 
            diff = self.getDiff(s)
            
            # Push s into the priority queue with priority -diff
            pq.push(s, -diff)
            
        
        # For iteration in 0, 1, 2, ..., self.iterations - 1, do:
        for _ in range(self.iterations):
            # If the priority queue is empty, then terminate.
            if pq.isEmpty():
                break
            
            # Pop a state s off the priority queue.
            s = pq.pop()
            
            # Update the value of s (if it is not a terminal state) in self.values.
            if not self.mdp.isTerminal(s):
                self.values[s] = self.getMaxIteration(s)
                
            # For each predecessor p of s, do:    
            for p in predecessors_dict[s]:
                # Find the absolute value of the difference between the current value of p in self.values 
                # and the highest Q-value across all possible actions from p (this represents what the value should be); 
                # call this number diff. 
                diff = self.getDiff(p)
                
                # If diff > theta, push p into the priority queue with priority -diff (note that this is negative), 
                # as long as it does not already exist in the priority queue with equal or lower priority, we use update.
                if diff > self.theta:
                    pq.update(p, -diff)
                    
                
                
    
    
                
        
        
            
            
        
                    
                    
                

