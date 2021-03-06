#!/usr/bin/env python
# coding: utf-8

# In[19]:


class Flags:
    
    def __init__(self):
        self.flag1=0
        self.flag2=0
        self.flag3=0
        self.flag4=0
        self.flagG=0
        
    def initial_state(self):
        initial_state== (0,0)    
    
    
    def get_all_states (self) :# return a list  containing  all the  possible  states  in this  MDP...
        states = [(0,0),(0,1),(0,2),(0,3),(0,4),
                  (1,0),(1,1),(1,2),(1,3),(1,4),
                  (2,0),(2,1),(2,2),(2,3),(2,4),
                  (3,0),(3,1),(3,2),(3,3),(3,4),
                  (4,0),(4,1),(4,2),(4,3),(4,4)]
        return states
    
    def next_s(self,state,action):
        s_list ={((0,0),'U'):[(1,0)],
                 ((0,0),'R'):[(0,1)],
                 ((0,0),'L'):[(0,0)],
                 ((0,0),'D'):[(0,0)],
                 
                 ((0,1),'U'):[(1,1)],
                 ((0,1),'R'):[(0,2)],
                 ((0,1),'L'):[(0,0)],
                 ((0,1),'D'):[(0,1)],
                 
                 ((0,2),'U'):[(1,2)],
                 ((0,2),'R'):[(0,3)],
                 ((0,2),'L'):[(0,1)],
                 ((0,2),'D'):[(0,2)],
                 
                 ((0,3),'U'):[(1,3)],
                 ((0,3),'R'):[(0,4)],
                 ((0,3),'L'):[(0,2)],
                 ((0,3),'D'):[(0,3)],
                 
                 ((0,4),'U'):[(1,4)],
                 ((0,4),'R'):[(0,4)],
                 ((0,4),'L'):[(0,3)],
                 ((0,4),'D'):[(0,4)],
                 
                 ((1,0),'U'):[(2,0)],
                 ((1,0),'R'):[(1,1)],
                 ((1,0),'L'):[(1,0)],
                 ((1,0),'D'):[(0,0)],
                 
                 ((1,1),'U'):[(2,1)],
                 ((1,1),'R'):[(1,2)],
                 ((1,1),'L'):[(1,0)],
                 ((1,1),'D'):[(0,1)],
                 
                 ((1,2),'U'):[(2,2)],
                 ((1,2),'R'):[(1,3)],
                 ((1,2),'L'):[(1,1)],
                 ((1,2),'D'):[(0,2)],
                 
                 ((1,3),'U'):[(2,3)],
                 ((1,3),'R'):[(1,4)],
                 ((1,3),'L'):[(1,2)],
                 ((1,3),'D'):[(0,3)],
                   
                 ((1,4),'U'):[(2,4)],
                 ((1,4),'R'):[(1,4)],
                 ((1,4),'L'):[(1,3)],
                 ((1,4),'D'):[(0,4)],
                 
                 ((2,0),'U'):[(3,0)],
                 ((2,0),'R'):[(2,1)],
                 ((2,0),'L'):[(2,0)],
                 ((2,0),'D'):[(1,0)],
                 
                 ((2,1),'U'):[(3,1)],
                 ((2,1),'R'):[(2,2)],
                 ((2,1),'L'):[(2,0)],
                 ((2,1),'D'):[(1,1)],
                 
                 ((2,2),'U'):[(3,2)],
                 ((2,2),'R'):[(2,3)],
                 ((2,2),'L'):[(2,1)],
                 ((2,2),'D'):[(1,2)],
                 
                 ((2,3),'U'):[(3,3)],
                 ((2,3),'R'):[(2,4)],
                 ((2,3),'L'):[(2,2)],
                 ((2,3),'D'):[(1,3)],
                   
                 ((2,4),'U'):[(3,4)],
                 ((2,4),'R'):[(2,4)],
                 ((2,4),'L'):[(2,3)],
                 ((2,4),'D'):[(1,4)],
                     
                 ((3,0),'U'):[(4,0)],
                 ((3,0),'R'):[(3,1)],
                 ((3,0),'L'):[(3,0)],
                 ((3,0),'D'):[(2,0)],
                 
                 ((3,1),'U'):[(4,1)],
                 ((3,1),'R'):[(3,2)],
                 ((3,1),'L'):[(3,0)],
                 ((3,1),'D'):[(2,1)],
                 
                 ((3,2),'U'):[(4,2)],
                 ((3,2),'R'):[(3,3)],
                 ((3,2),'L'):[(3,1)],
                 ((3,2),'D'):[(2,2)],
                 
                 ((3,3),'U'):[(4,3)],
                 ((3,3),'R'):[(3,4)],
                 ((3,3),'L'):[(3,2)],
                 ((3,3),'D'):[(2,3)],
                   
                 ((3,4),'U'):[(4,4)],
                 ((3,4),'R'):[(3,4)],
                 ((3,4),'L'):[(3,3)],
                 ((3,4),'D'):[(2,4)],
                 
                 ((4,0),'U'):[(4,0)],
                 ((4,0),'R'):[(4,1)],
                 ((4,0),'L'):[(4,0)],
                 ((4,0),'D'):[(3,0)],
                 
                 ((4,1),'U'):[(4,1)],
                 ((4,1),'R'):[(4,2)],
                 ((4,1),'L'):[(4,0)],
                 ((4,1),'D'):[(3,1)],
                 
                 ((4,2),'U'):[(4,2)],
                 ((4,2),'R'):[(4,3)],
                 ((4,2),'L'):[(4,1)],
                 ((4,2),'D'):[(3,2)],
                 
                 ((4,3),'U'):[(4,3)],
                 ((4,3),'R'):[(4,4)],
                 ((4,3),'L'):[(4,2)],
                 ((4,3),'D'):[(3,3)],
                 
                 ((4,4),'U'):[(4,4)],
                 ((4,4),'R'):[(4,4)],
                 ((4,4),'L'):[(4,3)],
                 ((4,4),'D'):[(3,4)]}
        return s_list[state,action]
        
    def is_terminal (self, state) :
        return self.flag1*self.flag2*self.flag3*self.flag4*self.flagG==1 and state==(4,4)
        
    def transition (self,state,action):
        reward = -1
        if self.next_s(state,action)==[(1,4)] and self.flag1==0:
            self.flag1=1
            reward=10
            
        elif self.next_s(state,action)==[(3,1)]:
            if self.flag1==1 and self.flag2==0:
                reward = 10
                self.flag2 = 1
            elif self.flag1==0:
                reward= -2
                
        elif self.next_s(state,action)==[(1,0)]:
            if self.flag1==self.flag2==1 and self.flag3==0:
                reward = 10
                self.flag3 = 1
            elif self.flag1==0 or self.flag2==0:
                reward = -2
            
        elif self.next_s(state,action)==[(0,4)]:
            if self.flag1==self.flag2==self.flag3==1 and self.flag4==0:
                reward = 10
                self.flag4=1
            elif self.flag1==0 or self.flag2==2 or self.flag3==0:
                reward= -2
            
        elif self.next_s(state,action)==[(4,4)]:
            if self.flag1==self.flag2==self.flag3==self.flag4==1 and self.flagG==0:
                reward = 100
                self.flagG=1
            else: reward = -2
            
        return (self.next_s(state,action)[0], reward)
    


# In[20]:


x = Flags()

