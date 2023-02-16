import algoritmo_forza_bruta
import algoritmo_ricorsivo
import algoritmo_ricorsivo_mem
import algoritmo_bottom_up
import timeit
import random


def test_algoritmi():
    pattern = "abc"
    text = "abcdabc"
    print("Ricerca stringa tramite forza bruta:")
    print("Pattern:", pattern)
    print("Testo:", text)
    print("Risultato atteso:", [0, 4])
    result = algoritmo_forza_bruta.bruteforce(pattern, text)
    print("Risultato ottenuto:", result)
    print("")

    # Test per la funzione CUT_ROD
    p = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
    n = 4
    print("CUT_ROD:")
    print("Prezzi:", p)
    print("Lunghezza asta:", n)
    print("Risultato atteso:", 10)
    result = algoritmo_ricorsivo.CUT_ROD(p, n)
    print("Risultato ottenuto:", result)
    print("")

    # Test per la funzione MEMOIZED_CUT_ROD
    p = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
    n = 4
    print("MEMOIZED_CUT_ROD:")
    print("Prezzi:", p)
    print("Lunghezza asta:", n)
    print("Risultato atteso:", 10)
    result = algoritmo_ricorsivo_mem.MEMOIZED_CUT_ROD(p, n)
    print("Risultato ottenuto:", result)
    print("")

    # Test per la funzione BOTTOM_UP_CUT_ROD
    p = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
    n = 4
    print("BOTTOM_UP_CUT_ROD:")
    print("Prezzi:", p)
    print("Lunghezza asta:", n)
    print("Risultato atteso:", 10)
    result = algoritmo_bottom_up.BOTTOM_UP_CUT_ROD(p, n)
    print("Risultato ottenuto:", result)
    print("")

    # Test delle prestazioni degli algoritmi
    print("Confronto delle prestazioni: ")
    for n in range(10, 101, 10):
        # Generazione casuale di una lista di prezzi per l'asta
        p = [random.randint(1, 100) for i in range(n)]
        print("Lunghezza asta:", n)
        # Tempo di esecuzione della funzione CUT_ROD
        start = timeit.default_timer()
        algoritmo_ricorsivo.CUT_ROD(p, n)
        end = timeit.default_timer()
        print("Tempo di esecuzione CUT_ROD:", end - start)
        # Tempo di esecuzione della funzione MEMOIZED_CUT_ROD
        start = timeit.default_timer()
        algoritmo_ricorsivo_mem.MEMOIZED_CUT_ROD(p, n)
        end = timeit.default_timer()
        print("Tempo di esecuzione MEMOIZED_CUT_ROD:", end - start)
        # Tempo di esecuzione della funzione BOTTOM_UP_CUT_ROD
        start = timeit.default_timer()
        algoritmo_bottom_up.BOTTOM_UP_CUT_ROD(p, n)
        end = timeit.default_timer()
        print("Tempo di esecuzione BOTTOM_UP_CUT_ROD:", end - start)
        # Stampa di un separatore






