#!/usr/bin/env python
# coding: utf-8

# In[17]:


from Flags import *
import numpy as np
class MonteCarlo:
    
    def __init__(self, flags, gammma, epsilon, episodeLength):
        self.flags = flags
        self.gam = gammma
        self.eps = epsilon
        self.epL = episodeLength
        self.initialize_values()
        
    def initialize_values(self):
        self.Qval = {}
        for state in self.flags.get_all_states():
            self.Qval[(state, 'U')] = 0
            self.Qval[(state, 'D')] = 0
            self.Qval[(state, 'L')] = 0
            self.Qval[(state, 'R')] = 0
            
    def sample_epsilon_greedy(self, state):
        aVal = {'U':self.Qval[(state, 'U')], 
                'D':self.Qval[(state, 'D')]
                'L':self.Qval[(state, 'L')]
                'R':self.Qval[(state, 'R')]}
        bestA = max(aVal, key = aVal.get)
        action = ['U','D','L','R']
        bestProb = 1 - self.eps+eps/4
        regProb = self.eps/4
        if bestA == 'U'
          probs = [bestProb,regProb,regProb,regProb]
        elif bestA == 'D'
          probs = [regProb,bestProb,regProb,regProb]
        elif bestA == 'L'
          probs = [regProb,regProb,bestProb,regProb]
        elif bestA == 'R'
          probs = [regProb,regProb,regProb,bestProb]
        action = np.random.choice(action, p=probs)
            

