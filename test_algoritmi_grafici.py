import random
import timeit
import matplotlib
import matplotlib.pyplot as plt
import algoritmo_forza_bruta
import algoritmo_ricorsivo
import algoritmo_ricorsivo_mem
import algoritmo_bottom_up
import numpy as np

def test_algoritmi_grafici():

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
    times_bruteforce = []
    times_cutrod = []
    times_memocutrod = []
    times_bottomup = []
    ns = range(10, 101, 10)
    for n in ns:
        # Generazione casuale di una lista di prezzi per l'asta
        p = [random.randint(1, 100) for i in range(n)]
        print("Lunghezza asta:", n)
        #tempo di esecuzione Forza Bruta
        start = timeit.default_timer()
        algoritmo_forza_bruta.bruteforce(pattern, text)
        end = timeit.default_timer()
        time_bruteforce = end - start
        times_bruteforce.append(time_bruteforce)
        print("Tempo di esecuzione FORZA BRUTA: ", end - start)

        # Tempo di esecuzione della funzione CUT_ROD
        start = timeit.default_timer()
        algoritmo_ricorsivo.CUT_ROD(p, n)
        end = timeit.default_timer()
        time_cutrod = end - start
        times_cutrod.append(time_cutrod)
        print("Tempo di esecuzione CUT_ROD:", end - start)

        # Tempo di esecuzione della funzione MEMOIZED_CUT_ROD
        start = timeit.default_timer()
        algoritmo_ricorsivo_mem.MEMOIZED_CUT_ROD(p, n)
        end = timeit.default_timer()
        time_memocutrod = end - start
        times_memocutrod.append(time_memocutrod)
        print("Tempo di esecuzione MEMOIZED_CUT_ROD:", end - start)
        # Tempo di esecuzione della funzione BOTTOM_UP_CUT_ROD
        start = timeit.default_timer()
        algoritmo_bottom_up.BOTTOM_UP_CUT_ROD(p, n)
        end = timeit.default_timer()
        time_bottomup = end - start
        times_bottomup.append(time_bottomup)
        print("Tempo di esecuzione BOTTOM_UP_CUT_ROD:", end - start)
        # Stampa di un separatore
        print("-----------------")



    y_bruteforce = times_bruteforce
    y_cutrod = times_cutrod
    y_memocutrod = times_memocutrod
    y_bottomup = times_bottomup

    plt.plot(ns, y_bruteforce, label='Forza Bruta')
    plt.plot(ns, y_cutrod, label='CUT_ROD')
    plt.plot(ns, y_memocutrod, label='MEMOIZED_CUT_ROD')
    plt.plot(ns, y_bottomup, label='BOTTOM_UP_CUT_ROD')

    plt.xlabel('Lunghezza asta')
    plt.ylabel('Tempo di esecuzione')
    plt.title('Prestazioni degli algoritmi')

    plt.legend()

    plt.show()


a = test_algoritmi_grafici()
print(a)


