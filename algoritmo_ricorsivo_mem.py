def MEMOIZED_CUT_ROD(p, n):
    """
    Implementazione dell'algoritmo MEMOIZED-CUT-ROD per trovare il massimo profitto ottenibile tagliando
    una verga di lunghezza n e vendendo i pezzi ottenuti ai prezzi indicati in un array p.
    """
    r = [-1] * (n+1)
    return MEMOIZED_CUT_ROD_AUX(p, n, r)

def MEMOIZED_CUT_ROD_AUX(p, n, r):
    """
    Funzione di supporto per l'algoritmo MEMOIZED-CUT-ROD.
    """
    if r[n] >= 0:
        return r[n]
    if n == 0:
        q = 0
    else:
        q = -1
        for i in range(1, n+1):
            q = max(q, p[i-1] + MEMOIZED_CUT_ROD_AUX(p, n-i, r))
    r[n] = q
    return q