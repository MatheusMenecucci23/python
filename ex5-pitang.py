z = (3, 10, 11, 8, 0, 4)
w = (2, 13, 11, 9, 7, 0)

def selection_sort(w, z):
    w = list(w)
    z = list(z)
    for i in range(len(w)):
        if w[i] > z[i]:
            x = z[i]
            z[i] = w[i]
            w[i] = x
        else:
            w[i] *= 2
            z[i] *= 3
    u = 0
    p = 0
    for i in range(len(w)):
        u = u + w[i]
        p = p+z[i]
        
    print(u,p)

selection_sort(w, z)
