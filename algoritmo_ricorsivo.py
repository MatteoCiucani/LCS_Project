def CUT_ROD(p, n):
    """
    Implementazione dell'algoritmo CUT-ROD per trovare il massimo profitto ottenibile tagliando una verga di lunghezza n e vendendo i pezzi ottenuti ai prezzi indicati in un array p.
    """
    r = [0] * (n+1)
    for j in range(1, n+1):
        q = -1
        for i in range(1, j+1):
            q = max(q, p[i-1] + r[j-i])
        r[j] = q
    return r[n]