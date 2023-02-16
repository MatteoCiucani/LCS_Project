def bruteforce(pattern, text):
    """
    Implementazione dell'algoritmo di forza bruta per trovare la posizione di un pattern all'interno di un testo.
    Restituisce una lista delle posizioni in cui il pattern è stato trovato.
    """
    positions = []
    n = len(text)
    m = len(pattern)
    for i in range(n - m + 1):
        j = 0
        while j < m and text[i+j] == pattern[j]:
            j += 1
        if j == m:
            positions.append(i)
    return positions