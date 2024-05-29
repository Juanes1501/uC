def prom(v):

  sum = 0
  k= len(v)

  for i in range(k):
     sum = sum + v[i]

  promedio = sum / k
  return promedio

def des_est(v):

   p=prom(v)
   sum = 0
   k = len(v)

   for i in range (k):
       
      sum = sum + (v[i] - p)**2

   de = sqrt(sum/k)
   return de

def varianza(v):

  de=des_est(V)

  var = de ** 2

  return var