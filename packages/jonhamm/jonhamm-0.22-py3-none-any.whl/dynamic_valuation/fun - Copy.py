import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d as interp
from scipy.optimize import minimize_scalar as mini
from scipy.optimize import root_scalar as root


class Capital_Accumulation:

    def __init__(self,

                 n=100,
                 freq=1,
                 δ=1e-1,
                 A=2,
                 mps=.5, alpha=.3, delta = 0.4,x0 = 0.25,s_min=0, s_max = 9):


        self.A=A
        self.mps=mps
        self.alpha=alpha
        self.delta=delta



        self.δ=δ
        self.β=np.exp(-δ/freq)
        self.freq=freq


        self.s_min=1e-1
        self.s_max=s_max
        self.n=n
        self.ds=(self.s_max-self.s_min)/(self.n-1)
        self.eq=root(lambda s: self.sdot(s,self.x(s)),bracket=[self.s_min,self.s_max],method='brentq').root

        self.s_grid=np.append(np.append(np.arange(self.s_min, self.eq, self.ds),np.arange(self.eq,self.s_max,self.ds)),self.s_max)


    def x(self,s):
        return (1-self.mps)*s
    def sdot(self, s,x):
        return self.A *(s-x)**self.alpha-self.delta*s
    def W(self,s,x):
        return x**.5
capital_accumulation=Capital_Accumulation()
   

def vf(cl=capital_accumulation,s=None):
      if s==0:
        return 0
      if s==None:
        s=cl.eq
      if abs(s-cl.eq)<cl.ds:
        return cl.veq
      else:
        return  cl.W(s,cl.x(s))/cl.freq+cl.β*vf(cl,s+cl.sdot(s,cl.x(s))/cl.freq)

def state_action_value(cl,s_grid,s, v_array,policy):

    v = interp(s_grid, v_array)
    sav=lambda x: cl.W(s,x)/cl.freq+ cl.β * v(min(max(s_grid[0],s+cl.sdot(s,x)/cl.freq),s_grid[-1]))

    if callable(policy):
      return sav(policy(s))
    else:
      return sav(policy)

def T(cl=capital_accumulation,v=[],s_grid=[],policy=None):
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

def vfi_plot(cl=capital_accumulation,max_iter=1e2,s_grid=[],initial_guess=[],optimal=0,tol=0,policy=None,policy_iterations=0,ax_pol=1,plot=1):
  if not list(s_grid):
      s_grid=cl.s_grid
  if not list(initial_guess):
      initial_guess=0*s_grid
  if optimal==0 and policy==None:
      policy=cl.x

  fig, (ax1,ax2) = plt.subplots(2,1,sharex=True)

  v=initial_guess
  ax1.plot(s_grid, v, color=plt.cm.jet(0),
          lw=2, alpha=0.6, label='Initial guess')
  if ax_pol!=0:
    ax2.plot(s_grid,[cl.x(s) for s in s_grid], color=plt.cm.jet(0),
          lw=2, alpha=0.6, label='status quo policy')

  i = 0


  while i < max_iter and 1>tol:
      if optimal==0:

        v= T(cl,v,s_grid,policy)
      else:
        tmp=T(cl,v,s_grid)
        v_new = tmp[0]
        j=0
        xinterp=interp(s_grid,tmp[1])
        while j<=policy_iterations:
          v= T(cl,v,s_grid,policy=xinterp)
          ax1.plot(s_grid, v, color=plt.cm.jet(i /  max_iter), lw=2, alpha=0.6)
          j+=1
          if ax_pol!=0:
            ax2.plot(s_grid, tmp[1], color=plt.cm.jet(i /  max_iter), lw=2, alpha=0.6)

      ax1.plot(s_grid, v, color=plt.cm.jet(i /  max_iter), lw=2, alpha=0.6)

      i += 1


  ax1.plot(s_grid, v, color=plt.cm.jet(i / max_iter), lw=2, alpha=0.6,label='VFI approximation')
  if ax_pol!=0:
    if optimal!=0:
      ax2.plot(s_grid, tmp[1], color=plt.cm.jet(i /  max_iter), lw=2, alpha=0.6,label='improved policy')
    ax2.legend()
    ax2.set_ylabel('policy', fontsize=12)

  else:
    ax2.axis('off')
    fig.set_size_inches(9, 9)

  ax1.legend()


  ax1.set_ylabel('value', fontsize=12)
  ax1.set_xlabel('initial capital stock $s_0$', fontsize=12)
  ax1.set_title('Value function iterations')

  if optimal==0:
    cl.vn=v
  else:
    cl.v=v
    cl.improved_policy_vector=tmp[1]
  if plot==0:
     plt.close()


