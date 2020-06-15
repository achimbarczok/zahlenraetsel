#!/usr/bin/env python3
# Copyright (c) 2020 Achim Barczok (achim@barczok.de)
# All rights reserved.

import math

def berechnen(zahl1,zahl2,operator):
    # Berechnet eine Zahlenkombination per Addition, Subtraktion, Multiplikation, Division oder Potenz
    # gibt das Ergebnis als Int aus

    if operator == 0:
        return(zahl1 + zahl2)
    elif operator == 1:
        return(zahl1 - zahl2)
    elif operator == 2:
        return(zahl1 / zahl2)
    elif operator == 3:
        return(zahl1 * zahl2)
    elif operator == 4:
        if zahl2 < 10000 and zahl1 < 100:
            # Hier setzen wir sicherheitshalber ein Maximum, um zu lange Rechenzeiten bei Potenzen zu vermeiden
            return(zahl1 ** zahl2)
        else:
            pass
    else:
        return "Fehler"


def kombinationen(zahl1,zahl2,ergebnis):
    # Gibt eine Liste aller möglichen Kombinationen
    # Ausgabe erfolgt als String im Format "(1+1)*3*3"
    return()

def main():
    # Berechnet Zahlenraetsel nach Heinz Böer:
    # x ? y = z
    # wobei x und y je eine Würfelzahl von 1 bis 6 sind
    # Beide Würfel dürfen 0 bis 2 mal in einer Rechnung verwendet werden
    # Genutzt werden dürfen die 4 Grundrechenarten, Potenzieren und Fakultäten
    # Ziel ist es, eine Rechnung zu finden, die z ergibt, wobei Z zwischen 1 und 20 liegt
    # Beispiel

    zahlenliste= []

    #Beispiele nehmen
    zahlenliste.append(1)
    zahlenliste.append(2)

    #fakultät berücksichtigen!
    zahlenliste.append(math.factorial(zahlenliste[0]))
    zahlenliste.append(math.factorial(zahlenliste[2]))


main()
