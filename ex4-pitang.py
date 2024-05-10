def VaiDarTrabalho():
  Z, B, A = 0, 0, 0
  veet = [0] * 15

  for Z in range(1, 14):
    B = Z + 1
    veet[Z] = B + (3 * Z)
    if Z > 0 :
        if(veet[B] < veet[Z]):
          A += 2
        else:
            A -=1
  
  if veet[5] > veet[10]:
    for Z in range(5, 15):
      veet[Z] += 1
  else:
    for Z in range(1, 10):
      veet[Z] -= 2

  print(veet[5])

# Chamada da função
VaiDarTrabalho()
