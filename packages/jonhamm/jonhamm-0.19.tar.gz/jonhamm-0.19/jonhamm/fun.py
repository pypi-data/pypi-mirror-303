import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d as interp
from scipy.optimize import minimize_scalar as mini
from scipy.optimize import root_scalar as root


def find_stable_points(cl):
  cl.sdotvec0=np.array([cl.sdot(i,cl.x(i)) for i in cl.s_grid])
  cl.sdotvec0[0]=max(0,cl.sdotvec0[0])
  cl.sdotvec0[-1]=min(0,cl.sdotvec0[-1])

  cl.signvec=np.sign(cl.sdotvec0).astype(int)
  cl.sign_diffs = np.diff(cl.signvec)
  cl.sign_change_indices = np.unique(np.r_[0,np.where(cl.sign_diffs!=0)[0],[len(cl.signvec)-1]])  # Skip first index
  
  
  cl.unstable_roots,cl.roots = [],[]
  for i,s in enumerate(cl.sign_change_indices[:-1]):  # Include 0th index and all sign changes

      a, b = max(0,cl.s_grid[cl.sign_change_indices[i]]-cl.ds), cl.s_grid[cl.sign_change_indices[i]]+cl.ds
      if cl.sdot(a,cl.x(a)) > cl.sdot(b,cl.x(b)):
        try:
          route=root(lambda s: cl.sdot(s,cl.x(s)),bracket=[a,b],method='brentq').root
          cl.roots.append(route)
        except:
          continue
  for i,s in enumerate(cl.sign_change_indices[:-1]):  # Include 0th index and all sign changes

      a, b = max(0,cl.s_grid[cl.sign_change_indices[i]]-cl.ds), cl.s_grid[cl.sign_change_indices[i]]+cl.ds
      if cl.sdot(a,cl.x(a)) < cl.sdot(b,cl.x(b)):
        try:
          route=root(lambda s: cl.sdot(s,cl.x(s)),bracket=[a,b],method='brentq').root
          cl.unstable_roots.append(route)
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

  # for r in cl.unstable_roots:
  #   if np.isin(r, cl.s_grid):
  #       cl.sdotvec0[np.where(cl.s_grid==r)]=0
  #       cl.signvec[np.where(cl.s_grid==r)]=0
  #       print(f"unstable root {r} is in the grid already")
  #   else:
  #       cl.s_grid=np.insert(cl.s_grid,0,r)
  #       cl.s_grid=np.unique(np.sort(cl.s_grid))
  #       cl.sdotvec0=np.insert(cl.sdotvec0,np.where(cl.s_grid==r)[0],0)
  #       cl.signvec=np.insert(cl.signvec,np.where(cl.s_grid==r)[0],0)
  #       print(f"unstable root {r} added to the grid")

  cl.all_roots=np.r_[cl.roots,cl.unstable_roots]

  cl.sfig, cl.sax = plt.subplots()
  cl.sax.plot(cl.s_grid,cl.sdotvec0)
  cl.sax.plot(cl.roots,[cl.sdot(i,cl.x(i)) for i in cl.roots],'ro',label='Stable Fixed Points')
  cl.sax.plot(cl.unstable_roots,[cl.sdot(i,cl.x(i)) for i in cl.unstable_roots],'ko',label='Unstable Fixed Points')


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

def vf_plot(cl,buffer_size=9):
  cl.indices = np.where(np.isin(cl.s_grid, cl.roots))[0]

  cl.buffered_indices = buffer_indices(cl.indices,buffer_size,len(cl.s_grid))

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

  cl.dtvec=v.copy()
  for i in range(len(cl.dtvec)):
    if i not in cl.indices:
        cl.dtvec=abs(cl.delta_s/cl.sdotvec)
  for i in range(len(cl.dtvec)):
    if i in cl.indices:
      if i==0:
        cl.dtvec[i]=cl.dtvec[1]
      elif i==len(cl.s_grid-1):
        cl.dtvec[i]=cl.dtvec[-2]
      else: 
        cl.dtvec[i]==(cl.dtvec[i-1]+cl.dtvec[i+1])/2
        
   

  
  

  
  
  for i in range(len(cl.s_grid)):
    next=cl.nextvec[i]
    if(cl.sdotvec[i]<0) and value_set[i]==0:
      v[i]=np.exp(-cl.δ*cl.dtvec[i])*v[next]+cl.wvec[i]*cl.dtvec[i]*np.exp(-cl.δ*cl.dtvec[i]/2)
      value_set[i]=1
  for i in reversed(range(len(cl.s_grid))):
    next=cl.nextvec[i]
    if(cl.sdotvec[i]>0) and value_set[i]==0:# and (errorvec[i]>.01):
      v[i]=np.exp(-cl.δ*cl.dtvec[i])*v[next]+cl.wvec[i]*cl.dtvec[i]*np.exp(-cl.δ*cl.dtvec[i]/2)
      value_set[i]=1
  cl.rhs=(np.gradient(v)/np.gradient(cl.s_grid)*cl.sdotvec0+cl.wvec0)/cl.δ
  cl.v=v

 
  cl.res=abs((cl.v-cl.rhs))
  print(f"Mean Square Residual is {np.mean(cl.res**2)}.")
  cl.vax.plot(cl.s_grid, cl.rhs,color='blue',label=r"$\frac{W(s)+V'(s)\dot{s}(s)}{\delta}$",zorder=1,lw=4)

  cl.vax.scatter(cl.s_grid[value_set==1], v[value_set==1],s=4,c='red',label='V(s)',zorder=2)
  cl.vax.legend()
  cl.vax.set_ylabel('Value: V(s)', fontsize=12)
  cl.vax.set_xlabel('Capital stock: $s$', fontsize=12)
  cl.vax.set_title('Value Function');


