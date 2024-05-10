def qualquer(z, k):
  if z == k or z == 0:
    return 1
  else:
    return qualquer(z - 1, k) + qualquer(z - 1, k - 1)

print(qualquer(4,3))