def plot_price(cl,max_iter=1e2,s_grid=[],initial_guess=[],optimal=0,tol=0,policy=None,policy_iterations=0,ax_pol=0,plot=1):
  vfi_plot(cl,max_iter,s_grid,initial_guess,optimal,tol,plot=0)
  if optimal==0:
    cl.pn=np.diff(cl.vn)/np.diff(s_grid)
    cl.pn=np.append(cl.pn,cl.pn[-1])
    fig, ax = plt.subplots()

    ax.plot(cl.s_grid,cl.pn)
    ax.set


def plot_fishery(cl):

  fig, ax = plt.subplots()

  ax.plot(cl.s_grid,[cl.f(s) for s in cl.s_grid],label='Natural Growth')
  ax.plot(cl.s_grid,[cl.h(s,cl.x(s)) for s in cl.s_grid],label='Harvest');
  ax.plot(cl.eq, cl.f(cl.eq), '-ro',label="equilibrium");
  ax.legend();

class Fishery:
    """
    This is a class that has all the parameters of the main fishery valuation in Fenichel & Abbott 2024
    to see the basic parameters: Fishy__

  c: the cost of a unit of a effort
  ds: the mesh size of the s_grid
  eq: the equilibrium of the fishery
  f: the growth rate of the fish stock as a function of the the fish stock
  freq: 1 is yearly, 12 is monthly, 365 is daily. 
  h: amount of fish harvest
  m: price of a unit of fish
  n: number of points in the s_grid
  policy_bound: this is the maximum that the policy function can take. In this case the maximum
  rate of fishing effort
  q:
 'r',
 's_grid',
 's_max',
 's_min',
 'sdot',
 'veq',
  x: fishing effort
 'y',
 'z',
 'α',
 'β',
 'γ',
 'δ'

    """
    def __init__(self,
                 s_min=1,
                 s_max=int(3.59e8),
                 freq=1,
                 δ=.02,
                 q=3.17e-4,
                 α=.544,
                 γ=.7882,
                 y=.157,
                 m=2.7,
                 c=153,
                 K=int(3.59e8),
                 z=1,
                 n=99,
                 r=.3847,
                 policy_bound=3.5e9):
                


        self.δ=δ
        self.β=np.exp(-δ/freq)
        self.freq=freq
        self.q=q
        self.α=α
        self.γ=γ
        self.y=y
        self.m=m
        self.c=c
        self.K=K
        self.s_min=s_min
        self.s_max=s_max
        self.z=z
        self.n=n
        self.r=r
        self.ds=(self.s_max-self.s_min)/(self.n-2)
        self.policy_bound=policy_bound
        self.eq=root(lambda s: self.sdot(s,self.x(s)),bracket=[self.s_min,self.s_max],method='brentq').root
        self.veq=(self.W(self.eq,self.x(self.eq)))/((self.freq)*(1-self.β))
        self.s_grid=np.append(np.append(np.arange(self.s_min, self.eq, self.ds),np.arange(self.eq,self.s_max,self.ds)),self.s_max)

    def x(self,s):

      return (self.y*s**self.γ)

    def f(self,s):
      return self.r*s*(1-s/self.K)
#this is per period growth
    def h(self,s,x):
      return ((self.q*s**self.z)*(x)**self.α)
#this is per period harvest as a function of the per period effort
    def sdot(self,s,x):
      return self.f(s)-self.h(s,x)
    def W(self,s,x):
      return (self.m*self.h(s,x)-self.c*x)



