import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def approxdef(deg, lb, ub, delta):
    '''
    The function defines an approximation space for all three
    approximation apporoaches (V, P, and Pdot).

    deg:    An array of degrees of approximation function: degrees of Chebyshev polynomials
    lb:     An array of lower bounds
    ub:     An array of upper bounds
    delta:  discount rate
    '''
    if (delta[0] > 1 or delta[0] < 0):
        raise Exception("delta should be in [0,1]!")

    dn = len(deg)
    dl = len(lb)
    du = len(ub)

    if (dn != dl):
        print("Dimension Mismatch: Stock dimension != lower bounds dimension")
    elif (dn != du) :
        print("Dimension Mismatch: Stock dimension != upper bounds dimension")
    else:
        param = dict({'degree': deg, 'lowerB': lb, 'upperB': ub, 'delta': delta})

    return param



def chebnodegen(n, a, b):
    '''
    The function generates uni-dimensional chebyshev nodes.

    n:   A number of nodes
    a:   The lower bound of inverval [a,b]
    b:   The upper bound of interval [a,b]

    Details:

    A polynomial approximant, S_i, over a bounded interval [a, b] is constructed by,
    s_i = (b + a)/2 + (b-a)/2 * cos((n - i + 0.5)/(n) * pi) for i = 1, 2, ..., n
    '''
    d1 = len(a)
    d2 = len(b)

    n = n[0]; a = a[0]; b = b[0]

    si = (a + b) * 0.5 + (b - a) * 0.5 * np.cos(np.pi * ((np.arange( (n - 1), -1, -1) + 0.5)/n))
    if (d1 != d2):
        raise Exception("Dimension Mismatch: dim(upper) != dim(lower)")

    return si



# stock = st[0]
# npol = 50
# a = 5e+06
# b = 359016000
# dorder = None



def chebbasisgen(stock, npol, a, b, dorder = None):
    '''
    The function calculates the monomial basis of Chebyshev polynomials for the
    given unidimensional nodes, s_i over a bounded interval [a,b].

    stock:      An array of Chebyshev polynomial nodes si (an array of stocks in capn-packages)
    npol:       Number of polynomials (n polynomials = (n-1)-th degree)
    a:          The lower bound of inverval [a,b]
    b:          The upper bound of inverval [a,b]
    dorder:     Degree of partial derivative of the

    Details:

    Suppose there are m numbers of Chebyshev nodes over a bounded interval [a, b]

    s_i in [a, b] for i = 1, 2, ..., m

    These nodes can be nomralized to the standard Chebyshev nodes over the domain [-1,1]:

    z_i = 2(s_i - a) / (b - a) - 1

    With normalized Chebyshev nodes, the recurrence relations of Chebyshev polynomials of order
    n is defined as:

    T0(zi) = 1
    T1(zi) = zi
    Tn(zi) = 2 z_i T_(n−1)(zi) − T_(n−2) (zi).

    The interpolation matrix (Vandermonde matrix) of (n-1)-th Chebyshev polynomials
    with m nodes, Φmn is:

           1  T1(z1) · · · Tn−1(z1) 
           1  T1(z2) · · · Tn−1(z2) 
           .    .    . . .    .     
    Φmn =  .    .    . . .    .     
           .    .    . . .    .     
           .    .    . . .    .     
           1  T1(zm) · · · Tn−1(zm) 

    The partial derivative of the monomial basis matrix can be found by the relation:

    (1 − z_i^2) T'_n (z_i) = n[T_(n - 1) (z_i) - z_i T_n(z_i)]
    '''
    if isinstance(stock, float):
        nknots = 1
    else:
        nknots = len(stock)

    # stock minus knots minus minimum divided by max - min
    z = (2 * stock - b - a) / (b - a)

    if (npol < 4):
        raise Exception("Degree of Chebyshev polynomial should be greater than 3!")

    # Initialize base matrix
    bvec = pd.DataFrame({'j=1': np.repeat(1, nknots), 'j=2': z})

    # Normalize Chebyshev nodes
    for j in np.arange(2, (npol)):
        Tj = pd.DataFrame({'jj': (2 * z * bvec.iloc[:, j - 1] - bvec.iloc[:, j - 2])})
        Tj = Tj.rename(columns={'jj': f"j={j+1}"})
        bvec = pd.concat([bvec, Tj], axis=1)

    if dorder is None:
        res = bvec

    elif (dorder == 1):
        bvecp = pd.DataFrame({'j=1': 0, 'j=2': np.repeat(2/(b - a), nknots)})

        # Generate interpolation matrix with n nodes
        for j in np.arange(2, (npol)):
            Tjp = pd.DataFrame({'jj': ((4/(b - a)) * bvec.iloc[:, j - 1] + 2 * z * bvecp.iloc[:, j - 1] - bvecp.iloc[:, j - 2])})
            Tjp = Tjp.rename(columns={'jj': f"j={j+1}"})
            bvecp = pd.concat([bvecp, Tjp], axis=1)

        res = bvecp

    else:
        raise Exception("dorder should be NULL or 1!")

    return res


