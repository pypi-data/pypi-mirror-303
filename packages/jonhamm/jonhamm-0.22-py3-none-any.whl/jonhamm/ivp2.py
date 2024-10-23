import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp



def find_stable_points(cl):
  cl.sdotvec=np.array([cl.sdot(i) for i in cl.s_grid])
  cl.sdotvec[0]=max(0,cl.sdotvec[0])
  cl.sdotvec[-1]=min(0,cl.sdotvec[-1])

  cl.signvec=np.sign(cl.sdotvec).astype(int)
  cl.sign_diffs = np.diff(cl.signvec)
  cl.sign_change_indices = np.sort(np.unique(np.where(cl.sign_diffs!=0)[0]))
  cl.sign_changes=cl.s_grid[cl.sign_change_indices]

  cl.stable_roots,cl.unstable_roots = [],[]

  if cl.sdotvec[1]<0:
    cl.stable_roots.append(cl.sign_changes[0])



  for i,s in enumerate(cl.sign_changes):  # Include 0th index and all sign changes
      #print(f'looking at index {i,s}')
      a, b = s,s+cl.ds
      if cl.sdot(a) > cl.sdot(b):
         cl.stable_roots.append(s)
      else:
         cl.unstable_roots.append(s)

  if cl.sdotvec[-2]>0:
    cl.stable_roots.append(cl.sign_changes[-1])

  cl.stable_roots=np.unique(cl.stable_roots)
  cl.unstable_roots=np.unique(cl.unstable_roots)
  cl.endpoints=np.sort(np.unique(np.r_[cl.s_grid[0],cl.s_grid[-1],cl.stable_roots,cl.unstable_roots]))
  

  def dv_over_ds(s, v): return (cl.δ*v-cl.W(s))/cl.sdot(s)

  sols=[]
  print(f'the list of interval endpoints is {cl.endpoints}')
  print(f'the list of stable roots is {cl.stable_roots}')
  if cl.stable_roots[0]==cl.s_grid[0]:
    print(f'There is a stable fixed point at the first endpoint {cl.s_grid[0]}')
    a=cl.s_grid[1]
    b=cl.endpoints[1]-cl.ds
    v=cl.W(a)/cl.δ
    print(f'Next branch of the differential equation solution is: sols[{len(sols)}] on {[a,b]} with initial condition v({a})={v}' )

    sols.append(solve_ivp(dv_over_ds,[a,b],[v],method='Radau',dense_output=True,t_eval=np.linspace(a,b,100)))
    for i,s in enumerate(cl.endpoints[2:-1]):
      if s in cl.stable_roots:
          print(f'next stable root at endpoints[{i+2}]={s}')
          a=cl.endpoints[i+1]+cl.ds
          b=s
          c=cl.endpoints[i+3]-cl.ds
          v=cl.W(b)/cl.δ
          print(f'sols[{len(sols)}] on {[b,a]} with initial condition v({b})={v}' )
          sols.append(solve_ivp(dv_over_ds,[b,a],[v],t_eval=np.linspace(b,a,100)))
          print(f'sols[{len(sols)}] on {[b,c]} with initial condition v({b})={v}' )

          sols.append(solve_ivp(dv_over_ds,[b,c],[v],method='Radau',dense_output=True,t_eval=np.linspace(b,c,100)))
      else:
          print(f'unstable root at {s}')


  else:

    for i,s in enumerate(cl.endpoints[1:-1]):
      i+=1
      if s in cl.stable_roots:
          print(f'next stable root at endpoints[{i}]={s}')

          a=cl.endpoints[i-1]+cl.ds
          b=s
          c=cl.endpoints[i+1]-cl.ds
          v=cl.W(b)/cl.δ
          sols.append(solve_ivp(dv_over_ds,[b,a],[v],method='Radau',dense_output=True,t_eval=np.linspace(b,a,100)))
          sols.append(solve_ivp(dv_over_ds,[b,c],[v],method='Radau',dense_output=True,t_eval=np.linspace(b,c,100)))
  cl.sols=sols

  cl.fig, (cl.sax,cl.vax,cl.pax) = plt.subplots(3,1,figsize=(10,15),sharex=True)
  cl.fig.subplots_adjust(hspace=0)

  cl.sax.plot(cl.s_grid,cl.sdotvec,)
  cl.sax.set_ylabel(r"rate of change $\dot{s}$", )
  cl.sax.set_title('Stock Dynamics');



  cl.vax.set_xlabel('Capital stock: $s$', )
  cl.ds_grid,cl.v,cl.p=np.array([]),np.array([]),np.array([])
  for i in sols:
   if len(i.t)>0:
    cl.sax.plot(i.t[0],cl.sdot(i.t[0]),'ro')
    cl.sax.plot(i.t[-1],cl.sdot(i.t[-1]),'go')
    cl.vax.plot(i.t,i.y[0],)
    cl.vax.plot(i.t[0],i.y[0][0],'ro')
    cl.vax.plot(i.t[-1],i.y[0][-1],'go')


    cl.pax.plot(i.t,np.gradient(i.y[0])/np.gradient(i.t),)
    cl.pax.plot((i.t)[0],(np.gradient(i.y[0])/np.gradient(i.t))[0],'ro')
    cl.pax.plot((i.t)[-1],(np.gradient(i.y[0])/np.gradient(i.t))[-1],'go')

    cl.ds_grid = np.concatenate((cl.ds_grid, i.t), axis=0)
    cl.v = np.concatenate((cl.v, i.y[0]), axis=0)
    cl.p = np.concatenate((cl.p, np.gradient(i.y[0])/np.gradient(i.t)), axis=0)

    sorted_indices = sorted(range(len(cl.ds_grid)), key=lambda k: cl.ds_grid[k])
  cl.ds_grid = [cl.ds_grid[i] for i in sorted_indices]
  cl.v = [cl.v[i] for i in sorted_indices]
  cl.p = [cl.p[i] for i in sorted_indices]
 


  lines = [plt.Line2D([0], [0], label='manual point', marker='o',
         markeredgecolor='r', markerfacecolor='r', linestyle='') ,plt.Line2D([0], [0], label='manual point', marker='o',
         markeredgecolor='g', markerfacecolor='g', linestyle='')]
  labels = ['Stable', r'Unstable Interior or Non-Equilibria Exterior']
  cl.vax.yaxis.set_label_position("right")
  cl.vax.yaxis.tick_right()
  cl.vax.set_ylabel(r"Total Value: V(s)", )
  cl.sax.legend(lines, labels,loc=(.7,1))
  cl.pax.set_ylabel(r"Marginal Value: $\frac{dV}{ds}$", )
  cl.pax.set_ylim(0,99)
  cl.pax.set_xlabel(r'Initial capital stock: $s_0$')
  #cl.vax.legend()
  #cl.pax.legend()