#####
def find_stable_points(cl):
  cl.sdotvec0=np.array([cl.sdot(i,cl.x(i)) for i in cl.s_grid])
  cl.sdotvec0[0]=max(0,cl.sdotvec0[0])
  cl.sdotvec0[-1]=min(0,cl.sdotvec0[-1])

  cl.signvec=np.sign(cl.sdotvec0).astype(int)
  cl.sign_diffs = np.diff(cl.signvec)
  cl.sign_change_indices = np.unique(np.r_[0,np.where(cl.sign_diffs!=0)[0],[len(cl.signvec)-1]])  # Skip first index
  
  
  cl.roots = []
  for i,s in enumerate(cl.sign_change_indices[:-1]):  # Include 0th index and all sign changes

      a, b = max(0,cl.s_grid[cl.sign_change_indices[i]]-cl.ds), cl.s_grid[cl.sign_change_indices[i]]+cl.ds
      if cl.sdot(a,cl.x(a)) > cl.sdot(b,cl.x(b)):
        try:
          route=root(lambda s: cl.sdot(s,cl.x(s)),bracket=[a,b],method='brentq').root
          cl.roots.append(route)
        except:
          continue


  for r in cl.roots:
    if np.isin(r, cl.s_grid):
        cl.sdotvec0[np.where(cl.s_grid==r)]=0
        cl.signvec[np.where(cl.s_grid==r)]=0
        print(f"stable root {r} is in the grid already")
    else:
        cl.s_grid=np.insert(cl.s_grid,0,r)
        cl.s_grid=np.unique(np.sort(cl.s_grid))
        cl.sdotvec0=np.insert(cl.sdotvec0,np.where(cl.s_grid==r)[0],0)
        cl.signvec=np.insert(cl.signvec,np.where(cl.s_grid==r)[0],0)
        print(f"stable root {r} added to the grid")


  cl.sfig, cl.sax = plt.subplots()
  cl.sax.plot(cl.s_grid,cl.sdotvec0)
  cl.sax.plot(cl.roots,[cl.sdot(i,cl.x(i)) for i in cl.roots],'ko',label='Stable Fixed Points')

  cl.sax.legend(loc='upper right')
  cl.sax.set_ylabel(r"rate of change $\dot{s}$", fontsize=12)
  cl.sax.set_xlabel('Capital stock: $s$', fontsize=12)
  cl.sax.set_title('Stock Dynamics');

  return cl.sfig

def buffer_indices(indices, buffer_size, set_length):
 
  buffered_indices = []
  for index in indices:
    start = max(0, index - buffer_size)
    end = min(set_length - 1, index + buffer_size + 1)
    buffered_indices.append(list(range(start, end)))

  return buffered_indices

def vf_plot(cl):
  cl.indices = np.where(np.isin(cl.s_grid, cl.roots))[0]

  cl.buffered_indices = buffer_indices(cl.indices,9 ,len(cl.s_grid))

  cl.wvec0=np.array([cl.W(s,cl.x(s)) for s in cl.s_grid])

  v=cl.wvec0/cl.δ
  value_set=0*v

  cl.vfig,cl.vax=plt.subplots()

  for i in range(len(cl.buffered_indices)):
    rudy=cl.roots[i]
    val=cl.W(rudy,cl.x(rudy))/cl.δ
    w_s=(cl.W(rudy+cl.ds,cl.x(rudy+cl.ds))-cl.W(rudy,cl.x(rudy)))/cl.ds
    sdot_s=(cl.sdot(rudy+cl.ds,cl.x(rudy+cl.ds))-cl.sdot(rudy,cl.x(rudy)))/cl.ds

    for j in range(len(cl.buffered_indices[i])):
      v[cl.buffered_indices[i][j]]=val+w_s/(cl.δ-sdot_s)*(cl.s_grid[cl.buffered_indices[i][j]]-rudy)
      value_set[cl.buffered_indices[i][j]]=i+1



  cl.vax.scatter(cl.s_grid[value_set>0], v[value_set>0],color='black',s=9,zorder=3)

  cl.delta_s=np.r_[np.gradient(cl.s_grid)]#np.r_[np.diff(cl.s_grid),0]

  cl.nextvec=range(len(cl.s_grid))+cl.signvec.astype(int)

  cl.sdotvec1=np.array([cl.sdot(cl.s_grid[i],cl.x(cl.s_grid[i])) for i in cl.nextvec])
  cl.wvec1=np.array([cl.W(cl.s_grid[i],cl.x(cl.s_grid[i])) for i in cl.nextvec])
  cl.wvec=.5*(cl.wvec0+cl.wvec1)
  cl.sdotvec=.5*(cl.sdotvec0+cl.sdotvec1)
  #absdot=[np.abs(i),0) for i in cl.sdotvec]
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

  rhs=(np.gradient(v)/np.gradient(cl.s_grid)*cl.sdotvec0+cl.wvec0)/cl.δ
  cl.v=v

 
  res=abs((v-rhs))
  print(f"Mean Residual is {np.mean(res)}.")
  cl.vax.plot(cl.s_grid, rhs,color='blue',label=r"$\frac{W(s)+V'(s)\dot{s}(s)}{\delta}$",zorder=1,lw=4)

  cl.vax.scatter(cl.s_grid[value_set==0], v[value_set==0],s=4,c='red',label='V(s)',zorder=2)
  cl.vax.legend()
  cl.vax.set_ylabel('Value: V(s)', fontsize=12)
  cl.vax.set_xlabel('Capital stock: $s$', fontsize=12)
  cl.vax.set_title('Value Function');



   