# approxspace = Aspace
# sdata = simuDataV

def vapprox(approxspace, sdata):
    '''
    The function provides the V-approximation coefficients of the
    defined Chebyshev polynomials in aproxdef.

    degree:       degree of Chebyshev polynomial
    lowerB:       lower bound of Chebyshev nodes
    upperB:       upper bound of Chebyshev nodes
    delta:        discount rate
    coefficient:  Chebyshev polynomial coefficients

    Details:

    The V-approximation is finding the shadow price of i-th stock, pi for
    i = 1, · · · , d from the relation:
    δV = W(S) + p1s˙1 + p2s˙2 + · · · + pds˙d,

    where δ is the given discount rate, V is the intertemporal welfare
    function, S = (s1, s2, · · · , sd) is a vector of stocks, W(S) is the
    net benefits accruing to society, and \\dot{s}_i is the growth of stock si
    .
    By the definition of the shadow price, we know:

    p_i = ∂V / ∂s_i

    Consider approximation V (S) = µ(S)β, µ(S) is Chebyshev polynomials and β
    is their coeffcients. Then, pi = µ_si (S)β by the orthogonality of Chebyshev
    basis. Adopting the properties above, we can get the unknown coefficient
    vector β from:

    δµ(S)β = W(S) +\\sum_i=1^d diag(\\dot{s}_i) µ_si (S)β, and thus,

    β = [delta µ(S) - \\sum_i=1^d diag(\\dot{s}_i) µ_si (S)]^(−1) W(S).

    Additional case: over-determined (more nodes than approaximation degrees)

    '''
    deg = approxspace["degree"]
    lb = approxspace["lowerB"]
    ub = approxspace["upperB"]
    delta = approxspace["delta"]
    dd = len([deg])

    if isinstance(sdata, pd.DataFrame):
        sdata = sdata.to_numpy()

    if not isinstance(sdata, np.ndarray):
        print("sdata should be a data.frame or matrix of [stock, sdot, w]!")

    if (sdata.shape[1] != (2 * dd + 1)):
        print("The number of columns in sdata is not right!")

    # INCOMPLETE
    # if (dd > 1):
    #     ordername = f"sdata[, {dd}]"
    #     for di in np.arange(2, dd):
    #         odtemp = f"sdata[, {dd - di + 1}]"
    #         ordername = paste0([ordername, odtemp], sep = ", ")

    #     ordername = f"sdata[order({ordername}),]"

    #     sdata <- eval(parse(text = ordername))

    else:
        sdata = sdata[sdata[:, 0].argsort()]

    # Get unique nodes
    st = [np.unique(sdata[:, k]) for k in np.arange(0, dd)]

    # Get sdot values
    sdot = [sdata[:, k] for k in np.arange((dd + 0), (2 * dd))]

    # Get w (net-benefit) W(S)
    w = sdata[:, (2 * dd + 0)]

    # Setup matrices
    fphi = np.matrix(1)
    sphi = np.zeros(( int(( np.prod([len(k) for k in st]) * np.prod(deg)) / np.prod(deg)), np.prod(deg) ))

    # Generate Chebychev Approximation matrices
    for di in np.arange(0, dd):
        dk = dd - di - 1
        ftemp = chebbasisgen(st[dk], deg[dk], lb[dk], ub[dk])
        fphi = np.kron(fphi, ftemp)

        stempi = chebbasisgen(st[di], deg[di], lb[di], ub[di], dorder = 1)
        sphitemp = np.matrix(1)
        for dj in np.arange(0, dd):
            dk2 = dd - dj - 1
            if (dk2 != di):
                stemp = chebbasisgen(st[dk2], deg[dk2], lb[dk2], ub[dk2])
            else:
                stemp = stempi

            sphitemp = np.kron(sphitemp, stemp)

        #Calculate:  \\sum_i=1^d diag(\\dot{s}_i) µ_si (S)
        sphi = np.array(sphi) + np.array(sphitemp) * sdot[di][:, np.newaxis]

    # Calculate: [delta µ(S) - \\sum_i=1^d diag(\\dot{s}_i) µ_si (S)]^(−1)
    nsqr = delta[0] * np.array(fphi) - np.array(sphi)

    # Solve for all betas (shadow price)
    if (fphi.shape[0] == fphi.shape[1]):
        coeff = np.linalg.lstsq(nsqr, w, rcond=None)[0]
        res = dict({'degree': deg, 'lowerB': lb, 'upperB': ub,
            'delta': delta, 'coefficient': coeff})

    # Solve for beta when over-determined
    elif (fphi.shape[0] != fphi.shape[1]):
        coeff = np.linalg.lstsq(nsqr.T @ nsqr, nsqr.T @ w, rcond=None)[0]
        res = dict({'degree': deg, 'lowerB': lb, 'upperB': ub,
            'delta': delta, 'coefficient': coeff})

    return res



