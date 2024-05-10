def selection_sort(vetor):
  achou = True
  while achou:
    achou = False
    for i in range(len(vetor) - 1):
      if vetor[i] > vetor[i + 1]:
        naosei = vetor[i]
        vetor[i] = vetor[i + 1]
        vetor[i + 1] = naosei
        achou = True

  return vetor

# Example usage
vetor = [81, 37, 51, 77, 19]
vetor = selection_sort(vetor)

for i in range(len(vetor)):
  print(vetor[i])
