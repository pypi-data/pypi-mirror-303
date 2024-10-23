import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d as interp
from scipy.optimize import minimize_scalar as mini
from scipy.optimize import root_scalar as root




def vf_plot(cl):
  cl.sdotvec0=np.array([cl.sdot(i,cl.x(i)) for i in cl.s_grid])
  cl.sdotvec0[0]=max(0,cl.sdotvec0[0])
  cl.sdotvec0[-1]=min(0,cl.sdotvec0[-1])

  cl.signvec=np.sign(cl.sdotvec0).astype(int)
 
  cl.wvec0=np.array([cl.W(s,cl.x(s)) for s in cl.s_grid])

  v=cl.wvec0/cl.δ
  value_set=0*v


  


  cl.delta_s=np.r_[np.gradient(cl.s_grid)]#np.r_[np.diff(cl.s_grid),0]

  cl.nextvec=range(len(cl.s_grid))+cl.signvec.astype(int)

  cl.sdotvec1=np.array([cl.sdot(cl.s_grid[i],cl.x(cl.s_grid[i])) for i in cl.nextvec])
  cl.wvec1=np.array([cl.W(cl.s_grid[i],cl.x(cl.s_grid[i])) for i in cl.nextvec])
  cl.wvec=.5*(cl.wvec0+cl.wvec1)
  cl.sdotvec=.5*(cl.sdotvec0+cl.sdotvec1)

  cl.dtvec=abs(cl.delta_s/cl.sdotvec)
  
  vold=v.copy()
  for i in range(1,len(cl.s_grid)):
    next=cl.nextvec[i]
    if(cl.sdotvec[i]<0) and value_set[i]==0:
      v[i]=np.exp(-cl.δ*cl.dtvec[i])*v[next]+cl.wvec[i]*cl.dtvec[i]*np.exp(-cl.δ*cl.dtvec[i]/2)

  for i in reversed(range(len(cl.s_grid))):
    next=cl.nextvec[i]
    if(cl.sdotvec[i]>0) and value_set[i]==0:# and (errorvec[i]>.01):
      v[i]=np.exp(-cl.δ*cl.dtvec[i])*v[next]+cl.wvec[i]*cl.dtvec[i]*np.exp(-cl.δ*cl.dtvec[i]/2)

  cl.v=v

 
  


def state_action_value(cl,s_grid,s, v_array,policy):

    v = interp(s_grid, v_array)
    sav=lambda x: cl.W(s,x)/cl.freq+ cl.β * v(min(max(s_grid[0],s+cl.sdot(s,x)/cl.freq),s_grid[-1]))

    if callable(policy):
      return sav(policy(s))
    else:
      return sav(policy)

def T(cl=[],v=[],s_grid=[],policy=None):
  if not list(s_grid):
    s_grid=cl.s_grid
  if not list(v):
     v=0*s_grid
  if policy==None:
    v_new = np.empty_like(v)
    x_new = np.empty_like(v)

    for i, s in enumerate(s_grid):
        # Maximize RHS of Bellman equation at state x
        foo=mini((lambda x: -state_action_value(cl,s_grid,s=s,v_array=v,policy=x)), bounds=(0, min(s,cl.policy_bound)),method='bounded')
        v_new[i]=-foo.fun
        x_new[i]=foo.x
    return v_new,x_new
  else:
    v_new = np.empty_like(v)

    for i, s in enumerate(s_grid):
      v_new[i] = state_action_value(cl,s_grid,s,v,policy)

    return v_new

def vfi_plot(cl=[],max_iter=1e2,initial_guess=[]):
 
  if not list(initial_guess):
      initial_guess=0*cl.s_grid
  v=initial_guess
  
  i = 0
  while i < max_iter:
        vf_plot(cl)
        tmp_T=T(cl,cl.v,cl.s_grid)
        v = tmp_T[0]
        cl.x=lambda s:interp(cl.s_grid,tmp_T[1])(s)
        i+=1
  