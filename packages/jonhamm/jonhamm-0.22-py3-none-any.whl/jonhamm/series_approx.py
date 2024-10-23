def series_vapprox(cl,p):
  A = np.array([[cl.δ * s**j - cl.sdot(s,cl.x(s)) * j * s**(j - 1) for j in range(p + 1)] for s in cl.s_grid])
  coeffs = np.linalg.solve(A.T @ A, A.T @ [cl.W(s,cl.x(s)) for s in cl.s_grid])

  V_approx = np.sum([coeffs[i] * cl.s_grid**i for i in range(p + 1)], axis=0)
  for i in range(p + 1):
    1#plt.plot(cl.s_grid, coeffs[i] * cl.s_grid**i)
  plt.plot(cl.s_grid, V_approx, 'r--', lw=1, label=f"Least Squares Collocation: {p+1} Monomials on {cl.n} Uniform Nodes")
  #plt.plot(cl.s_grid,cl.s_grid**.5/1.5,lw=4)
  plt.xlabel(r'$s$: the stock level to be valued')
  plt.ylabel(r'$V(s):$ value')
  plt.legend()
  plt.show()