def vsim(vcoeff, adata, wval=None):
    '''
    The function provides the V-approximation simulation by adopting
    the results of vaprox. Available for multiple stock problems.
    '''

    deg = vcoeff["degree"]
    lb = vcoeff["lowerB"]
    ub = vcoeff["upperB"]
    delta = vcoeff["delta"]
    coeff = vcoeff['coefficient']
    nnodes = len(adata)
    dd = len(deg)

    if isinstance(adata, pd.DataFrame):
        st = adata.to_numpy()
    elif isinstance(adata, pd.Series):
        st = adata.to_numpy()
    elif isinstance(adata, np.matrix):
        st = adata
    else:
        raise Exception("st is not a matrix or data.frame")

    # Vectorized Chebyshev basis generation
    fphi = np.ones((nnodes, 1))  # Start with a column of ones
    sphi = np.zeros((nnodes, np.prod(deg)))
    accp = np.zeros((nnodes, dd))

    for di in range(dd):
        dk = dd - di - 1
        ftemp = chebbasisgen(st[dk], deg[dk], lb[dk], ub[dk])
        fphi = np.kron(fphi, ftemp)

        stempd = chebbasisgen(st[di], deg[di], lb[di], ub[di], dorder=1)
        sphitemp = np.ones((nnodes, 1))
        for dj in range(dd):
            dk2 = dd - dj - 1
            if dk2 != di:
                stemp = chebbasisgen(st[:, dk2], deg[dk2], lb[dk2], ub[dk2])
            else:
                stemp = stempd
            sphitemp = np.kron(sphitemp, stemp)

        sphi += sphitemp * st[di][ np.newaxis]  # Vectorized multiplication
        accp[:, di] = (sphi @ coeff).flatten()  # Matrix multiplication

    iwhat = accp.T * st
    iw = iwhat.ravel()
    vhat = fphi @ coeff

    if not isinstance(wval, np.ndarray):
        wval = "wval is not provided"

    res = {'shadowp': accp, 'iweach': iwhat, 'iw': iw,
           'vfun': vhat, 'stock': st, 'wval': wval}

    return res





def find_stable_points(cl,order):
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



  full_nodes=[]
  full_v=[]
  print(f'the list of interval endpoints is {cl.endpoints}')
  print(f'the list of stable roots is {cl.stable_roots}')
  if cl.stable_roots[0]==cl.s_grid[0]:
    print(f'There is a stable fixed point at the first endpoint {cl.s_grid[0]}')
    a=cl.s_grid[1]
    b=cl.endpoints[1]-cl.ds
    Aspace = approxdef([order],
                   [a],[b],
                   [cl.δ]) #defines the approximation space


    nodes = np.sort(np.r_[a,chebnodegen([order-1],
                     [a],
                    [b])]) #define the nodes
    simuDataV = pd.DataFrame({
  'nodes': nodes,
  'sdot': cl.sdot(nodes),
  'profit': cl.W(nodes)})

    vC = vapprox(Aspace, simuDataV)  #the approximated coefficent vector for prices


    SimV = vsim(vC,
              simuDataV.iloc[:, 0],
              cl.W(nodes))



    full_nodes.append(nodes)
    full_v.append(SimV['vfun'])

    for i,s in enumerate(cl.endpoints[2:-1]):
      if s in cl.stable_roots:
          print(f'next stable root at endpoints[{i+2}]={s}')
          a=cl.endpoints[i+1]+cl.ds
          b=cl.endpoints[i+3]-cl.ds
          Aspace = approxdef([order],
                   [a],[b],
                   [cl.δ]) #defines the approximation space


          nodes = np.sort(np.r_[s,chebnodegen([order-1],
                     [a],
                    [b])]) #define the nodes

          simuDataV = pd.DataFrame({'nodes': nodes,
            'sdot': cl.sdot(nodes),
             'profit': cl.W(nodes)})

          vC = vapprox(Aspace, simuDataV)  #the approximated coefficent vector for prices
          SimV = vsim(vC,
              simuDataV.iloc[:, 0],
              cl.W(nodes))
          full_nodes.append(nodes)
          full_v.append(SimV['vfun'])





      else:
          print(f'unstable root at {s}')


  else:

    for i,s in enumerate(cl.endpoints[1:-1]):
      i+=1
      if s in cl.stable_roots:
          print(f'next stable root at endpoints[{i}]={s}')

          a=cl.endpoints[i-1]+cl.ds
          b=cl.endpoints[i+1]-cl.ds
          Aspace = approxdef([order],
                   [a],[b],
                   [cl.δ]) #defines the approximation space


          nodes = np.sort(np.r_[s,chebnodegen([order-1],
                     [a],
                    [b])]) #define the nodes

          simuDataV = pd.DataFrame({'nodes': nodes,
            'sdot': cl.sdot(nodes),
             'profit': cl.W(nodes)})

          vC = vapprox(Aspace, simuDataV)  #the approximated coefficent vector for prices
          SimV = vsim(vC,
              simuDataV.iloc[:, 0],
              cl.W(nodes))
          full_nodes.append(nodes)
          full_v.append(SimV['vfun'])


  cl.full_v=np.array(full_v).flatten()
  cl.nodes=np.array(full_nodes).flatten()
