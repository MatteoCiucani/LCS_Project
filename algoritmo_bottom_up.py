def BOTTOM_UP_CUT_ROD(p, n):
    # Crea un array per memorizzare i massimi profitti
    r = [0] * (n + 1)

    # Itera su tutte le possibili lunghezze della verga
    for j in range(1, n + 1):
        q = float('-inf')

        # Itera su tutte le possibili combinazioni di taglio
        for i in range(j):
            q = max(q, p[i] + r[j - i - 1])

        # Memorizza il massimo profitto ottenibile per la lunghezza corrente
        r[j] = q

    # Restituisce il massimo profitto ottenibile tagliando la verga di lunghezza n
    return r[n]